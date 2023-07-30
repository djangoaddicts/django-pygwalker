from django.urls import path, include

from tests.core.testapp.views import (BasicPygWalkerView, 
                                      ExplicitFieldsPygWalkerView, 
                                      CustomTemplatecPygWalkerView)

urlpatterns = [
    path("basic/", BasicPygWalkerView.as_view(), name="basic"),
    path("explicit/", ExplicitFieldsPygWalkerView.as_view(), name="explicit"),
    path("custom/", CustomTemplatecPygWalkerView.as_view(), name="custom"),
]
