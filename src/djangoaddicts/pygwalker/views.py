import mimetypes

import pandas as pd
import pygwalker as pyg
from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.gui import HandyHelperListView, HandyHelperPaginatedListView

from djangoaddicts.pygwalker.forms import UploadFileForm


class PygWalkerView(View):
    """View to create a PyGWalker visualization interface from a Django queryset.
    See https://github.com/Kanaries/pygwalker for more information on PyGWalker.

    class parameters:
        field_list    - list of model fields to include; defaults to fields defined in the model
        queryset      - queryset providing data available to visualization
        template_name - template used when rendering page; defaults to: pygwalker/bs5/pyg.html
        theme         - PyGWalker theme to use for pyg html; defaults to: "media"
        title         - title used on html render

    example:

        from djangoaddicts.pygwalker.views import PygWalkerView
        class MyPygView(PygWalkerView):
            queryset = Order.objects.all()
            title = "Order Data Analysis"
            theme = "light"
            field_list = ["status__name", "customer", "order_id", "created_at", "updated_at", "products"]
    """

    field_list: list = []
    queryset: QuerySet = None
    template_name: str = "pygwalker/bs5/pygwalker.html"
    theme: str = getattr(settings, "PYGWALKER_THEME", "media")
    title: str = "Data Analysis"

    def get(self, request):
        pd_data = pd.DataFrame(list(self.queryset.values(*self.field_list)))
        context = {"pyg": pyg.walk(pd_data, return_html=True, dark=self.theme), "title": self.title}
        return render(request, self.template_name, context)


class StaticCsvPygWalkerView(View):
    """View to create a PyGWalker visualization interface from a statically definied csv file.
    See https://github.com/Kanaries/pygwalker for more information on PyGWalker.

    class parameters:
        csv_file      - csv file containing data to visualize
        template_name - template used when rendering page; defaults to: pygwalker/bs5/pyg.html
        theme         - PyGWalker theme to use for pyg html; defaults to: "media"
        title         - title used on html render

    example:

        from djangoaddicts.pygwalker.views import StaticCsvPygWalkerView
        class MyPygView(StaticCsvPygWalkerView):
            csv_file = "my_csv_file.csv
            title = "Order Data Analysis"
            theme = "light"
    """

    csv_file = None
    template_name: str = "pygwalker/bs5/pygwalker.html"
    theme: str = getattr(settings, "PYGWALKER_THEME", "media")
    title: str = "Data Analysis"

    def get(self, request):
        pd_data = pd.read_csv(self.csv_file)
        context = {"pyg": pyg.walk(pd_data, return_html=True, dark=self.theme), "title": self.title}
        return render(request, self.template_name, context)


class DynamicCsvPygWalkerView(View):
    """View to create a PyGWalker visualization interface from a provided csv file.
    See https://github.com/Kanaries/pygwalker for more information on PyGWalker.

    class parameters:
        template_name - template used when rendering page; defaults to: pygwalker/bs5/pygwalker_dynamic.html
        theme         - PyGWalker theme to use for pyg html; defaults to "media"
        title         - title used on html render
    """

    template_name: str = "pygwalker/bs5/pygwalker_dynamic.html"
    theme: str = getattr(settings, "PYGWALKER_THEME", "media")
    title: str = "Upload a csv file"

    def get(self, request):
        context = {"form": UploadFileForm(), "title": "Upload a csv file"}
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data["csv_file"]
            if mimetypes.guess_type(csv_file.name)[0] not in ["text/csv"]:
                messages.add_message(
                    request, messages.ERROR, "file provided is not a csv file", extra_tags="alert-danger"
                )
                return render(request, self.template_name, context)
            pd_data = pd.read_csv(csv_file)
            context["pyg"] = pyg.walk(pd_data, return_html=True, dark=self.theme)
            context[
                "title"
            ] = f"""Showing data from <span class="text-secondary">{csv_file.name.split("/")[-1]}</span>"""
            return render(request, self.template_name, context)
        else:
            for error in form.errors:
                for i in form.errors[error].data:
                    for msg in i.messages:
                        messages.add_message(
                            self.request,
                            messages.ERROR,
                            msg,
                            extra_tags="alert-danger",
                        )
        return self.get(request)


class GenericPygWalkerView(View):
    """View to create a PyGWalker visualization interface from an app and model passed as kwargs. If query
    parameters are present, include only filtered data, based on query parameters, in the PyGWalker interface."""

    field_list: list = []
    queryset: QuerySet = None
    template_name: str = "pygwalker/bs5/pygwalker.html"
    theme: str = getattr(settings, "PYGWALKER_THEME", "media")
    title: str = "Data Analysis"

    def get(self, request, **kwargs):
        """process GET request"""
        referrer = request.META.get("HTTP_REFERER", "")
        if "?" in referrer:
            query_dict = {
                key: value for key, value in (item.split("=") for item in referrer.split("?")[1].split("&") if item)
            }
        else:
            query_dict = {}
        model = apps.get_model(kwargs["app_name"], kwargs["model_name"])
        self.queryset = model.objects.filter(**query_dict)
        pd_data = pd.DataFrame(list(self.queryset.values(*self.field_list)))
        context = {"pyg": pyg.walk(pd_data, return_html=True, dark=self.theme), "title": self.title}
        return render(request, self.template_name, context)


class PygWalkerListViewMixin:
    pygwalker_icon: str = """<i class="fa-solid fa-magnifying-glass-chart"></i>"""
    pygwalker_title: str = "PyGWalker view"

    def get(self, request, *args, **kwargs): 
        self.pygwalker_url = (
            f"/pygwalker/generic_pyg/{self.queryset.model._meta.app_label}/{self.queryset.model._meta.model_name}"
        )

        self.extra_controls['pygwalker'] = \
            {"icon": self.pygwalker_icon,
             "title": self.pygwalker_title,
             "url": self.pygwalker_url,
             }
        return super().get(request, *args, **kwargs)


class PygWalkerListView(PygWalkerListViewMixin, HandyHelperListView):
    """extend the HandyHelperListView (from handyhelpers) to add an icon for a PyGWalker
    visualzation interface. If the list view is filtered, include only filtered data in the PyGWalker interface."""
 

class PygWalkerPaginatedListView(PygWalkerListViewMixin, HandyHelperPaginatedListView):
    """extend the HandyHelperPaginatedListView (from handyhelpers) to add an icon for a PyGWalker 
    visualzation interface. If the list view is filtered, include only filtered data in the PyGWalker interface."""
 