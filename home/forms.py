from django import forms
from django.forms import TextInput

from .models import DataCbRawit, DataCbMerah, DataTestingCbRawit, DataTestingCbMerah

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


class DataCbRawitForm(forms.ModelForm):
    class Meta:
        model = DataCbRawit
        fields = "__all__"


class DataTestingCbRawitForm(forms.ModelForm):
    class Meta:
        model = DataTestingCbRawit
        fields = ['no', 'bulan', 'tahun', 'harga', 'produksi', 'ketersediaan', 'permintaan']


class DataCbMerahForm(forms.ModelForm):
    class Meta:
        model = DataCbMerah
        fields = "__all__"


class DataTestingCbMerahForm(forms.ModelForm):
    class Meta:
        model = DataTestingCbMerah
        fields = ['no', 'bulan', 'tahun', 'harga', 'produksi', 'ketersediaan', 'permintaan']


class DataForm(forms.ModelForm):
    class Meta:
        model = DataCbMerah
        fields = "__all__"


class TrainingForm(forms.Form):
    hidden_neuron = forms.CharField(label='Hidden Neuron', required=True, max_length=100,
                                    widget=TextInput(attrs={'type': 'number'}),
                                    error_messages={'required': "Masukkan Hidden Neuron"})

    rasio_data = forms.ChoiceField(label='Rasio Data Training dan Testing', choices=RASIO_CHOICES)
