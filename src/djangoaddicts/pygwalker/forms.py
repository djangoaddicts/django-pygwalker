from django import forms


class UploadFileForm(forms.Form):
    """simple form for uploading a csv file"""

    csv_file = forms.FileField()
