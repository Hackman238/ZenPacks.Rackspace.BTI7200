import re

from Products.AdvancedQuery import And, Eq, Or

import Products.ZenEvents.ZenEventClasses as ZenEventClasses
from Products.Zuul.interfaces import ICatalogTool


def add_local_lib_path():
    """Helper to add the ZenPack's lib directory to PYTHONPATH."""
    import os
    import site

    site.addsitedir(os.path.join(os.path.dirname(__file__), 'lib'))


class EntityBase(object):
    description = None
    hardware_version = None
    firmware_version = None
    software_version = None
    fru = None
    assy_number = None
    assy_revision = None
    assy_clei = None

    _properties = (
        {'id': 'description', 'type': 'string', 'mode': 'w'},
        {'id': 'hardware_version', 'type': 'string', 'mode': 'w'},
        {'id': 'firmware_version', 'type': 'string', 'mode': 'w'},
        {'id': 'software_version', 'type': 'string', 'mode': 'w'},
        {'id': 'fru', 'type': 'boolean', 'mode': 'w'},
        {'id': 'assy_number', 'type': 'string', 'mode': 'w'},
        {'id': 'assy_revision', 'type': 'string', 'mode': 'w'},
        {'id': 'assy_clei', 'type': 'string', 'mode': 'w'},
        )

    # Used by StatusThreshold to map collected status identifiers to event
    # severities and string representations.
    status_maps = {
        'entStateOper': {
            1: (ZenEventClasses.Error, 'unknown'),
            2: (ZenEventClasses.Clear, 'disabled'),
            3: (ZenEventClasses.Clear, 'enabled'),
            4: (ZenEventClasses.Critical, 'testing'),
            }
        }


class FRUBase(EntityBase):
    admin_status = None
    oper_status = None
    current_multiplier = 1

    _properties = EntityBase._properties + (
        {'id': 'admin_status', 'type': 'string', 'mode': 'w'},
        {'id': 'oper_status', 'type': 'string', 'mode': 'w'},
        {'id': 'current_multiplier', 'type': 'float', 'mode': 'w'},
        )

    status_maps = dict({
        'cefcFRUPowerOperStatus_cefcFRUPowerOperStatus': {
            1: (ZenEventClasses.Critical, 'off (other)'),
            2: (ZenEventClasses.Clear, 'on'),
            3: (ZenEventClasses.Info, 'off (admin)'),
            4: (ZenEventClasses.Critical, 'off (denied)'),
            5: (ZenEventClasses.Critical, 'off (environmental)'),
            6: (ZenEventClasses.Critical, 'off (temperature)'),
            7: (ZenEventClasses.Critical, 'off (fan)'),
            8: (ZenEventClasses.Critical, 'failed'),
            9: (ZenEventClasses.Error, 'on (fan failed)'),
            10: (ZenEventClasses.Critical, 'off (cooling)'),
            11: (ZenEventClasses.Critical, 'off (connector rating)'),
            12: (ZenEventClasses.Error, 'on (no inline power)'),
            },
        }, **EntityBase.status_maps)


def keyword_search(obj, keyword, types=(), meta_type=None):
    """Generate objects with a matching serial number."""
    keyword_query = Eq('searchKeywords', keyword)

    query = None
    if meta_type:
        query = And(Eq('meta_type', meta_type), keyword_query)
    else:
        query = keyword_query

    for brain in ICatalogTool(obj.dmd).search(types, query=query):
        yield brain.getObject()


def device_ip_search(obj, ip_address):
    """Return a device given an IP address."""
    device = obj.getDmdRoot('Devices').findDevice(ip_address)
    if device:
        return device

    ip = obj.getDmdRoot('Networks').findIp(ip_address)
    if ip:
        return ip.device()


def interfaces_by_names(device, interface_names, type_='Interface'):
    """Yield Interface objects matching the given names."""
    catalog = ICatalogTool(device.primaryAq())

    name_equals = (Eq('name', x) for x in interface_names)

    search_results = catalog.search(
        types=('ZenPacks.Rackspace.BTI7200.%s.%s' % (type_, type_,)),
        query=Or(*name_equals))

    for result in search_results.results:
        yield result.getObject()


def interfaces_by_type(device, type_):
    """Yield Interface objects matching the given type."""
    catalog = ICatalogTool(device.primaryAq())

    search_results = catalog.search(
        types=('ZenPacks.Rackspace.BTI7200.%s.%s' % (type_, type_)))

    for result in search_results.results:
        yield result.getObject()


def interfaces_by_name(device, interface_name, type_='Interface'):
    """Yield Interface objects matching the given name."""
    for result in interfaces_by_names(device, (interface_name,), type_=type_):
        yield result


def oid_to_string(oid):
    return ''.join(map(chr, map(int, oid.split('.'))))


def snmp_ifDescr(short_ifname):
    """Return the IF-MIB::ifDescr for a short Cisco interface name."""
    prefix_map = {
        'Lo': 'Loopback',
        'Po': 'Port-channel',
        'Vl': 'Vlan',
        'Te': 'TenGigabitEthernet',
        'Gi': 'GigabitEthernet',
        'Eth': 'Ethernet',
        }

    match = re.search(r'^([^\d]+)(\d.*)$', short_ifname)
    if match:
        return '%s%s' % (prefix_map.get(
            match.group(1), match.group(1)), match.group(2))

    return short_ifname


def string_to_int(value):
    """Convert value to integer for valid comparison."""
    try:
        i = int(value)
    except ValueError:
        i = value

    return i


def lookup_if_admin_status(value):
    """Resolve IF-MIB::ifAdminStatus to string."""
    return {
        1: 'up',
        2: 'down',
        3: 'testing',
        }.get(string_to_int(value), 'unknown')


def lookup_if_oper_status(value):
    """Resolve IF-MIB::ifOperStatus to string."""
    return {
        1: 'up',
        2: 'down',
        3: 'testing',
        4: 'unknown',
        5: 'dormant',
        6: 'not present',
        7: 'lower layer down',
        }.get(string_to_int(value), 'unknown')


def lookup_truth_value(value):
    """Resolve SNMPv2-TC::TruthValue value to boolean."""
    return {
        1: True,
        2: False,
        }.get(string_to_int(value), None)


def lookup_physical_class(value):
    """Resolve ENTITY-MIB::PhysicalClass value to string."""
    return {
        1: 'other',
        2: 'unknown',
        3: 'chassis',
        4: 'backplane',
        5: 'container',
        6: 'power supply',
        7: 'fan',
        8: 'sensor',
        9: 'module',
        10: 'port',
        11: 'stack',
        12: 'CPU',
        }.get(string_to_int(value), 'unknown')


def lookup_EntityAdminState(value):
    """Resolve ENTITY-STATE-TC-MIB::EntityAdminState to string."""
    return {
        1: 'unknown',
        2: 'locked',
        3: 'shuttingDown',
        4: 'unlocked',
        }.get(string_to_int(value), 'unknown')


def lookup_EntityOperState(value):
    """Resolve ENTITY-STATE-TC-MIB::EntityOperState to string."""
    return {
        1: 'unknown',
        2: 'disabled',
        3: 'enabled',
        4: 'testing',
        }.get(string_to_int(value), 'unknown')
