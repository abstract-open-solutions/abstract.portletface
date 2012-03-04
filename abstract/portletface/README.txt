Abstract.portletface
====================

We start with a standard test boilerplate:

    >>> from plone.testing.z2 import Browser
    >>> from plone.app.testing import TEST_USER_NAME
    >>> from plone.app.testing import TEST_USER_PASSWORD
    >>> browser = Browser(layer['app'])
    >>> browser.addHeader('Authorization',
    ...     'Basic %s:%s' % (TEST_USER_NAME, TEST_USER_PASSWORD,))


When we open a page, we can enable portlet page behaviour by clicking on
'Enable extra portlets' link on actions menu.

    >>> doc = layer['portal']['test_document']
    >>> browser.open(doc.absolute_url())
    >>> browser.getLink('Enable extra portlets').click()
    >>> 'Extra portlets have been enabled' in browser.contents
    True

We can manage all contextual portlets by 'Portlets' link in the edit bar.
(See collective.portletpage tests for further informations):

    >>> browser.getLink('Portlets').click()
    >>> 'Manage Portlet Page portlets' in browser.contents
    True


After that we can disable the extra portlets in this context by clicking on
'Disable extra portlets' link on actions menu:

    >>> browser.open(doc.absolute_url())
    >>> browser.getLink('Disable extra portlets').click()
    >>> 'Extra portlets have been disabled' in browser.contents
    True

This behaviout works only for not folderish content types::

    >>> folder = layer['portal']['test_folder']
    >>> browser.open(folder.absolute_url())
    >>> browser.getLink('Enable extra portlets')
    Traceback (most recent call last):
    ...
    LinkNotFoundError

