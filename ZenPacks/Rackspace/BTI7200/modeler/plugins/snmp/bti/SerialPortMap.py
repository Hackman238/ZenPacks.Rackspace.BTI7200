import Globals
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenUtils.Utils import convToUnits, prepId
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs
from struct import *
import sys
import string

class SerialPortMap(ZenPackPersistence, SnmpPlugin):

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    maptype = 'SerialPortMap'
    compname = 'os'
    relname = 'serialPorts'
    modname = 'ZenPacks.Rackspace.BTI7200.serialPort'

    snmpGetTableMaps = (
        GetTableMap('serialEntry', '1.3.6.1.4.1.18070.2.2.1.5.3.1',
                {'.1':'serialPortIdx',
                 '.2':'serialBaudRate',
                 '.3':'serialDataBits',
                 '.4':'serialParity',
                 '.5':'serialStopBits'}
        ),
    )


    def process(self, device, results, log):
        """
        From SNMP info gathered from the device, convert them
        to serial objects.
        """
        log.info('Modeler %s processing data for device %s', self.name(), device.id)
        getdata, tabledata = results

        table = tabledata.get('serialEntry')
        rm = self.relMap()
        count = -1 
        for entry in table.values():
            count = count + 1
            keys = table.keys()
            log.debug('Entry: %s', entry)
            om = self.objectMap(entry)
            id = self.prepId('s' +  str(keys[count]))
            om.id = id.replace('.','')
            rm.append(om)
        return [rm]
