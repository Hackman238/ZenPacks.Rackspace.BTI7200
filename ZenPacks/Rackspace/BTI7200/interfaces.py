from Products.Zuul.interfaces import IComponentInfo, IIpInterfaceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.Zuul.interfaces import IDeviceInfo

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IInterfaceInfo(IIpInterfaceInfo):
    '''
    Info adapter interface for common BTI interface components.
    '''
    intShelfIdx = schema.Text(title=_t(u'intShelfIdx'), readonly=True, group='Details')
    intSlotIdx = schema.Text(title=_t(u'intSlotIdx'), readonly=True, group='Details')
    intPortIdx = schema.Text(title=_t(u'intPortIdx'), readonly=True, group='Details')
    intPEC = schema.Text(title=_t(u'intPEC'), readonly=True, group='Details')
    intOperStatQlfr = schema.Text(title=_t(u'intOperStatQlfr'), readonly=True, group='Details')
    intWavelengthx10 = schema.Text(title=_t(u'intWavelengthx10'), readonly=True, group='Details')
    intVendorPN1 = schema.Text(title=_t(u'intVendorPN1'), readonly=True, group='Details')
    intVendorPN2 = schema.Text(title=_t(u'intVendorPN2'), readonly=True, group='Details')
    intVendorPN3 = schema.Text(title=_t(u'intVendorPN3'), readonly=True, group='Details')
    intPhyPMMon = schema.Text(title=_t(u'intPhyPMMon'), readonly=True, group='Details')
    intFPSD = schema.Text(title=_t(u'intFPSD'), readonly=True, group='Details')
    intId1 = schema.Text(title=_t(u'intId1'), readonly=True, group='Details')
    intFiberType = schema.Text(title=_t(u'intFiberType'), readonly=True, group='Details')
    intMediaRate = schema.Text(title=_t(u'intMediaRate'), readonly=True, group='Details')
    intRemoteId = schema.Text(title=_t(u'intRemoteId'), readonly=True, group='Details')


class IserialPortInfo(IComponentInfo):
    '''
    Info adapter interface for BTI serial port components.
    '''
    serialPortIdx = schema.Text(title=_t(u'serialPortIdx'), readonly=True, group='Details')
    serialBaudRate = schema.Text(title=_t(u'serialBaudRate'), readonly=True, group='Details')
    serialDataBits = schema.Text(title=_t(u'serialDataBits'), readonly=True, group='Details')
    serialParity = schema.Text(title=_t(u'serialParity'), readonly=True, group='Details')
    serialStopBits = schema.Text(title=_t(u'serialStopBits'), readonly=True, group='Details')


class IethernetInterfaceInfo(IInterfaceInfo):
    '''
    Info adapter interface for BTI ethernet interface components.
    '''
    ethIntfPortTypeIdx = schema.Text(title=_t(u'ethIntfPortTypeIdx'), readonly=True, group='Details')
    ethIntfLinkStatus = schema.Text(title=_t(u'ethIntfLinkStatus'), readonly=True, group='Details')
    ethIntfLagId = schema.Text(title=_t(u'ethIntfLagId'), readonly=True, group='Details')
    ethIntfLagPortPriority = schema.Text(title=_t(u'ethIntfLagPortPriority'), readonly=True, group='Details')
    ethIntfBER = schema.Text(title=_t(u'ethIntfBER'), readonly=True, group='Details')
    ethIntfLineMapping = schema.Text(title=_t(u'ethIntfLineMapping'), readonly=True, group='Details')
    ethIntfErrorCorrection = schema.Text(title=_t(u'ethIntfErrorCorrection'), readonly=True, group='Details')
    ethIntfLpbkOpCmd = schema.Text(title=_t(u'ethIntfLpbkOpCmd'), readonly=True, group='Details')


class IgigabitEthernetInterfaceInfo(IInterfaceInfo):
    '''
    Info adapter interface for BTI gigabit interface components.
    '''
    geGfpMode = schema.Text(title=_t(u'geGfpMode'), readonly=True, group='Details')
    geFlowControl = schema.Text(title=_t(u'geFlowControl'), readonly=True, group='Details')


class InetworkManagementInterfaceInfo(IInterfaceInfo):
    '''
    Info adapter interface for BTI management interface components.
    '''
    netMgmtIdx = schema.Text(title=_t(u'netMgmtIdx'), readonly=True, group='Details')
    netMgmtType = schema.Text(title=_t(u'netMgmtType'), readonly=True, group='Details')


class IopticalAmplifierInfo(IInterfaceInfo):
    '''
    Info adapter interface for BTI optical amplification components.
    '''
    oType = schema.Text(title=_t(u'oType'), readonly=True, group='Details')
    oIdx = schema.Text(title=_t(u'oIdx'), readonly=True, group='Details')
    oModeSetting = schema.Text(title=_t(u'oModeSetting'), readonly=True, group='Details')
    oGainSetting = schema.Text(title=_t(u'oGainSetting'), readonly=True, group='Details')
    oPwrSetting = schema.Text(title=_t(u'oPwrSetting'), readonly=True, group='Details')
    oTiltCompSetting = schema.Text(title=_t(u'oTiltCompSetting'), readonly=True, group='Details')
    oStatus = schema.Text(title=_t(u'oStatus'), readonly=True, group='Details')
    oLaserStatus = schema.Text(title=_t(u'oLaserStatus'), readonly=True, group='Details')
    oId2 = schema.Text(title=_t(u'oId2'), readonly=True, group='Details')
    oNumChannels = schema.Text(title=_t(u'oNumChannels'), readonly=True, group='Details')
    oCustom2 = schema.Text(title=_t(u'oCustom2'), readonly=True, group='Details')
    oCustom3 = schema.Text(title=_t(u'oCustom3'), readonly=True, group='Details')


class IopticalSupervisoryChannelInfo(IInterfaceInfo):
    '''
    Info adapter interface for BTI optical supervisory channel components.
    '''
    oscIdx = schema.Text(title=_t(u'oscIdx'), readonly=True, group='Details')
    oscIPAddr = schema.Text(title=_t(u'oscIPAddr'), readonly=True, group='Details')
    oscIPMask = schema.Text(title=_t(u'oscIPMask'), readonly=True, group='Details')
    oscIPBcast = schema.Text(title=_t(u'oscIPBcast'), readonly=True, group='Details')
    oscType = schema.Text(title=_t(u'oscType'), readonly=True, group='Details')


class IwaveConversionPackInfo(IInterfaceInfo):
    '''
    Info adapter interface for BTI wave conversion pack components.
    '''
    xcvrTypeIdx = schema.Text(title=_t(u'xcvrTypeIdx'), readonly=True, group='Details')
    xcvrType = schema.Text(title=_t(u'xcvrType'), readonly=True, group='Details')
    xcvrIdx = schema.Text(title=_t(u'xcvrIdx'), readonly=True, group='Details')
    xcvrProtSwEvtType = schema.Text(title=_t(u'xcvrProtSwEvtType'), readonly=True, group='Details')
    xcvrProtocol = schema.Text(title=_t(u'xcvrProtocol'), readonly=True, group='Details')
    xcvrLaserStatus = schema.Text(title=_t(u'xcvrLaserStatus'), readonly=True, group='Details')
    xcvrId2 = schema.Text(title=_t(u'xcvrId2'), readonly=True, group='Details')
    xcvrCustom2 = schema.Text(title=_t(u'xcvrCustom2'), readonly=True, group='Details')
    xcvrCustom3 = schema.Text(title=_t(u'xcvrCustom3'), readonly=True, group='Details')
    xcvrTraceLabel = schema.Text(title=_t(u'xcvrTraceLabel'), readonly=True, group='Details')
    xcvrExpectedTraceLabel = schema.Text(title=_t(u'xcvrExpectedTraceLabel'), readonly=True, group='Details')
    xcvrReceivedTraceLabel = schema.Text(title=_t(u'xcvrReceivedTraceLabel'), readonly=True, group='Details')
    xcvrSDBERTh = schema.Text(title=_t(u'xcvrSDBERTh'), readonly=True, group='Details')
    xcvrLoopbackType = schema.Text(title=_t(u'xcvrLoopbackType'), readonly=True, group='Details')


class IShelfInfo(IComponentInfo):
    '''
    Info adapter for BTI shelf components.
    '''
    shelfInvType = schema.Text(title=_t(u'shelfInvType'), readonly=True, group='Details')
    shelfInvShortName = schema.Text(title=_t(u'shelfInvShortName'), readonly=True, group='Details')
    shelfInvName = schema.Text(title=_t(u'shelfInvName'), readonly=True, group='Details')
    shelfInvChassisPEC = schema.Text(title=_t(u'shelfInvChassisPEC'), readonly=True, group='Details')
    shelfInvRev = schema.Text(title=_t(u'shelfInvRev'), readonly=True, group='Details')
    shelfInvUSI = schema.Text(title=_t(u'shelfInvUSI'), readonly=True, group='Details')


class IBSlotInfo(IComponentInfo):
    '''
    Info adapter for BTI Slot components.
    '''
    slotInvType = schema.Text(title=_t(u'slotInvType'), readonly=True, group='Details')
    slotInvShortName = schema.Text(title=_t(u'slotInvShortName'), readonly=True, group='Details')
    slotInvName = schema.Text(title=_t(u'slotInvName'), readonly=True, group='Details')
    slotInvChassisPEC = schema.Text(title=_t(u'slotInvChassisPEC'), readonly=True, group='Details')
    slotInvPackSerialNum = schema.Text(title=_t(u'slotInvPackSerialNum'), readonly=True, group='Details')
    slotInvRev = schema.Text(title=_t(u'slotInvRev'), readonly=True, group='Details')
    slotInvUSI = schema.Text(title=_t(u'slotInvUSI'), readonly=True, group='Details')
