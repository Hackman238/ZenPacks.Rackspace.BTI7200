from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import *
from AccessControl import ClassSecurityInfo

class serialPort(ZenPackPersistence, OSComponent): 
    # serialPort Object class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'serialPort'

    serialPortIdx = None
    serialBaudRate = None
    serialDataBits = None
    serialParity = None
    serialStopBits = None

    _properties = OSComponent._properties + (
        {'id':'serialPortIdx', 'type':'int', 'mode':'w'},
        {'id':'serialBaudRate', 'type':'int', 'mode':'w'},
        {'id':'serialDataBits', 'type':'int', 'mode':'w'},
        {'id':'serialParity', 'type':'int', 'mode':'w'},
        {'id':'serialStopBits', 'type':'int', 'mode':'w'},
        )

    _relations = OSComponent._relations + (
        ("os", ToOne(ToManyCont, "Products.ZenModel.OperatingSystem", "serialPorts")),
        )

    security = ClassSecurityInfo()

    def deviceId(self):
        # The device id, for indexing purposes.
        d = self.device()
        if d:
           return d.getPrimaryId()
        else:
           return None

    def getId(self):
        return self.id

    def viewName(self):
        return self.id
    name = primarySortKey = viewName


    def managedDeviceLink(self):
        from Products.ZenModel.ZenModelRM import ZenModelRM
        d = self.getDmdRoot('Devices').findDevice(self.id)
        if d:
            return ZenModelRM.urlLink(d, 'link')
        return None

    def getRRDTemplateName(self):
        # Return the interface type as the target type name.
        return None

    def getRRDTemplates(self):
        # Return a list containing the appropriate RRDTemplate.
        return []
