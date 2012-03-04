# -*- coding: utf-8 -*-
from plone.testing import z2
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from plone.app.testing import IntegrationTesting, FunctionalTesting


class PortletFaceFixture(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # pylint: disable=W0613
        import abstract.portletface
        self.loadZCML(package=abstract.portletface)

        z2.installProduct(app, 'collective.portletpage')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'abstract.portletface:default')

        setRoles(portal, TEST_USER_ID, ['Manager'])
        self.doc_id = portal.invokeFactory('Document', 'test_document')
        self.folder_id = portal.invokeFactory('Folder', 'test_folder')
        setRoles(portal, TEST_USER_ID, ['Member'])

    def tearDownZope(self, app):
        # Uninstall Zope2 products
        z2.uninstallProduct(app, 'collective.portletpage')


BASE_FIXTURE = PortletFaceFixture()

INTEGRATION_TESTING = IntegrationTesting(
                                    bases=(BASE_FIXTURE, ),
                                    name="PortletFaceFixture:Integration")

FUNCTIONAL_TESTING = FunctionalTesting(
                                    bases=(BASE_FIXTURE, ),
                                    name="PortletFaceFixture:Functional")
