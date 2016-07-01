from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HAProxyBackends(SnmpPlugin):
    relname = 'haproxy_backends'
    modname = 'ZenPacks.community.HAProxy.HAProxyBackend'

    snmpGetTableMaps = (
        GetTableMap(
            'haBackendTable', '.1.3.6.1.4.1.29385.106.1.1', {
                '.0': 'haProxyBackendProxyName',
                '.17': 'haProxyBackendStatus',
                '.6': 'haProxyBackendSessionLimit',
                }
            ),
        )

    def process(self, device, results, log):
        haproxy_backends = results[1].get('haBackendTable', {})
        rm = self.relMap()
        for snmpindex, row in haproxy_backends.items():
            name = row.get('haProxyBackendProxyName')
            if not name:
                log.warn('Skipping empty zone')
                continue

            log.debug('found backend: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'backend_status': row.get('haProxyBackendStatus'),
                'backend_sessionlimit': row.get('haProxyBackendSessionLimit'),
                }))

        log.debug(rm)
        return rm
