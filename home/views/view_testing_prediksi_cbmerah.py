from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from home.models import DataTestingCbMerah
from home.forms import DataTestingCbMerahForm
from home.views import prediksi


class IndexView(ListView):
    template_name = 'proses_testing_prediksi_cbmerah.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataTestingCbMerah.objects.all()


class DataDetailView(DetailView):
    model = DataTestingCbMerah
    template_name = 'proses_prediksi_detail_cbmerah.html'


def create(request):
    form = DataTestingCbMerahForm()

    if request.method == 'POST':
        form = DataTestingCbMerahForm(request.POST)
        if form.is_valid():
            form.save()

            # Prediksi
            prediksi.get_data_testing('cbmerah')

            return redirect('home:prediksi_cbmerah')

    return render(request, 'proses_predisksi_create_cbmerah.html', {'form': form})


def edit(request, pk, template_name='edit_cbmerah.html'):
    data = get_object_or_404(DataTestingCbMerah, pk=pk)
    form = DataTestingCbMerahForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()

        # Prediksi
        prediksi.get_data_testing('cbmerah')

        return redirect('home:prediksi_cbmerah')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_delete_cbmerah.html'):
    data = get_object_or_404(DataTestingCbMerah, pk=pk)
    if request.method == 'POST':
        data.delete()

        # Prediksi
        prediksi.get_data_testing('cbmerah')

        return redirect('home:prediksi_cbmerah')
    return render(request, template_name, {'object': data})
