from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from home.models import DataTestingCbRawit
from home.forms import DataTestingCbRawitForm
from home.views import prediksi


class IndexView(ListView):
    template_name = 'proses_testing_prediksi_cbrawit.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTestingCbRawit.objects.all()


class DataDetailView(DetailView):
    model = DataTestingCbRawit
    template_name = 'proses_prediksi_detail_cbrawit.html'


def create(request):
    form = DataTestingCbRawitForm(initial={"permintaan": "0"})

    if request.method == 'POST':
        form = DataTestingCbRawitForm(request.POST)
        if form.is_valid():
            form.fields['permintaan'].initial = 0
            form.save()

            # Prediksi
            prediksi.get_data_testing('cbrawit')

            return redirect('home:prediksi_cbrawit')

    return render(request, 'proses_predisksi_create_cbrawit.html', {'form': form})


def edit(request, pk, template_name='edit_cbrawit.html'):
    data = get_object_or_404(DataTestingCbRawit, pk=pk)
    form = DataTestingCbRawitForm(request.POST or None, instance=data, initial={"permintaan": "0"})
    if form.is_valid():
        form.save()

        # Prediksi
        prediksi.get_data_testing('cbrawit')

        return redirect('home:prediksi_cbrawit')
    return render(request, template_name, {'form': form})