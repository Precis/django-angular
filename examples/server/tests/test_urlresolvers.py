# -*- coding: utf-8 -*-
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from djangular.core.urlresolvers import get_all_remote_methods, get_current_remote_methods
from server.tests.urls import RemoteMethodsView


class TemplateRemoteMethods(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @override_settings(ROOT_URLCONF='server.tests.urls')
    def test_get_current_remote_methods(self):
        view = RemoteMethodsView()
        view.request = self.factory.get('/straight_methods/')
        remote_methods = get_current_remote_methods(view)
        self.assertDictEqual({'foo': {'url': '/straight_methods/', 'headers': {'DjNg-Remote-Method': 'foo'}, 'method': 'auto'}, 'bar': {'url': '/straight_methods/', 'headers': {'DjNg-Remote-Method': 'bar'}, 'method': 'auto'}},
                             remote_methods)

    @override_settings(ROOT_URLCONF='server.tests.urls')
    def test_get_all_remote_methods(self):
        remote_methods = get_all_remote_methods()
        self.assertDictEqual(remote_methods, {'submethods': {'sub': {'app': {'foo': {'url': '/sub_methods/sub/app/', 'headers': {'DjNg-Remote-Method': 'foo'}, 'method': 'auto'}, 'bar': {'url': '/sub_methods/sub/app/', 'headers': {'DjNg-Remote-Method': 'bar'}, 'method': 'auto'}}}}, 'straightmethods': {'foo': {'url': '/straight_methods/', 'headers': {'DjNg-Remote-Method': 'foo'}, 'method': 'auto'}, 'bar': {'url': '/straight_methods/', 'headers': {'DjNg-Remote-Method': 'bar'}, 'method': 'auto'}}})
