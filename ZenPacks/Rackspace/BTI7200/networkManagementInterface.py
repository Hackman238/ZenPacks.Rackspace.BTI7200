from ZenPacks.Rackspace.BTI7200.Interface import Interface
from Products.ZenUtils.Utils import convToUnits, prepId

class networkManagementInterface(Interface): 
    # networkManagementInterface Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'networkManagementInterface'

    netMgmtIdx = None
    netMgmtIPAddr = None
    netMgmtIPMask = None
    netMgmtIPBcast = None
    netMgmtType = None

    _properties = Interface._properties + (
        {'id':'netMgmtIdx', 'type':'int', 'mode':'w'},
        {'id':'netMgmtIPAddr', 'type':'string', 'mode':'w'},
        {'id':'netMgmtIPMask', 'type':'string', 'mode':'w'},
        {'id':'netMgmtIPBcast', 'type':'string', 'mode':'w'},
        {'id':'netMgmtType', 'type':'int', 'mode':'w'},
        )
