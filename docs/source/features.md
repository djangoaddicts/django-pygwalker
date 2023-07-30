# Features

The PygWalkerView view renders a page containing PyGWalker html. This view takes a queryset parameter and included all data in the queryset for visualizations. By default fields defined in the model will be included. To exclude fields or include additional fields (such as related fields), use the field_list parameter to specify exact fields desired for visualizations.  

A Bootstrap 5 template is included, but can be overwritten using the template_name parameter. 

## Parameters
- **field_list:** list of model fields to include (defaults to fields defined in the model)
- **queryset:** queryset providing data available to visualization
- **theme:** PyGWalker theme to use for pyg html (defaults to "media")
- **title:** title used on html render
- **template_name:** template used when rendering page; (defaults to pygwalker/bs5/pygwalker.html)

<br/>


## Usage Examples

```python
from djangoaddicts.pygwalker.views import PygWalkerView

class MyPygWalkerView(PygWalkerView):
    queryset = MyModel.objects.all()
```

#### Explicitly Defined Fields

```python
from djangoaddicts.pygwalker.views import PygWalkerView

class MyPygWalkerView(PygWalkerView):
    queryset = MyModel.objects.all()
    title = "MyModel Data Analysis"
    theme = "light"
    field_list = ["name", "some_field", "some_other__related_field", "id", "created_at", "updated_at"]
```


#### Custom Template
Custom views/templates can be used to override the Bootstrap 5 templates provided by default view. Here is an example:

```python
from djangoaddicts.pygwalker.views import PygWalkerView

class MyPygWalkerView(PygWalkerView):
    queryset = MyModel.objects.all()
    template_name = "my_custom_template.html"
```
