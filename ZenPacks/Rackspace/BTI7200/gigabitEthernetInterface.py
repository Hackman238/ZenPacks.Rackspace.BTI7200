from ZenPacks.Rackspace.BTI7200.Interface import Interface
from Products.ZenUtils.Utils import convToUnits, prepId

class gigabitEthernetInterface(Interface): 
    # gigabitEthernetInterface Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'gigabitEthernetInterface'

    geGfpMode = None
    geFlowControl = None

    _properties = Interface._properties + (
        {'id':'geGfpMode', 'type':'int', 'mode':'w'},
        {'id':'geFlowControl', 'type':'int', 'mode':'w'},
        )
