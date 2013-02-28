import Globals
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs
from struct import *
import sys
import string

class InterfaceMap(ZenPackPersistence, SnmpPlugin):

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    maptype = "InterfaceMap"
    compname = "os"
    relname = "interfaces"
    modname = "ZenPacks.Rackspace.BTI7200.Interface"

    snmpGetTableMaps = (
        GetTableMap('NetMgmtEntry','.1.3.6.1.4.1.18070.2.2.1.5.2.1',
                {'.1': 'netMgmtIdx',
                 '.5': 'netMgmtIPAddr',
                 '.6': 'netMgmtIPMask',
                 '.7': 'netMgmtIPBcast',
                 '.9': 'netMgmtType',
                 '.2': 'adminStatus',
                 '.3': 'operStatus',
                 '.4': 'intOperStatQlfr',
                 '.8': 'description',
                 '.11': 'speed',
                 '.12': 'duplex',
                 '.13': 'intMediaRate',
                 '.14': 'mtu',
                 '.15': 'macaddress'}
        ),

        GetTableMap('OscEntry','.1.3.6.1.4.1.18070.2.2.1.5.1.1',
                {'.1': 'oscIdx',
                 '.15': 'oscIPAddr',
                 '.16': 'oscIPMask',
                 '.17': 'oscIPBcast',
                 '.8': 'oscType',
                 '.4': 'adminStatus',
                 '.5': 'operStatus',
                 '.6': 'intOperStatQlfr',
                 '.7': 'description',
                 '.10': 'speed',
                 '.11': 'duplex',
                 '.12': 'intMediaRate',
                 '.13': 'mtu',
                 '.14': 'macaddress'}
        ),

        GetTableMap('EthIntfEntry','.1.3.6.1.4.1.18070.2.2.1.4.14.1',
                {'.3': 'ethIntfPortTypeIdx',
                 '.31': 'ethIntfLinkStatus',
                 '.32': 'ethIntfLagId',
                 '.33': 'ethIntfLagPortPriority',
                 '.37': 'ethIntfBER',
                 '.40': 'ethIntfLineMapping',
                 '.41': 'ethIntfErrorCorrection',
                 '.42': 'ethIntfLpbkOpCmd',
                 '.1': 'intShelfIdx',
                 '.2': 'intSlotIdx',
                 '.3': 'intPortIdx',
                 '.11': 'intPEC',
                 '.12': 'adminStatus',
                 '.13': 'operStatus',
                 '.14': 'intOperStatQlfr',
                 '.17': 'intWavelengthx10',
                 '.18': 'intVendorPN1',
                 '.19': 'intVendorPN2',
                 '.20': 'intVendorPN3',
                 '.21': 'intPhyPMMon',
                 '.22': 'intFPSD',
                 '.24': 'intId1',
                 '.25': 'intFiberType',
                 '.26': 'description',
                 '.27': 'speed',
                 '.28': 'duplex',
                 '.29': 'intMediaRate',
                 '.30': 'mtu',
                 '.39': 'macaddress',
                 '.43': 'intRemoteId'}
        ),

        GetTableMap('GeEntry','.1.3.6.1.4.1.18070.2.2.1.4.9.1',
                {'.31': 'geGfpMode',
                 '.32': 'geFlowControl',
                 '.1': 'intShelfIdx',
                 '.2': 'intSlotIdx',
                 '.3': 'intPortIdx',
                 '.10': 'intPEC',
                 '.11': 'adminStatus',
                 '.12': 'operStatus',
                 '.13': 'intOperStatQlfr',
                 '.16': 'intWavelengthx10',
                 '.17': 'intVendorPN1',
                 '.18': 'intVendorPN2',
                 '.19': 'intVendorPN3',
                 '.20': 'intPhyPMMon',
                 '.21': 'intFPSD',
                 '.23': 'intId1',
                 '.24': 'intFiberType',
                 '.25': 'description',
                 '.26': 'speed',
                 '.27': 'duplex',
                 '.28': 'intMediaRate',
                 '.29': 'mtu',
                 '.30': 'macaddress',
                 '.33': 'intRemoteId'}
        ),

        GetTableMap('OaEntry','.1.3.6.1.4.1.18070.2.2.1.4.1.1',
                {'.1': 'oType',
                 '.4': 'oIdx',
                 '.46': 'oModeSetting',
                 '.47': 'oGainSetting',
                 '.48': 'oPwrSetting',
                 '.49': 'oTiltCompSetting',
                 '.50': 'oStatus',
                 '.51': 'oLaserStatus',
                 '.53': 'oId2',
                 '.54': 'oFiberType',
                 '.56': 'oNumChannels',
                 '.58': 'oCustom2',
                 '.59': 'oCustom3',
                 '.2': 'intShelfIdx',
                 '.3': 'intSlotIdx',
                 '.41': 'adminStatus',
                 '.42': 'operStatus',
                 '.43': 'intOperStatQlfr',
                 '.60': 'intWavelengthx10',
                 '.52': 'intId1',
                 '.54': 'intFiberType',
                 '.57': 'description',
                 '.61': 'intRemoteId'}
        ),

        GetTableMap('XcvrEntry','.1.3.6.1.4.1.18070.2.2.1.4.2.1',
                {'.1': 'xcvrTypeIdx',
                 '.2': 'intShelfIdx',
                 '.3': 'intSlotIdx',
                 '.4': 'xcvrIdx',
                 '.11': 'xcvrProtSwEvtType',
                 '.18': 'xcvrProtocol',
                 '.25': 'xcvrLaserStatus',
                 '.27': 'xcvrId2',
                 '.31': 'xcvrCustom2',
                 '.32': 'xcvrCustom3',
                 '.33': 'xcvrTraceLabel',
                 '.34': 'xcvrExpectedTraceLabel',
                 '.35': 'xcvrReceivedTraceLabel',
                 '.36': 'xcvrSDBERTh',
                 '.37': 'xcvrLoopbackType',
                 '.3': 'intSlotIdx',
                 '.12': 'intPEC',
                 '.13': 'adminStatus',
                 '.14': 'operStatus',
                 '.15': 'intOperStatQlfr',
                 '.19': 'intWavelengthx10',
                 '.20': 'intVendorPN1',
                 '.21': 'intVendorPN2',
                 '.22': 'intVendorPN3',
                 '.23': 'intPhyPMMon',
                 '.24': 'intFPSD',
                 '.26': 'intId1',
                 '.28': 'intFiberType',
                 '.30': 'description',
                 '.38': 'intRemoteId'}
        ),

    )


    def process(self, device, results, log):
        """
        From SNMP info gathered from the device, convert them
        to BTI Interface and Optics objects.
        """
        getdata, tabledata = results
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        log.debug( '%s tabledata = %s' % (device.id,tabledata) )
        rm = self.relMap()

        table = tabledata.get('NetMgmtEntry')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.networkManagementInterface'
            id = self.prepId('netMgmt' + str(snmpindex))
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.interfaceName = id
            om.macaddress = self.asmac(om.macaddress)
            om.snmpindex = snmpindex
            om.ifindex = snmpindex
            ip = om.netMgmtIPAddr
            nm = om.netMgmtIPMask
            ipnm = ip + "/" + str(self.maskToBits(nm))
            om.setIpAddresses = [ipnm]
            om.type = 'networkManagementInterface'
            rm.append(om)
        table = tabledata.get('OscEntry')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.opticalSupervisoryChannel'
            id = self.prepId('osc' + str(snmpindex))
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.interfaceName = id
            om.macaddress = self.asmac(om.macaddress)
            om.snmpindex = snmpindex
            om.ifindex = snmpindex
            ip = om.oscIPAddr
            nm = om.oscIPMask
            ipnm = ip + "/" + str(self.maskToBits(nm))
            om.setIpAddresses = [ipnm]
            om.type = 'opticalSupervisoryChannel'
            rm.append(om)
        table = tabledata.get('EthIntfEntry')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.ethernetInterface'
            id = self.prepId('eth' + str(snmpindex))
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.interfaceName = id
            om.macaddress = self.asmac(om.macaddress)
            om.snmpindex = snmpindex
            om.ifindex = snmpindex
            om.type = 'ethernetInterface'
            rm.append(om)
        table = tabledata.get('GeEntry')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.gigabitEthernetInterface'
            id = self.prepId('ge' + str(snmpindex))
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.interfaceName = id
            om.macaddress = self.asmac(om.macaddress)
            om.snmpindex = snmpindex
            om.ifindex = snmpindex
            om.type = 'gigabitEthernetInterface'
            rm.append(om)
        table = tabledata.get('OaEntry')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.opticalAmplifier'
            id = self.prepId('oa' + str(snmpindex))
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.interfaceName = id
            om.snmpindex = snmpindex
            om.ifindex = snmpindex
            om.type = 'opticalAmplifier'
            rm.append(om)
        table = tabledata.get('XcvrEntry')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.waveConversionPack'
            id = self.prepId('xcvr' + str(snmpindex))
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.interfaceName = id
            om.snmpindex = snmpindex + '.1'
            om.ifindex = snmpindex + '.1'
            om.type = 'waveConversionPack'
            rm.append(om)
        return [rm]
