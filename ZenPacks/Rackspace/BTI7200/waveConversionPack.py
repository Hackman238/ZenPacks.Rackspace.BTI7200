from ZenPacks.Rackspace.BTI7200.Interface import Interface
from Products.ZenUtils.Utils import convToUnits, prepId

class waveConversionPack(Interface): 
    # waveConversionPack Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'waveConversionPack'

    xcvrTypeIdx = None 
    xcvrType = None 
    xcvrIdx = None
    xcvrProtSwEvtType = None
    xcvrProtocol = None
    xcvrLaserStatus = None
    xcvrId2 = None
    xcvrCustom2 = None
    xcvrCustom3 = None
    xcvrTraceLabel = None
    xcvrExpectedTraceLabel = None
    xcvrReceivedTraceLabel = None
    xcvrSDBERTh = None
    xcvrLoopbackType = None

    _properties = Interface._properties + (
        {'id':'xcvrTypeIdx', 'type':'int', 'mode':'w'},
        {'id':'xcvrType', 'type':'int', 'mode':'w'},
        {'id':'xcvrIdx', 'type':'int', 'mode':'w'},
        {'id':'xcvrProtSwEvtType', 'type':'int', 'mode':'w'},
        {'id':'xcvrProtocol', 'type':'int', 'mode':'w'},
        {'id':'xcvrLaserStatus', 'type':'int', 'mode':'w'},
        {'id':'xcvrId2', 'type':'string', 'mode':'w'},
        {'id':'xcvrCustom2', 'type':'string', 'mode':'w'},
        {'id':'xcvrCustom3', 'type':'string', 'mode':'w'},
        {'id':'xcvrTraceLabel', 'type':'string', 'mode':'w'},
        {'id':'xcvrExpectedTraceLabel', 'type':'string', 'mode':'w'},
        {'id':'xcvrReceivedTraceLabel', 'type':'string', 'mode':'w'},
	    {'id':'xcvrSDBERTh', 'type':'int', 'mode':'w'},
        {'id':'xcvrLoopbackType', 'type':'int', 'mode':'w'},
        )
