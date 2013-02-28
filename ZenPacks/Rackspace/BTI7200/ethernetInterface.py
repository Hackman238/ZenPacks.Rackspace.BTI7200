from ZenPacks.Rackspace.BTI7200.Interface import Interface
from Products.ZenUtils.Utils import convToUnits, prepId

class ethernetInterface(Interface): 
    # ethernetInterface Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'ethernetInterface'

    ethIntfPortTypeIdx = None
    ethIntfLinkStatus = None
    ethIntfLagId = None
    ethIntfLagPortPriority = None
    ethIntfBER = None
    ethIntfLineMapping = None
    ethIntfErrorCorrection = None
    ethIntfLpbkOpCmd = None

    _properties = Interface._properties + (
        {'id':'ethIntfPortTypeIdx', 'type':'int', 'mode':'w'},
        {'id':'ethIntfLinkStatus', 'type':'int', 'mode':'w'},
        {'id':'ethIntfLagId', 'type':'int', 'mode':'w'},
        {'id':'ethIntfLagPortPriority', 'type':'int', 'mode':'w'},
        {'id':'ethIntfBER', 'type':'int', 'mode':'w'},
        {'id':'ethIntfLineMapping', 'type':'int', 'mode':'w'},
        {'id':'ethIntfErrorCorrection', 'type':'int', 'mode':'w'},
        {'id':'ethIntfLpbkOpCmd', 'type':'int', 'mode':'w'},
        )
