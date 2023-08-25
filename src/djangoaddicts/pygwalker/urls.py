from django.urls import path

from djangoaddicts.pygwalker.views import DynamicCsvPygWalkerView, GenericPygWalkerView

app_name = "pygwalker"

urlpatterns = [
    path("", DynamicCsvPygWalkerView.as_view(), name=""),
    path("csv", DynamicCsvPygWalkerView.as_view(), name="csv"),
    path("dynamic", DynamicCsvPygWalkerView.as_view(), name="dynamic"),
    path("file", DynamicCsvPygWalkerView.as_view(), name="file"),
    path("generic_pyg/<str:app_name>/<str:model_name>/", GenericPygWalkerView.as_view(), name="generic_pyg"),
]
