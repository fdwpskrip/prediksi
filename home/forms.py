from django import forms
from django.forms import TextInput

from .models import Data, cbMerah

RASIO_CHOICES = (
        ('-', '--Pilih Rasio Data--'),
        ('50:50', '50% : 50%'),
        ('60:40', '60% : 40%'),
        ('70:30', '70% : 30%'),
        ('80:20', '80% : 20%'),
        ('90:10', '90% : 10%'),
        ('10:90', '10% : 90%'),
        ('20:80', '20% : 80%'),
        ('30:70', '30% : 70%'),
        ('40:60', '40% : 60%')
    )


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"


class cbMerahForm(forms.ModelForm):
    class Meta:
        model = cbMerah
        fields = "__all__"


class TrainingForm(forms.Form):
    hidden_neuron = forms.CharField(label='Hidden Neuron', required=True, max_length=100,
                                    widget=TextInput(attrs={'type': 'number'}),
                                    error_messages={'required': "Masukkan Hidden Neuron"})

    rasio_data = forms.ChoiceField(label='Rasio Data Training dan Testing', choices=RASIO_CHOICES)
