from django.urls import path

from tests.core.testapp.views import (
    BasicPygWalkerView,
    BasicStaticCsvPygWalkerViewView,
    CustomTemplatePygWalkerView,
    CustomTemplateStaticCsvPygWalkerViewView,
    ExplicitFieldsPygWalkerView,
)

urlpatterns = [
    path("basic/", BasicPygWalkerView.as_view(), name="basic"),
    path("explicit/", ExplicitFieldsPygWalkerView.as_view(), name="explicit"),
    path("custom/", CustomTemplatePygWalkerView.as_view(), name="custom"),
    path("static_basic/", BasicStaticCsvPygWalkerViewView.as_view(), name="static_basic"),
    path("static_custom/", CustomTemplateStaticCsvPygWalkerViewView.as_view(), name="static_custom"),
]
