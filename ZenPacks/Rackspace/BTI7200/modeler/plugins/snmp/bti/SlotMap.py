import Globals
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs
from struct import *
import sys
import string

class SlotMap(ZenPackPersistence, SnmpPlugin):

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    compname = "os"
    relname = "slots"
    modname = "ZenPacks.Rackspace.BTI7200.BSlot"

    snmpGetTableMaps = (

        GetTableMap('slotInv','.1.3.6.1.4.1.18070.2.2.1.2.2.1',
                {'.10':'slotInvType',
                 '.5':'slotInvShortName',
                 '.6':'slotInvName',
                 '.7':'slotInvChassisPEC',
                 '.9':'slotInvPackSerialNum',
                 '.10':'slotInvRev',
                 '.17':'slotInvUSI'},
        ),

    )


    def process(self, device, results, log):
        """
        From SNMP info gathered from the device, convert them
        to slot objects.
        """
        getdata, tabledata = results
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        log.debug( '%s tabledata = %s' % (device.id,tabledata) )
        rm = self.relMap()

        table = tabledata.get('slotInv')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.BSlot'
            id = self.prepId(om.slotInvName)
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.snmpindex = snmpindex
            om.type = 'slot'
            rm.append(om)
        return [rm]
