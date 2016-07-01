from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class HAProxyServer(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'HAProxyHAProxyServers'
 
    server_status = None
    server_proxyname = None

    _properties = ManagedEntity._properties + (
        {'id': 'server_status', 'type': 'string'},
        {'id': 'server_proxyname', 'type': 'string'},
        {'id': 'server_sessionlimit', 'type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('haproxy_server', ToOne(ToManyCont,
            'ZenPacks.community.HAProxy.HAProxyDevice',
            'haproxy_servers',
            )),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.haproxy_server()

    def getRRDTemplateName(self):
        return 'HAProxyServers'
