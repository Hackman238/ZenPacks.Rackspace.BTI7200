from zope.event import notify

from Globals import InitializeClass

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.Zuul.catalog.events import IndexingEvent
from Products.Zuul.interfaces import ICatalogTool

from ZenPacks.Rackspace.BTI7200.utils import (
    interfaces_by_name,
    interfaces_by_type,
    )


class btiDevice(Device):
    "A BTI device"

    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()

    def interface_ids(self):
        """Return IDs for all network interfaces on this device."""
        search = ICatalogTool(self).search

        ids = []
        for brain in search('Products.ZenModel.IpInterface.IpInterface'):
            ids.append(brain.id)

        return ids

InitializeClass(btiDevice)
