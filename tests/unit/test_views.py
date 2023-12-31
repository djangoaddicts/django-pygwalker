from django.shortcuts import reverse
from django.test import RequestFactory, TestCase

from djangoaddicts.pygwalker.views import PygWalkerView, StaticCsvPygWalkerView, PygWalkerListView, PygWalkerPaginatedListView
from tests.core.testapp.forms import TestForm
from tests.core.testapp.models import TestModel
from model_bakery import baker


class PygWalkerViewCallTests(TestCase):
    """test PygWalkerView view"""

    class MyPygWalkerView(PygWalkerView):
        queryset = TestModel.objects.none()

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.request = self.factory.get("")
        return super().setUp()

    def test_view(self) -> None:
        """verify PygWalkerView is called"""
        response = self.MyPygWalkerView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class StaticCsvPygWalkerViewCallTests(TestCase):
    """test StaticCsvPygWalkerView view"""

    class MyPygWalkerView(StaticCsvPygWalkerView):
        csv_file = "tests/data/data.csv"

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.request = self.factory.get("")
        return super().setUp()

    def test_view(self) -> None:
        """verify StaticCsvPygWalkerView is called"""
        response = self.MyPygWalkerView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class PygWalkerViewUsageTests(TestCase):
    def test_basic(self):
        baker.make("testapp.TestModel")
        url = reverse("basic")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_basic_no_data(self):
        url = reverse("basic")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_custom_template(self):
        baker.make("testapp.TestModel")
        url = reverse("custom")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "testapp/my_custom_template.html")
        self.assertTemplateNotUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_explicit_fields(self):
        baker.make("testapp.TestModel")
        url = reverse("explicit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_custom_title(self):
        baker.make("testapp.TestModel")
        url = reverse("custom_title")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_with_referrer(self):
        baker.make("testapp.TestModel")
        url = reverse("basic")
        response = self.client.get(url, HTTP_REFERER="/?name=blah")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")


class StaticCsvPygWalkerViewUsageTests(TestCase):
    def test_basic(self):
        url = reverse("static_basic")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_custom_template(self):
        url = reverse("static_custom")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "testapp/my_custom_template.html")
        self.assertTemplateNotUsed(response, "pygwalker/bs5/pygwalker.html")


class DynamicCsvPygWalkerTests(TestCase):
    """test DynamicCsvPygWalker view"""
    def test_get(self):
        url = reverse("pygwalker:")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker_dynamic.html")

    def test_post(self):
        url = reverse("pygwalker:")
        with open("./tests/data/data.csv") as csv_file:
            response = self.client.post(url, data={"csv_file": csv_file})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker_dynamic.html")

    def test_post_invalid_file(self):
        url = reverse("pygwalker:")
        with open("./tests/data/invalid") as csv_file:
            response = self.client.post(url, data={"csv_file": csv_file})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker_dynamic.html")

    def test_post_blank_file(self):
        url = reverse("pygwalker:")
        with open("./tests/data/blank") as csv_file:
            response = self.client.post(url, data={"csv_file": csv_file})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker_dynamic.html")


class GenericPygWalkerTests(TestCase):
    """test GenericPygWalkerTests view"""
    def test_get(self):
        baker.make("testapp.TestModel")
        url = reverse("pygwalker:generic_pyg", kwargs={"app_name":"testapp", "model_name":"testmodel"})
        response = self.client.get(url)
        self.assertTrue(True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_get_with_referrer(self):
        baker.make("testapp.TestModel")
        url = reverse("pygwalker:generic_pyg", kwargs={"app_name":"testapp", "model_name":"testmodel"})
        response = self.client.get(url, **{"HTTP_REFERER": "/home?name=blah"})
        self.assertTrue(True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")


class PygWalkerListViewCallTests(TestCase):
    """test PygWalkerListView view"""

    class MyPygWalkerListView(PygWalkerListView):
        queryset = TestModel.objects.none()
        pygwalker_url = f"/pygwalker/generic_pyg/{queryset.model._meta.app_label}/{queryset.model._meta.model_name}"
        filter_form_obj = TestForm
        create_form_obj = TestForm

    class MyPygWalkerListViewNoUrl(PygWalkerListView):
        queryset = TestModel.objects.none()

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.request = self.factory.get("")
        return super().setUp()

    def test_view(self) -> None:
        """verify PygWalkerListView is called"""
        response = self.MyPygWalkerListView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_view_no_url(self) -> None:
        """verify PygWalkerListView is called"""
        response = self.MyPygWalkerListViewNoUrl.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class PygWalkerListViewUsageTests(TestCase):
    def test_basic(self):
        url = reverse("test_model_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "handyhelpers/generic/bs5/generic_list.html")


class PygWalkerPaginatedListViewCallTests(TestCase):
    """test PygWalkerPaginatedListView view"""

    class MyPygWalkerPaginatedListView(PygWalkerPaginatedListView):
        queryset = TestModel.objects.none()
        pygwalker_url = f"/pygwalker/generic_pyg/{queryset.model._meta.app_label}/{queryset.model._meta.model_name}"
        filter_form_obj = TestForm
        create_form_obj = TestForm

    class MyPygWalkerPaginatedListViewNoUrl(PygWalkerPaginatedListView):
        queryset = TestModel.objects.none()

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.request = self.factory.get("")
        return super().setUp()

    def test_view(self) -> None:
        """verify PygWalkerListView is called"""
        response = self.MyPygWalkerPaginatedListView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_view_no_url(self) -> None:
        """verify PygWalkerListView is called"""
        response = self.MyPygWalkerPaginatedListViewNoUrl.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class PygWalkerPaginatedListViewUsageTests(TestCase):
    def test_basic(self):
        url = reverse("test_model_paginated_list_view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "handyhelpers/generic/bs5/generic_list.html")
