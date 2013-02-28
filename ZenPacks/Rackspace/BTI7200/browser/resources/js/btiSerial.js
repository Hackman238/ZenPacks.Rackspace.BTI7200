(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.serialPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'serialPort',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'serialBaudRate'},
                {name: 'serialDataBits'},
                {name: 'serialParity'},
                {name: 'serialStopBits'},
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
                width: 120,
                sortable: true,
            },{
                id: 'serialBaudRate',
                dataIndex: 'serialBaudRate',
                header: _t('Baud Rate'),
                sortable: true,
            },{
                id: 'serialDataBits',
                dataIndex: 'serialDataBits',
                header: _t('Data Bits'),
                sortable: true,
            },{
                id: 'serialParity',
                dataIndex: 'serialParity',
                header: _t('Parity'),
                sortable: true,
            },{
                id: 'serialStopBits',
                dataIndex: 'serialStopBits',
                header: _t('Stop Bits'),
                sortable: true,
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
        ZC.serialPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('serialPortPanel', ZC.serialPortPanel);

ZC.registerName('serialPort', _t('Serial Port'), _t('Serial Ports'));
})();
