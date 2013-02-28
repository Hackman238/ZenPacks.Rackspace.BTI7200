import Globals
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs
from struct import *
import sys
import string

class ShelfMap(ZenPackPersistence, SnmpPlugin):

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    compname = "os"
    relname = "shelves"
    modname = "ZenPacks.Rackspace.BTI7200.Shelf"

    snmpGetTableMaps = (

        GetTableMap('shelfInv','.1.3.6.1.4.1.18070.2.2.1.2.1.1',
                {'.10':'shelfInvType',
                 '.11':'shelfInvShortName',
                 '.12':'shelfInvName',
                 '.13':'shelfInvChassisPEC',
                 '.16':'shelfInvRev',
                 '.18':'shelfInvUSI'},
        ),

    )


    def process(self, device, results, log):
        """
        From SNMP info gathered from the device, convert them
        to shelf objects.
        """
        getdata, tabledata = results
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        log.debug( '%s tabledata = %s' % (device.id,tabledata) )
        rm = self.relMap()

        table = tabledata.get('shelfInv')
        count = -1
        for snmpindex, entry in table.items():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            om.modname = 'ZenPacks.Rackspace.BTI7200.Shelf'
            id = self.prepId(om.shelfInvName)
            id = id.replace('.','')
            om.id = id
            om.title = id
            om.snmpindex = snmpindex
            om.type = 'shelf'
            rm.append(om)
        return [rm]
