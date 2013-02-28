from zope.component import adapts
from zope.interface import implements

from Products.ZenUtils.Utils import convToUnits

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.template import RRDDataSourceInfo

from ZenPacks.Rackspace.BTI7200.Interface import Interface
from ZenPacks.Rackspace.BTI7200.serialPort import serialPort
from ZenPacks.Rackspace.BTI7200.ethernetInterface import ethernetInterface
from ZenPacks.Rackspace.BTI7200.gigabitEthernetInterface import gigabitEthernetInterface
from ZenPacks.Rackspace.BTI7200.networkManagementInterface import networkManagementInterface
from ZenPacks.Rackspace.BTI7200.opticalAmplifier import opticalAmplifier
from ZenPacks.Rackspace.BTI7200.opticalSupervisoryChannel import opticalSupervisoryChannel
from ZenPacks.Rackspace.BTI7200.waveConversionPack import waveConversionPack
from ZenPacks.Rackspace.BTI7200.Shelf import Shelf 
from ZenPacks.Rackspace.BTI7200.BSlot import BSlot
from Products.Zuul.infos.component.ipinterface import IpInterfaceInfo

from ZenPacks.Rackspace.BTI7200.interfaces import *

#class btiDeviceInfo(ComponentInfo):
#    '''
#    Info adapter for BTI device.
#    '''
#    implements(IbtiDeviceInfo)
#    adapts(btiDevice)

class BtiComponentInfoMixin(object):
    meta_type = ProxyProperty('meta_type')


class BtiComponentInfo(ComponentInfo, BtiComponentInfoMixin):
    pass


class InterfaceInfo(IpInterfaceInfo, BtiComponentInfoMixin):
    '''
    Info adapter for common BTI interface components.
    '''
    implements(IInterfaceInfo)

    intShelfIdx = ProxyProperty('intShelfIdx')
    intSlotIdx = ProxyProperty('intSlotIdx')
    intPortIdx = ProxyProperty('intPortIdx')
    intPEC = ProxyProperty('intPEC')
    intOperStatQlfr = ProxyProperty('intOperStatQlfr')
    intVendorPN1 = ProxyProperty('intVendorPN1')
    intVendorPN2 = ProxyProperty('intVendorPN2')
    intVendorPN3 = ProxyProperty('intVendorPN3')
    intPhyPMMon = ProxyProperty('intPhyPMMon')
    intFPSD = ProxyProperty('intFPSD')
    intId1 = ProxyProperty('intId1')
    intFiberType = ProxyProperty('intFiberType')
    intMediaRate = ProxyProperty('intMediaRate')
    intRemoteId = ProxyProperty('intRemoteId')

    @property
    def monitored(self):
        return self._object.monitored() and not self._object.snmpIgnore()


class serialPortInfo(ComponentInfo):
    '''
    Info adapter for BTI serial port components.
    '''
    implements(IserialPortInfo)
    adapts(serialPort)

    serialPortIdx = ProxyProperty('serialPortIdx')
    serialBaudRate = ProxyProperty('serialBaudRate')
    serialDataBits = ProxyProperty('serialDataBits')
    serialParity = ProxyProperty('serialParity')
    serialStopBits = ProxyProperty('serialStopBits')

    @property
    def monitored(self):
        return self._object.monitored() and not self._object.snmpIgnore()


class ethernetInterfaceInfo(InterfaceInfo):
    '''
    Info adapter for BTI ethernet interface components.
    '''
    implements(IethernetInterfaceInfo)

    ethIntfPortTypeIdx = ProxyProperty('ethIntfPortTypeIdx')
    ethIntfLinkStatus = ProxyProperty('ethIntfLinkStatus')
    ethIntfLagId = ProxyProperty('ethIntfLagId')
    ethIntfLagPortPriority = ProxyProperty('ethIntfLagPortPriority')
    ethIntfBER = ProxyProperty('ethIntfBER')
    ethIntfLineMapping = ProxyProperty('ethIntfLineMapping')
    ethIntfErrorCorrection = ProxyProperty('ethIntfErrorCorrection')
    ethIntfLpbkOpCmd = ProxyProperty('ethIntfLpbkOpCmd')


class gigabitEthernetInterfaceInfo(InterfaceInfo):
    '''
    Info adapter for BTI gigabit interface components.
    '''
    implements(IgigabitEthernetInterfaceInfo)

    geGfpMode = ProxyProperty('geGfpMode')
    geFlowControl = ProxyProperty('geFlowControl')


class networkManagementInterfaceInfo(InterfaceInfo):
    '''
    Info adapter for BTI management interface components.
    '''
    implements(InetworkManagementInterfaceInfo)

    netMgmtIdx = ProxyProperty('netMgmtIdx')
    netMgmtType = ProxyProperty('netMgmtType')


class opticalAmplifierInfo(InterfaceInfo):
    '''
    Info adapter for BTI optical amplification components.
    '''
    implements(IopticalAmplifierInfo)

    oType = ProxyProperty('oType')
    oIdx = ProxyProperty('oIdx')
    oModeSetting = ProxyProperty('oModeSetting')
    oGainSetting = ProxyProperty('oGainSetting')
    oPwrSetting = ProxyProperty('oPwrSetting')
    oTiltCompSetting = ProxyProperty('oTiltCompSetting')
    oStatus = ProxyProperty('oStatus')
    oLaserStatus = ProxyProperty('oLaserStatus')
    oId2 = ProxyProperty('oId2')
    oNumChannels = ProxyProperty('oNumChannels')
    oCustom2 = ProxyProperty('oCustom2')
    oCustom3 = ProxyProperty('oCustom3')

class opticalSupervisoryChannelInfo(InterfaceInfo):
    '''
    Info adapter for BTI optical supervisory channel components.
    '''
    implements(IopticalSupervisoryChannelInfo)

    oscIdx = ProxyProperty('oscIdx')
    oscIPAddr = ProxyProperty('oscIPAddr')
    oscIPMask = ProxyProperty('oscIPMask')
    oscIPBcast = ProxyProperty('oscIPBcast')
    oscType = ProxyProperty('oscType')

class waveConversionPackInfo(InterfaceInfo):
    '''
    Info adapter for BTI wave conversion pack components.
    '''
    implements(IwaveConversionPackInfo)

    xcvrTypeIdx = ProxyProperty('xcvrTypeIdx')
    xcvrType = ProxyProperty('xcvrType')
    xcvrIdx = ProxyProperty('xcvrIdx')
    xcvrProtSwEvtType = ProxyProperty('xcvrProtSwEvtType')
    xcvrProtocol = ProxyProperty('xcvrProtocol')
    xcvrLaserStatus = ProxyProperty('xcvrLaserStatus')
    xcvrId2 = ProxyProperty('xcvrId2')
    xcvrCustom2 = ProxyProperty('xcvrCustom2')
    xcvrCustom3 = ProxyProperty('xcvrCustom3')
    xcvrTraceLabel = ProxyProperty('xcvrTraceLabel')
    xcvrExpectedTraceLabel = ProxyProperty('xcvrExpectedTraceLabel')
    xcvrReceivedTraceLabel = ProxyProperty('xcvrReceivedTraceLabel')
    xcvrSDBERTh = ProxyProperty('xcvrSDBERTh')
    xcvrLoopbackType = ProxyProperty('xcvrLoopbackType')

    @property
    def intWavelengthx10(self):
        return int(self._object.intWavelengthx10)/10


class ShelfInfo(ComponentInfo):
    '''
    Info adapter for BTI shelf components.
    '''
    implements(IShelfInfo)
    adapts(Shelf)

    shelfInvType = ProxyProperty('shelfInvType')
    shelfInvShortName = ProxyProperty('shelfInvShortName')
    shelfInvName = ProxyProperty('shelfInvName')
    shelfInvChassisPEC = ProxyProperty('shelfInvChassisPEC')
    shelfInvRev = ProxyProperty('shelfInvRev')
    shelfInvUSI = ProxyProperty('shelfInvUSI')

    @property
    def monitored(self):
        return self._object.monitored() and not self._object.snmpIgnore()


class BSlotInfo(ComponentInfo):
    '''
    Info adapter for BTI Slot components.
    '''
    implements(IBSlotInfo)
    adapts(BSlot)

    slotInvType = ProxyProperty('slotInvType')
    slotInvShortName = ProxyProperty('slotInvShortName')
    slotInvName = ProxyProperty('slotInvName')
    slotInvChassisPEC = ProxyProperty('slotInvChassisPEC')
    slotInvPackSerialNum = ProxyProperty('slotInvPackSerialNum')
    slotInvRev = ProxyProperty('slotInvRev')
    slotInvUSI = ProxyProperty('slotInvUSI')

    @property
    def monitored(self):
        return self._object.monitored() and not self._object.snmpIgnore()
