from django import forms
from .models import Data, cbMerah


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"

class cbMerahForm(forms.ModelForm):
    class Meta:
        model = cbMerah
        fields = "__all__"
