(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.btiInterfacePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'btiInterface',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'description'},
                {name: 'macaddress'},
                {name: 'description'},
                {name: 'adminStatus'},
                {name: 'operStatus'},
                {name: 'intOperStatQlfr'},
                {name: 'speed'},
                {name: 'duplex'},
                {name: 'intMediaRate'},
                {name: 'mtu'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'usesMonitorAttribute'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
               id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 105,
                sortable: true
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true
            },{
                id: 'speed',
                dataIndex: 'speed',
                header: _t('Speed'),
                width: 70,
                sortable: true
            },{
                id: 'duplex',
                dataIndex: 'duplex',
                header: _t('Duplex'),
                width: 70,
                sortable: true
            },{
                id: 'intMediaRate',
                dataIndex: 'intMediaRate',
                header: _t('Media Rate'),
                width: 75,
                sortable: true
            },{
                id: 'mtu',
                dataIndex: 'mtu',
                header: _t('MTU'),
                width: 50,
                sortable: true
            },{
                id: 'adminStatus',
                dataIndex: 'adminStatus',
                header: _t('Admin Status'),
                width: 90,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'operStatus',
                dataIndex: 'operStatus',
                header: _t('Op Status'),
                width: 85,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'intOperStatQlfr',
                dataIndex: 'intOperStatQlfr',
                header: _t('Op Qlfr'),
                width: 85,
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 70,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]
        });
        ZC.btiInterfacePanel.superclass.constructor.call(this, config);
    }
});

ZC.ethernetInterfacePanel = Ext.extend(ZC.btiInterfacePanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'ethernetInterface',
        });
        ZC.ethernetInterfacePanel.superclass.constructor.call(
            this, config);
    }
});

ZC.gigabitEthernetInterfacePanel = Ext.extend(ZC.btiInterfacePanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'gigabitEthernetInterface',
        });
        ZC.gigabitEthernetInterfacePanel.superclass.constructor.call(
            this, config);
    }
});

ZC.networkManagementInterfacePanel = Ext.extend(ZC.btiInterfacePanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'networkManagementInterface',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'macaddress'},
                {name: 'description'},
                {name: 'ipAddressObjs'},
                {name: 'network'},  // required for ipAddresses field
                {name: 'netmask'},  // required for ipAddresses field
                {name: 'netMgmtType'},
                {name: 'adminStatus'},
                {name: 'operStatus'},
                {name: 'intOperStatQlfr'},
                {name: 'speed'},
                {name: 'duplex'},
                {name: 'intMediaRate'},
                {name: 'mtu'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'usesMonitorAttribute'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
               id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 105,
                sortable: true
            },{
                id: 'ipAddresses',
                dataIndex: 'ipAddressObjs',
                header: _t('IP Addresses'),
                renderer: function(ipaddresses) {
                    var returnString = '';
                    Ext.each(ipaddresses, function(ipaddress, index) {
                        if (index > 0) returnString += ', ';
                        if (ipaddress && Ext.isObject(ipaddress) && ipaddress.netmask) {
                            var name = ipaddress.name + '/' + ipaddress.netmask;
                            returnString += Zenoss.render.link(ipaddress.uid, undefined, name);
                        }
                        else if (Ext.isString(ipaddress)) {
                            returnString += ipaddress;
                        }
                    });
                    return returnString;
                }
            },{
                id: 'macaddress',
                dataIndex: 'macaddress',
                header: _t('MAC'),
                width: 105,
                sortable: true
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true
            },{
                id: 'netMgmtType',
                dataIndex: 'netMgmtType',
                header: _t('Type'),
                width: 50,
                sortable: true
            },{
                id: 'speed',
                dataIndex: 'speed',
                header: _t('Speed'),
                width: 70,
                sortable: true
            },{
                id: 'duplex',
                dataIndex: 'duplex',
                header: _t('Duplex'),
                width: 70,
                sortable: true
            },{
                id: 'intMediaRate',
                dataIndex: 'intMediaRate',
                header: _t('Media Rate'),
                width: 75,
                sortable: true
            },{
                id: 'mtu',
                dataIndex: 'mtu',
                header: _t('MTU'),
                width: 50,
                sortable: true
            },{
                id: 'adminStatus',
                dataIndex: 'adminStatus',
                header: _t('Admin Status'),
                width: 90,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'operStatus',
                dataIndex: 'operStatus',
                header: _t('Op Status'),
                width: 85,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'intOperStatQlfr',
                dataIndex: 'intOperStatQlfr',
                header: _t('Op Qlfr'),
                width: 85,
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 70,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]

        });
        ZC.networkManagementInterfacePanel.superclass.constructor.call(
            this, config);
    }
});

ZC.opticalSupervisoryChannelPanel = Ext.extend(ZC.btiInterfacePanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'opticalSupervisoryChannel',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'macaddress'},
                {name: 'description'},
                {name: 'ipAddressObjs'},
                {name: 'network'},  // required for ipAddresses field
                {name: 'netmask'},  // required for ipAddresses field
                {name: 'oscType'},
                {name: 'adminStatus'},
                {name: 'operStatus'},
                {name: 'intOperStatQlfr'},
                {name: 'speed'},
                {name: 'duplex'},
                {name: 'intMediaRate'},
                {name: 'mtu'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'usesMonitorAttribute'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
               id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 105,
                sortable: true
            },{
                id: 'ipAddresses',
                dataIndex: 'ipAddressObjs',
                header: _t('IP Addresses'),
                renderer: function(ipaddresses) {
                    var returnString = '';
                    Ext.each(ipaddresses, function(ipaddress, index) {
                        if (index > 0) returnString += ', ';
                        if (ipaddress && Ext.isObject(ipaddress) && ipaddress.netmask) {
                            var name = ipaddress.name + '/' + ipaddress.netmask;
                            returnString += Zenoss.render.link(ipaddress.uid, undefined, name);
                        }
                        else if (Ext.isString(ipaddress)) {
                            returnString += ipaddress;
                        }
                    });
                    return returnString;
                }
            },{
                id: 'macaddress',
                dataIndex: 'macaddress',
                header: _t('MAC'),
                width: 105,
                sortable: true
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true
            },{
                id: 'oscType',
                dataIndex: 'Type',
                header: _t('Type'),
                width: 50,
                sortable: true
            },{
                id: 'speed',
                dataIndex: 'speed',
                header: _t('Speed'),
                width: 70,
                sortable: true
            },{
                id: 'duplex',
                dataIndex: 'duplex',
                header: _t('Duplex'),
                width: 70,
            },{
                id: 'intMediaRate',
                dataIndex: 'intMediaRate',
                header: _t('Media Rate'),
                width: 75,
                sortable: true
            },{
                id: 'mtu',
                dataIndex: 'mtu',
                header: _t('MTU'),
                width: 50,
                sortable: true
            },{
                id: 'adminStatus',
                dataIndex: 'adminStatus',
                header: _t('Admin Status'),
                width: 90,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'operStatus',
                dataIndex: 'operStatus',
                header: _t('Op Status'),
                width: 85,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'intOperStatQlfr',
                dataIndex: 'intOperStatQlfr',
                header: _t('Op Qlfr'),
                width: 85,
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 70,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]

        });
        ZC.opticalSupervisoryChannelPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.waveConversionPackPanel = Ext.extend(ZC.btiInterfacePanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'waveConversionPack',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'description'},
                {name: 'adminStatus'},
                {name: 'operStatus'},
                {name: 'intOperStatQlfr'},
                {name: 'xcvrTypeIdx'},
                {name: 'xcvrType'},
                {name: 'xcvrProtSwEvtType'},
                {name: 'xcvrProtocol'},
                {name: 'xcvrId2'},
                {name: 'xcvrCustom2'},
                {name: 'xcvrCustom3'},
                {name: 'xcvrSDBERTh'},
                {name: 'xcvrLoopbackType'},
                {name: 'xcvrLaserStatus'},
                {name: 'intWavelengthx10'},
                {name: 'intPEC'},
                {name: 'intVendorPN1'},
                {name: 'intVendorPN2'},
                {name: 'intVendorPN3'},
                {name: 'intPhyPMMon'},
                {name: 'intFPSD'},
                {name: 'intId1'},
                {name: 'intFiberType'},
                {name: 'intRemoteId'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'usesMonitorAttribute'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 115,
                sortable: true
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Custom'),
                width: 100,
                sortable: true
            },{
                id: 'intWavelengthx10',
                dataIndex: 'intWavelengthx10',
                header: _t('Wave Length'),
                width: 90,
                sortable: true
            },{
                id: 'intPEC',
                dataIndex: 'intPEC',
                header: _t('PEC'),
                width: 90,
                sortable: true
            },{
                id: 'xcvrType',
                dataIndex: 'xcvrType',
                header: _t('Type'),
                width: 50,
                sortable: true
            },{
                id: 'xcvrProtocol',
                dataIndex: 'xcvrProtocol',
                header: _t('Proto'),
                width: 50,
                sortable: true
            },{
                id: 'intPhyPMMon',
                dataIndex: 'intPhyPMMon',
                header: _t('PhyPMMon'),
                width: 60,
                sortable: true
            },{
                id: 'intFPSD',
                dataIndex: 'intFPSD',
                header: _t('FPSD'),
                width: 50,
                sortable: true
            },{
                id: 'intFiberType',
                dataIndex: 'intFiberType',
                header: _t('Fiber Type'),
                width: 60,
                sortable: true
            },{
                id: 'xcvrSDBERTh',
                dataIndex: 'xcvrSDBERTh',
                header: _t('SDBER'),
                width: 60,
                sortable: true
            },{
                id: 'xcvrLoopbackType',
                dataIndex: 'xcvrLoopbackType',
                header: _t('Loop Type'),
                width: 60,
                sortable: true
            },{
                id: 'adminStatus',
                dataIndex: 'adminStatus',
                header: _t('Admin Status'),
                width: 90,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'operStatus',
                dataIndex: 'operStatus',
                header: _t('Op Status'),
                width: 85,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'intOperStatQlfr',
                dataIndex: 'intOperStatQlfr',
                header: _t('Op Qlfr'),
                width: 85,
                sortable: true
            },{
                id: 'xcvrLaserStatus',
                dataIndex: 'xcvrLaserStatus',
                header: _t('Laser Status'),
                width: 85,
                sortable: true,
               renderer: Zenoss.render.checkbox
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 70,
                sortable: true,
                renderer: Zenoss.render.checkbox
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons
            }]

        });
        ZC.waveConversionPackPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('waveConversionPackPanel', ZC.waveConversionPackPanel);
Ext.reg('btiInterfacePanel', ZC.btiInterfacePanel);
Ext.reg('ethernetInterfacePanel', ZC.ethernetInterfacePanel);
Ext.reg('gigabitEthernetInterfacePanel', ZC.gigabitEthernetInterfacePanel);
Ext.reg('networkManagementInterfacePanel', ZC.networkManagementInterfacePanel);
Ext.reg('opticalSupervisoryChannelPanel', ZC.opticalSupervisoryChannelPanel);

ZC.registerName('waveConversionPack', _t('Wave Conversion Pack'), _t('Wave Conversion Packs'));
ZC.registerName('btiInterface', _t('Network Interface'), _t('Network Interfaces'));
ZC.registerName('ethernetInterface', _t('Ethernet Interfaces'), _t('Ethernet Interfaces'));
ZC.registerName('gigabitEthernetInterface', _t('Ethernet Interface'), _t('Ethernet Interfaces'));
ZC.registerName('networkManagementInterface', _t('Management Interface'), _t('Management Interfaces'));
ZC.registerName('opticalSupervisoryChannel', _t('Optical Supervisory Channel'), _t('Optical Supervisory Channels'));

})();
