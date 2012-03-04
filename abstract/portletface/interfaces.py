from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IPortletFaceBrowserLayer(IDefaultPloneLayer):
    """ Marker interface that defines a Zope 3 browser layer. """


class IPortletFace(Interface):
    """Marker interface for IPortletFace content types
    """
