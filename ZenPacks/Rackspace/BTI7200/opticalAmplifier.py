from ZenPacks.Rackspace.BTI7200.Interface import Interface
from Products.ZenUtils.Utils import convToUnits, prepId

class opticalAmplifier(Interface): 
    # opticalAmplifier Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'opticalAmplifier'

    oType = None
    oIdx = None
    oModeSetting = None
    oGainSetting = None
    oPwrSetting = None
    oTiltCompSetting = None
    oStatus = None
    oLaserStatus = None
    oId2 = None
    oNumChannels = None
    oCustom2 = None
    oCustom3 = None

    _properties = Interface._properties + (
        {'id':'oType', 'type':'int', 'mode':'w'},
        {'id':'oIdx', 'type':'int', 'mode':'w'},
        {'id':'oModeSetting', 'type':'int', 'mode':'w'},
        {'id':'oGainSetting', 'type':'int', 'mode':'w'},
        {'id':'oPwrSetting', 'type':'int', 'mode':'w'},
        {'id':'oTiltCompSetting', 'type':'int', 'mode':'w'},
        {'id':'oStatus', 'type':'int', 'mode':'w'},
        {'id':'oLaserStatus', 'type':'int', 'mode':'w'},
        {'id':'oId2', 'type':'string', 'mode':'w'},
        {'id':'oFiberType', 'type':'string', 'mode':'w'},
        {'id':'oNumChannels', 'type':'int', 'mode':'w'},
        {'id':'oCustom2', 'type':'string', 'mode':'w'},
        {'id':'oCustom3', 'type':'string', 'mode':'w'},
        )
