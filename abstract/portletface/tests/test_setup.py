# -*- coding: utf-8 -*-
import unittest2 as unittest
from zope.interface import directlyProvides
from zope.component import getUtility

from Products.CMFPlone.utils import getToolByName

from zope.browsermenu.interfaces import IBrowserMenu

from layers import INTEGRATION_TESTING
from abstract.portletface.interfaces import IPortletFaceBrowserLayer


class TestSetup(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        # marking the request
        directlyProvides(self.request, IPortletFaceBrowserLayer)

    def _get_action_menu(self, obj):
        menu = getUtility(IBrowserMenu,
                    name='plone_contentmenu_actions',
                    context=obj)
        menu_items = menu.getMenuItems(obj, self.request)
        return [i['action'] for i in menu_items]

    def test_setup_dependencies(self):
        pq = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(pq.isProductInstalled('collective.portletpage'),
                                "collective.portletpage is not installed")

    def test_portal_actions(self):
        pa = getToolByName(self.portal, 'portal_actions')
        actions = pa['object_buttons']

        portletface_actions = ['enable_portletface', 'disable_portletface']
        for act in portletface_actions:
            self.assertIn(act, actions.keys())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
