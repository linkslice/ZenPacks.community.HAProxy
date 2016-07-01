from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class HAProxyFrontend(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'HAProxyHAProxyFrontends'
 
    frontend_status = None
    frontend_servicename = None
    frontend_sessionlimit = None

    _properties = ManagedEntity._properties + (
        {'id': 'frontend_status', 'type': 'string'},
        {'id': 'frontend_servicename', 'type': 'string'},
        {'id': 'frontend_sessionlimit', 'type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('haproxy_frontend', ToOne(ToManyCont,
            'ZenPacks.community.HAProxy.HAProxyDevice',
            'haproxy_frontends',
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
        return self.haproxy_frontend()

    def getRRDTemplateName(self):
        return 'HAProxyFrontends'
