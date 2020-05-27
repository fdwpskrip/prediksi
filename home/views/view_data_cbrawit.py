from django.shortcuts import render, redirect, get_object_or_404
from home.models import DataCbRawit
from home.forms import DataCbRawitForm
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'home_data_cbrawit.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataCbRawit.objects.all()


class DataView(ListView):
    template_name = 'proses_data_cbrawit.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return DataCbRawit.objects.all()


class DataDetailView(DetailView):
    model = DataCbRawit
    template_name = 'data-detail.html'


def create(request):
    if request.method == 'POST':
        form = DataCbRawitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home_view')
    form = DataCbRawitForm()

    return render(request, 'create.html', {'form': form})


def edit(request, pk, template_name='edit.html'):
    data = get_object_or_404(DataCbRawit, pk=pk)
    form = DataCbRawitForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home:home_view')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(DataCbRawit, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home:home_view')
    return render(request, template_name, {'object': contact})
