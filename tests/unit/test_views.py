from django.test import RequestFactory, TestCase
from django.shortcuts import reverse

from djangoaddicts.pygwalker.views import PygWalkerView
from tests.core.testapp.models import TestModel


class PygWalkerViewTests(TestCase):
    """test PygWalkerView view"""
    class MyPygWalkerView(PygWalkerView):
        queryset = TestModel.objects.none()

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.request = self.factory.get("")
        return super().setUp()

    def test_view(self) -> None:
        """verify PygWalkerViewis called"""
        response = self.MyPygWalkerView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class UsageTests(TestCase):
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
