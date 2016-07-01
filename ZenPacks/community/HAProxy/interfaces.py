from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IHAProxyBackendsInfo(IComponentInfo):
    backend_status = schema.TextLine(title=_t('Backend Status'))
    backend_sessionlimit = schema.TextLine(title=_t('Beckend Session Limit'))

class IHAProxyFrontendsInfo(IComponentInfo):
    frontend_status = schema.TextLine(title=_t('Frontend Status'))
    frontend_servicename = schema.TextLine(title=_t('Frontend Service Name'))
    frontend_sessionlimit = schema.TextLine(title=_t('Frontend Session Limit'))

class IHAProxyServersInfo(IComponentInfo):
    server_status = schema.TextLine(title=_t('Server Status'))
    server_proxyname = schema.TextLine(title=_t('Servers Proxy Name'))

