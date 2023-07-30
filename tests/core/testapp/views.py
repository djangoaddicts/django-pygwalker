from djangoaddicts.pygwalker.views import PygWalkerView

from tests.core.testapp.models import TestModel


class BasicPygWalkerView(PygWalkerView):
    queryset = TestModel.objects.all()


class ExplicitFieldsPygWalkerView(PygWalkerView):
    queryset = TestModel.objects.all()
    title = "TestModel Data Analysis"
    theme = "light"
    field_list = ["name"]


class CustomTemplatecPygWalkerView(PygWalkerView):
    queryset = TestModel.objects.all()
    template_name = "testapp/my_custom_template.html"
