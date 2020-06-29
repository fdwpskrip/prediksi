from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView

from home.models import DataCbMerah, DataTestingCbRawit
from home.forms import DataCbMerahForm, DataTestingCbRawitForm


class IndexView(ListView):
    template_name = 'proses_testing_prediksi_cbrawit.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTestingCbRawit.objects.all()


def create(request):
    form = DataTestingCbRawitForm()

    if request.method == 'POST':
        form = DataTestingCbRawitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:prediksi_cbrawit')

    return render(request, 'proses_predisksi_create_cbrawit.html', {'form': form})