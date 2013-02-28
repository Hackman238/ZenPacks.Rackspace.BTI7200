(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.ShelfPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'Shelf',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'id'},
                {name: 'meta_type'},
                {name: 'severity'},
                {name: 'shelfInvShortName'},
                {name: 'shelfInvType'},
                {name: 'shelfInvChassisPEC'},
                {name: 'shelfInvRev'},
                {name: 'shelfInvUSI'},
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
                id: 'shelfInvShortName',
                dataIndex: 'shelfInvShortName',
                header: _t('Short Name'),
                sortable: true,
            },{
                id: 'shelfInvType',
                dataIndex: 'shelfInvType',
                header: _t('Type'),
                sortable: true,
            },{
                id: 'shelfInvChassisPEC',
                dataIndex: 'shelfInvChassisPEC',
                header: _t('PEC'),
                sortable: true,
            },{
                id: 'shelfInvRev',
                dataIndex: 'shelfInvRev',
                header: _t('Rev'),
                sortable: true,
            },{
                id: 'shelfInvUSI',
                dataIndex: 'shelfInvUSI',
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
        ZC.ShelfPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('ShelfPanel', ZC.ShelfPanel);

ZC.registerName('Shelf', _t('Shelf'), _t('Shelfs'));
})();
