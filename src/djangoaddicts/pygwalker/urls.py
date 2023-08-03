from django.urls import path

from djangoaddicts.pygwalker.views import DynamicCsvPygWalkerView

app_name = "pygwalker"

urlpatterns = [
    path("", DynamicCsvPygWalkerView.as_view(), name=""),
]
