from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from abstract.portletface.interfaces import IPortletFace
from abstract.portletface import MessageFactory as _


class EnablePortletFace(BrowserView):
    def __call__(self):
        alsoProvides(self.context, IPortletFace)
        plone_utils = getToolByName(self.context, 'plone_utils')
        plone_utils.addPortalMessage(_(u"Extra portlets have been enabled"))
        self.request.response.redirect(self.context.absolute_url())


class DisablePortletFace(BrowserView):
    def __call__(self):
        noLongerProvides(self.context, IPortletFace)
        plone_utils = getToolByName(self.context, 'plone_utils')
        plone_utils.addPortalMessage(_(u"Extra portlets have been disabled"))
        self.request.response.redirect(self.context.absolute_url())


class PortletFaceEnabled(BrowserView):
    @property
    def is_enabled(self):
        return IPortletFace.providedBy(self.context)
