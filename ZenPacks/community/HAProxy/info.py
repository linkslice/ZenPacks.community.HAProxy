from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.HAProxy.interfaces import (
    IHAProxyBackendsInfo,
    IHAProxyFrontendsInfo,
    IHAProxyServersInfo,
    )

class HAProxyBackendsInfo(ComponentInfo):
    implements(IHAProxyBackendsInfo)
    backend_status = ProxyProperty('backend_status')
    backend_sessionlimit = ProxyProperty('backend_sessionlimit')
    
class HAProxyFrontendsInfo(ComponentInfo):
    implements(IHAProxyFrontendsInfo)
    frontend_status = ProxyProperty('frontend_status')
    frontend_servicename = ProxyProperty('frontend_servicename')
    frontend_sessionlimit = ProxyProperty('frontend_sessionlimit')

class HAProxyServersInfo(ComponentInfo):
    implements(IHAProxyServersInfo)
    server_status = ProxyProperty('server_status')
    server_proxyname = ProxyProperty('server_proxyname')

