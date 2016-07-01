from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HAProxyServers(SnmpPlugin):
    relname = 'haproxy_servers'
    modname = 'ZenPacks.community.HAProxy.HAProxyServer'

    snmpGetTableMaps = (
        GetTableMap(
            'haProxyServerTable', '1.3.6.1.4.1.29385.106.1.2', {
                '.0': 'haProxyServerProxyName',
                '.1': 'haProxyServerServiceName',
                '.17': 'haProxyServerStatus',
                }
            ),
        )

    def process(self, device, results, log):
        haproxy_servers = results[1].get('haProxyServerTable', {})
   
        #print results 

        zonelen = len(haproxy_servers.keys())
        rm = self.relMap()
        for snmpindex, row in haproxy_servers.items():
            name = row.get('haProxyServerServiceName')
            if not name:
                log.warn('Skipping empty zone')
                continue

            log.debug('found server: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(str(name)),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'server_status': row.get('haProxyServerStatus'),
                'server_proxyname': row.get('haProxyServerProxyName'),
                }))

        print rm
        return rm

