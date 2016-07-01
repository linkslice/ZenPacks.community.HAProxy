from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HAProxyFrontends(SnmpPlugin):
    relname = 'haproxy_frontends'
    modname = 'ZenPacks.community.HAProxy.HAProxyFrontend'

    snmpGetTableMaps = (
        GetTableMap(
            'haProxyFrontendTable', '1.3.6.1.4.1.29385.106.1.0', {
                '.0': 'haProxyFrontendProxyName',
                '.1': 'haProxyFrontendServiceName',
                '.17': 'haProxyFrontendStatus',
                '.6': 'haProxyFrontendSessionLimit',
                }
            ),
        )

    def process(self, device, results, log):
        haproxy_frontends = results[1].get('haProxyFrontendTable', {})
   
        #print results 

        zonelen = len(haproxy_frontends.keys())
        rm = self.relMap()
        for snmpindex, row in haproxy_frontends.items():
            name = row.get('haProxyFrontendProxyName')
            if not name:
                log.warn('Skipping empty zone')
                continue

            log.debug('found frontend: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(str(name)),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'frontend_status': row.get('haProxyFrontendStatus'),
                'frontend_servicename': row.get('haProxyFrontendServiceName'),
                'frontend_sessionlimit': row.get('haProxyFrontendSessionLimit'),
                }))

        print rm
        return rm

