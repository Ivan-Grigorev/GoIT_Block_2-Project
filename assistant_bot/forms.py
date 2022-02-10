from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget

from .models import AddressBook

from datetime import datetime


class AddAddressBook(ModelForm):
    class Meta:
        model = AddressBook
        fields = ['name', 'surname', 'phone', 'email', 'address', 'birthday']
        widgets = {
            'birthday': SelectDateWidget(
                years=[year for year in range(1950, datetime.now().year + 1)]
            )
        }


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
