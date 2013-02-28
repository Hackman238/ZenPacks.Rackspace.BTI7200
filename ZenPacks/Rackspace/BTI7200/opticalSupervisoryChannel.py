from ZenPacks.Rackspace.BTI7200.Interface import Interface
from Products.ZenUtils.Utils import convToUnits, prepId

class opticalSupervisoryChannel(Interface): 
    # opticalSupervisoryChannel Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'opticalSupervisoryChannel'

    oscIdx = None
    oscIPAddr = None
    oscIPMask = None
    oscIPBcast = None
    oscType = None

    _properties = Interface._properties + (
        {'id':'oscIdx', 'type':'int', 'mode':'w'},
        {'id':'oscIPAddr', 'type':'string', 'mode':'w'},
        {'id':'oscIPMask', 'type':'string', 'mode':'w'},
        {'id':'oscIPBcast', 'type':'string', 'mode':'w'},
        {'id':'oscType', 'type':'int', 'mode':'w'},
        )
