import Globals
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap, MultiArgs
from struct import *
import sys
import string

class DeviceMap(ZenPackPersistence, SnmpPlugin):

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    maptype = "DeviceMap"
    compname = "os"
    relname = ""
    modname = "ZenPacks.Rackspace.BTI7200.bitDevice"

    columns = {
             '.1.3.6.1.2.1.1.1.0' : 'snmpDescr',
             '.1.3.6.1.2.1.1.2.0' : 'snmpOid',
             '.1.3.6.1.2.1.1.4.0' : 'snmpContact',
             '.1.3.6.1.2.1.1.5.0' : 'snmpSysName',
             '.1.3.6.1.2.1.1.6.0' : 'snmpLocation',
             }
    snmpGetMap = GetMap(columns)

    def process(self, device, results, log):
        """
        Collect snmp information from this device
        """
        log.info('Modeler processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        if not self.checkColumns(getdata, self.columns, log):
            return
        om = self.objectMap(getdata)

        return om
