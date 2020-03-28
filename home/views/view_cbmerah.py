from django.shortcuts import render, redirect, get_object_or_404
from home.models import cbMerah
from home.forms import cbMerahForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'homedata_cbmerah.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return cbMerah.objects.all()

class DataView(ListView):
    template_name = 'home_cabaimerah.html'
    context_object_name = 'data_list'

    def get_queryset(self):
        return cbMerah.objects.all()


class DataDetailView(DetailView):
    model = cbMerah
    template_name = 'data-detailcbmerah.html'

def create(request):
    if request.method == 'POST':
        form = cbMerahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:homeview_cbmerah')
    form = cbMerahForm()

    return render(request, 'create_cbmerah.html', {'form': form})

def edit(request, pk, template_name='edit_cbmerah.html'):
    data = get_object_or_404(cbMerah, pk=pk)
    form = cbMerahForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home:homeview_cbmerah')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_deletecbmerah.html'):
    contact = get_object_or_404(cbMerah, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home:homeview_cbmerah')
    return render(request, template_name, {'object': contact})