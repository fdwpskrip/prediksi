from django.shortcuts import render, redirect, get_object_or_404
from home.models import DataCbMerah
from home.forms import DataCbMerahForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'home_data_cbmerah.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataCbMerah.objects.all()


class DataView(ListView):
    template_name = 'proses_data_cbmerah.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataCbMerah.objects.all()


class DataDetailView(DetailView):
    model = DataCbMerah
    template_name = 'data-detailcbmerah.html'


def create(request):
    if request.method == 'POST':
        form = DataCbMerahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:homeview_cbmerah')
    form = DataCbMerahForm()

    return render(request, 'create_cbmerah.html', {'form': form})


def edit(request, pk, template_name='edit_cbmerah.html'):
    data = get_object_or_404(DataCbMerah, pk=pk)
    form = DataCbMerahForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home:homeview_cbmerah')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_deletecbmerah.html'):
    contact = get_object_or_404(DataCbMerah, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home:homeview_cbmerah')
    return render(request, template_name, {'object': contact})