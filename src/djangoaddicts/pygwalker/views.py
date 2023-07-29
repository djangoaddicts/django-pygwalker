import pandas as pd
import pygwalker as pyg
from django.shortcuts import render
from django.views.generic import View


class PygView(View):
    """View to create a PyGWalker visualization interface from a Django queryset.
    See https://github.com/Kanaries/pygwalker for more information on PyGWalker.

    class parameters:
        field_list    - list of model fields to include
        queryset      - queryset providing data available to visualization
        theme         - PyGWalker theme to use for pyg html (defaults to "media")
        title         - title used on html render
        template_name - template used when rendering page; defaults to: pygwalker/bs5/pyg.html

    example:

        from djangoaddicts.pygwalker.views import PygView
        class MyPygView(PygView):
            queryset = Order.objects.all()
            title = "Order Data Analysis"
            theme = "light"
            field_list = ["status__name", "customer", "order_id", "created_at", "updated_at", "products"]
    """

    field_list: list = []
    queryset = None
    template_name: str = "storemgr/pyg/pyg.html"
    theme: str = "media"
    title: str = "Data Analysis"

    def get(self, request):
        pd_data = pd.DataFrame(list(self.queryset.values(*self.field_list)))
        context = {"pyg": pyg.walk(pd_data, return_html=True, dark=self.theme), "title": self.title}
        return render(request, self.template_name, context)
