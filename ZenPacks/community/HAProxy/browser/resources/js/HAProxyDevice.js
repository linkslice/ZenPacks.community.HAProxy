(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'HAProxyHAProxyFrontends',
    _t('HAProxy Frontend'),
    _t('HAProxy Frontends'));

ZC.registerName(
    'HAProxyHAProxyBackends',
    _t('HAProxy Backend'),
    _t('HAProxy Backends'));

ZC.registerName(
    'HAProxyHAProxyServers',
    _t('HAProxy Server'),
    _t('HAProxy Servers'));

ZC.HAProxyHAProxyBackendsPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HAProxyHAProxyBackends',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'backend_status'},
                {name: 'backend_sessionlimit'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'backend_status',
                dataIndex: 'backend_status',
                header: _t('Status'),
                sortable: true,
                width: 120
            },{
                id: 'backend_sessionlimit',
                dataIndex: 'backend_sessionlimit',
                header: _t('Session Limit'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.HAProxyHAProxyBackendsPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.HAProxyHAProxyFrontendsPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HAProxyHAProxyFrontends',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'frontend_status'},
                {name: 'frontend_servicename'},
                {name: 'frontend_sessionlimit'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'frontend_status',
                dataIndex: 'frontend_status',
                header: _t('Status'),
                sortable: true,
                width: 120
            },{
                id: 'frontend_servicename',
                dataIndex: 'frontend_servicename',
                header: _t('Service'),
                sortable: true,
                width: 120
            },{
                id: 'frontend_sessionlimit',
                dataIndex: 'frontend_sessionlimit',
                header: _t('Session Limit'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.HAProxyHAProxyFrontendsPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.HAProxyHAProxyServersPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HAProxyHAProxyServers',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'server_status'},
                {name: 'server_proxyname'},
                {name: 'server_sessionlimit'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'server_status',
                dataIndex: 'server_status',
                header: _t('Status'),
                sortable: true,
                width: 120
            },{
                id: 'server_servicename',
                dataIndex: 'server_proxyname',
                header: _t('Frontend'),
                sortable: true,
                width: 120
            },{
                id: 'server_sessionlimit',
                dataIndex: 'server_sessionlimit',
                header: _t('Session Limit'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.HAProxyHAProxyServersPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('HAProxyHAProxyBackendsPanel', ZC.HAProxyHAProxyBackendsPanel);
Ext.reg('HAProxyHAProxyFrontendsPanel', ZC.HAProxyHAProxyFrontendsPanel);
Ext.reg('HAProxyHAProxyServersPanel', ZC.HAProxyHAProxyServersPanel);

})();
