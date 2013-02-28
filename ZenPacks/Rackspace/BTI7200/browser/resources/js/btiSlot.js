(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.SlotPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'Slot',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'slotInvShortName'},
                {name: 'slotInvType'},
                {name: 'slotInvChassisPEC'},
                {name: 'slotInvPackSerialNum'},
                {name: 'slotInvRev'},
                {name: 'slotInvUSI'},
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
                id: 'slotInvShortName',
                dataIndex: 'slotInvShortName',
                header: _t('Short Name'),
                sortable: true,
            },{
                id: 'slotInvType',
                dataIndex: 'slotInvType',
                header: _t('Type'),
                sortable: true,
            },{
                id: 'slotInvChassisPEC',
                dataIndex: 'slotInvChassisPEC',
                header: _t('PEC'),
                sortable: true,
            },{
                id: 'slotInvPackSerialNum',
                dataIndex: 'slotInvPackSerialNum',
                header: _t('Serial'),
                sortable: true,
            },{
                id: 'slotInvRev',
                dataIndex: 'slotInvRev',
                header: _t('Rev'),
                sortable: true,
            },{
                id: 'slotInvUSI',
                dataIndex: 'slotInvUSI',
                header: _t('USI'),
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
        ZC.SlotPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('SlotPanel', ZC.SlotPanel);

ZC.registerName('Slot', _t('Slot'), _t('Slots'));
})();
