from django.urls import path, include

from tests.core.testapp.views import (
    BasicPygWalkerView,
    BasicStaticCsvPygWalkerViewView,
    CustomTitlePygWalkerView,
    CustomTemplatePygWalkerView,
    CustomTemplateStaticCsvPygWalkerViewView,
    ExplicitFieldsPygWalkerView,
    TestModelListView,
    TestModelPaginatedListView,
)

urlpatterns = [
    path("basic/", BasicPygWalkerView.as_view(), name="basic"),
    path("custom_title/", CustomTitlePygWalkerView.as_view(), name="custom_title"),
    path("explicit/", ExplicitFieldsPygWalkerView.as_view(), name="explicit"),
    path("custom/", CustomTemplatePygWalkerView.as_view(), name="custom"),
    path("static_basic/", BasicStaticCsvPygWalkerViewView.as_view(), name="static_basic"),
    path("static_custom/", CustomTemplateStaticCsvPygWalkerViewView.as_view(), name="static_custom"),
    path("test_model_list_view/", TestModelListView.as_view(), name="test_model_list_view"),
    path(
        "test_model_paginated_list_view/", TestModelPaginatedListView.as_view(), name="test_model_paginated_list_view"
    ),
    path("pygwalker/", include("djangoaddicts.pygwalker.urls")),
]
