from django.shortcuts import reverse
from django.test import RequestFactory, TestCase

from djangoaddicts.pygwalker.views import PygWalkerView, StaticCsvPygWalkerView, DynamicCsvPygWalkerView
from tests.core.testapp.models import TestModel
from django.contrib import messages

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
        url = reverse("basic")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_explicit_fields(self):
        url = reverse("explicit")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pygwalker/bs5/pygwalker.html")

    def test_custom_template(self):
        url = reverse("custom")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "testapp/my_custom_template.html")
        self.assertTemplateNotUsed(response, "pygwalker/bs5/pygwalker.html")


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
