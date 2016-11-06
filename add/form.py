from django import forms

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label=" Choose the CSV file")