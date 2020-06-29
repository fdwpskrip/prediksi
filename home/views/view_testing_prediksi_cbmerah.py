from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView

from home.models import DataCbMerah, DataTestingCbRawit, DataTestingCbMerah
from home.forms import DataCbMerahForm, DataTestingCbMerahForm


class IndexView(ListView):
    template_name = 'proses_testing_prediksi_cbmerah.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTestingCbMerah.objects.all()


def create(request):
    form = DataTestingCbMerahForm()

    if request.method == 'POST':
        form = DataTestingCbMerahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:prediksi_cbmerah')

    return render(request, 'proses_predisksi_create_cbmerah.html', {'form': form})
