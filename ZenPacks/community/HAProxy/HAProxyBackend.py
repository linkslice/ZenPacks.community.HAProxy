from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class HAProxyBackend(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'HAProxyHAProxyBackends'
   
    backend_status = None
    backend_sessionlimit = None

    _properties = ManagedEntity._properties + (
        {'id': 'backend_status','type': 'string'},
        {'id': 'backend_sessionlimit','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('haproxy_backend', ToOne(ToManyCont,
            'ZenPacks.community.HAProxy.HAProxyDevice',
            'haproxy_backends',
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
        return self.haproxy_backend()

    def getRRDTemplateName(self):
        return 'HAProxyBackends'
