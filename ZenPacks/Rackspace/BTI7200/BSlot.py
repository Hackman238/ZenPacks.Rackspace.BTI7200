from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import *
from AccessControl import ClassSecurityInfo

class BSlot(ZenPackPersistence, OSComponent):
    # Slot Object Class

    ZENPACKID = 'ZenPacks.Rackspace.BTI7200'

    portal_type = meta_type = 'Slot'

    monitor = True

    slotInvType = None
    slotInvShortName = None
    slotInvName = None
    slotInvChassisPEC = None
    slotInvPackSerialNum = None
    slotInvRev = None
    slotInvUSI = None

    _properties = OSComponent._properties + (
        {'id':'slotInvType', 'type':'int', 'mode':'w'},
        {'id':'slotInvShortName', 'type':'string', 'mode':'w'},
        {'id':'slotInvName', 'type':'string', 'mode':'w'},
        {'id':'slotInvChassisPEC', 'type':'string', 'mode':'w'},
        {'id':'slotInvPackSerialNum', 'type':'string', 'mode':'w'},
        {'id':'slotInvRev', 'type':'int', 'mode':'w'},
        {'id':'slotInvUSI', 'type':'string', 'mode':'w'},
        )

    _relations = OSComponent._relations + (
        ("os", ToOne(ToManyCont, "Products.ZenModel.OperatingSystem", "slots")),
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
