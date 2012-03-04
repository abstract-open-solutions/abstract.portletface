# -*- coding: utf-8 -*-
import unittest2 as unittest
from zope.interface import directlyProvides
from zope.component import queryMultiAdapter

# from Products.CMFPlone.utils import getToolByName
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from layers import INTEGRATION_TESTING

from abstract.portletface.interfaces import IPortletFaceBrowserLayer


class TestSetup(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        # marking the request
        directlyProvides(self.request, IPortletFaceBrowserLayer)

    def test_enable_disable_portlets(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        doc_id = self.portal.invokeFactory('Document', 'test_document_1')
        doc = self.portal[doc_id]

        enabled_view = queryMultiAdapter((doc, self.request),
                                    name='portletface_enabled')

        self.assertFalse(enabled_view.is_enabled)

        view = queryMultiAdapter((doc, self.request),
                                    name='enable_portletface')

        self.assertIsNotNone(view)
        # enabling portletface
        view()
        self.assertTrue(enabled_view.is_enabled)

        view = queryMultiAdapter((doc, self.request),
                                    name='disable_portletface')

        self.assertIsNotNone(view)
        # disabling portletface
        view()

        self.assertFalse(enabled_view.is_enabled)

        setRoles(self.portal, TEST_USER_ID, ['Member'])


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
