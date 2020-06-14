from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get

from home.models import DataCbMerah
from home.forms import DataCbMerahForm


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
    form = DataCbMerahForm()

    if request.method == 'POST':
        if request.POST.get("input_excel"):
            try:
                excel_file = request.FILES['file-excel']
            except MultiValueDictKeyError:
                return render(request, 'create_cbmerah.html', {'form': form})

            if str(excel_file).split('.')[-1] == 'xls':
                data = xls_get(excel_file, column_limit=7)
            elif str(excel_file).split('.')[-1] == 'xlsx':
                data = xlsx_get(excel_file, column_limit=7)
            else:
                return render(request, 'create_cbmerah.html', {'form': form})

            if data is not None:
                save_excel_to_db(data)
                return redirect('home:homeview_cbmerah')
        else:
            form = DataCbMerahForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home:homeview_cbmerah')

    return render(request, 'create_cbmerah.html', {'form': form})


def edit(request, pk, template_name='edit_cbmerah.html'):
    data = get_object_or_404(DataCbMerah, pk=pk)
    form = DataCbMerahForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        return redirect('home:homeview_cbmerah')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='confirm_delete_cbmerah.html'):
    contact = get_object_or_404(DataCbMerah, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home:homeview_cbmerah')
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
                        db = DataCbMerah.objects.filter(no=str(no))

                        if len(db) == 0:
                            DataCbMerah.objects.create(
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
