from zope.event import notify

import Products.ZenEvents.ZenEventClasses as ZenEventClasses
from Products.ZenModel.IpInterface import IpInterface
from Products.ZenRelations.RelSchema import ToMany, ToOne
from Products.Zuul.catalog.events import IndexingEvent
from Products.Zuul.interfaces import ICatalogTool


class Interface(IpInterface):
    portal_type = meta_type = 'bitInterface'

    intShelfIdx = None
    intSlotIdx = None
    intPortIdx = None
    intPEC = None
    intOperStatQlfr = None
    intWavelengthx10 = None
    intVendorPN1 = None
    intVendorPN2 = None
    intVendorPN3 = None
    intPhyPMMon = None
    intFPSD = None
    intId1 = None
    intFiberType = None
    intMediaRate = None
    intRemoteId = None

    _properties = IpInterface._properties + (
        {'id': 'intShelfIdx', 'type': 'int', 'mode': 'w'},
        {'id': 'intSlotIdx', 'type': 'int', 'mode': 'w'},
        {'id': 'intPortIdx', 'type': 'int', 'mode': 'w'},
        {'id': 'intPEC', 'type': 'string', 'mode': 'w'},
        {'id': 'intOperStatQlfr', 'type': 'int', 'mode': 'w'},
        {'id': 'intWavelengthx10', 'type': 'int', 'mode': 'w'},
        {'id': 'intVendorPN1', 'type': 'string', 'mode': 'w'},
        {'id': 'intVendorPN2', 'type': 'string', 'mode': 'w'},
        {'id': 'intVendorPN3', 'type': 'string', 'mode': 'w'},
        {'id': 'intPhyPMMon', 'type': 'int', 'mode': 'w'},
        {'id': 'intFPSD', 'type': 'int', 'mode': 'w'},
        {'id': 'intId1', 'type': 'int', 'mode': 'w'},
        {'id': 'intFiberType', 'type': 'int', 'mode': 'w'},
        {'id': 'intMediaRate', 'type': 'int', 'mode': 'w'},
        {'id': 'intRemoteId', 'type': 'string', 'mode': 'w'},
        )

    # Used by StatusThreshold to map collected status identifiers to event
    # severities and string representations.
    status_maps = {
        'ifAdminStatus_ifAdminStatus': {
            1: (ZenEventClasses.Clear, 'up'),
            2: (ZenEventClasses.Critical, 'down'),
            3: (ZenEventClasses.Critical, 'testing'),
            },

        'ifOperStatus_ifOperStatus': {
            1: (ZenEventClasses.Clear, 'up'),
            2: (ZenEventClasses.Critical, 'down'),
            3: (ZenEventClasses.Critical, 'testing'),
            4: (ZenEventClasses.Critical, 'unknown'),
            5: (ZenEventClasses.Critical, 'dormant'),
            6: (ZenEventClasses.Critical, 'not present'),
            7: (ZenEventClasses.Critical, 'lower layer down'),
            },
        }

    def snmpIgnore(self):
        """Ignore interface that are administratively down."""
        return self.adminStatus != 1 or self.monitor == False

    def getRRDTemplateName(self):
        # Return the interface type as the target type name.
        return self.prepId(self.type or 'Unknown')

    def getRRDTemplates(self):
        # Return a list containing the appropriate RRDTemplate.
        templateName = self.getRRDTemplateName()
        default = self.getRRDTemplateByName(templateName)

        if not default:
            default = self.getRRDTemplateByName('Unknown')

        if default:
            return [default]
        return []
