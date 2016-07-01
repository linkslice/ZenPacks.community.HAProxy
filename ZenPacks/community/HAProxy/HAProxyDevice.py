from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.Device import Device



class HAProxyDevice(Device):
    _relations = Device._relations + (
        ('haproxy_frontends', ToManyCont(ToOne,
            'ZenPacks.community.HAProxy.HAProxyFrontend',
            'haproxy_frontend'
            )),
        ('haproxy_backends', ToManyCont(ToOne,
            'ZenPacks.community.HAProxy.HAProxyBackend',
            'haproxy_backend'
            )),
        ('haproxy_servers', ToManyCont(ToOne,
            'ZenPacks.community.HAProxy.HAProxyServer',
            'haproxy_server'
            )),

        )
