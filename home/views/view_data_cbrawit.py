from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get

from home.models import DataCbRawit
from home.forms import DataCbRawitForm


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
    template_name = 'data-detailcbrawit.html'


def create(request):
    form = DataCbRawitForm()

    if request.method == 'POST':
        if request.POST.get("input_excel"):
            try:
                excel_file = request.FILES['file-excel']
            except MultiValueDictKeyError:
                return render(request, 'create_cbrawit.html', {'form': form})

            if str(excel_file).split('.')[-1] == 'xls':
                data = xls_get(excel_file, column_limit=7)
            elif str(excel_file).split('.')[-1] == 'xlsx':
                data = xlsx_get(excel_file, column_limit=7)
            else:
                return render(request, 'create_cbrawit.html', {'form': form})

            if data is not None:
                save_excel_to_db(data)
                return redirect('home:home_view')
        else:
            form = DataCbRawitForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home:home_view')

    return render(request, 'create_cbrawit.html', {'form': form})


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


def save_excel_to_db(data_excel):
    for d_sheet in data_excel:
        sheet = data_excel[d_sheet]
        if len(sheet) > 1:  # data sheet
            for data in sheet:
                if len(data) > 0:  # check row tidak kosong
                    if str(data[0]).lower() != 'no':  # check bukan header

                        # Check jika ada data yg kosong
                        if len(data) < 7:
                            i = len(data)
                            while i < 7:
                                data.append('')
                                i += 1

                        # Simpan data
                        no = data[0]
                        db = DataCbRawit.objects.filter(no=str(no))

                        if len(db) == 0:
                            DataCbRawit.objects.create(
                                no=data[0],
                                bulan=data[1],
                                tahun=data[2],
                                harga=data[3],
                                produksi=data[4],
                                ketersediaan=data[5],
                                permintaan=data[6]
                            )
                        else:
                            dt = db[0]
                            dt.no = data[0]
                            dt.bulan = data[1]
                            dt.tahun = data[2]
                            dt.harga = data[3]
                            dt.produksi = data[4]
                            dt.ketersediaan = data[5]
                            dt.permintaan = data[6]
                            dt.save()

