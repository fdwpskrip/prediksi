from django.shortcuts import render, redirect, get_object_or_404
from home.models import cbMerah
from home.forms import cbMerahForm
from django.views.generic import ListView, DetailView
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'normalisasi_cbmerah.html'
    context_object_name = 'data'

    def get_queryset(self):
        listdata = cbMerah.objects.all()
        listharga = cbMerah.objects.values_list('harga', flat=True)
        listproduksi = cbMerah.objects.values_list('produksi', flat=True)
        listketersediaan = cbMerah.objects.values_list('ketersediaan', flat=True)
        listpermintaan = cbMerah.objects.values_list('permintaan', flat=True)

        minvalue = {
            'harga': min([int(i) for i in listharga]),
            'produksi': min([float(i) for i in listproduksi]),
            'ketersediaan': min([float(i) for i in listketersediaan]),
            'permintaan': min([float(i) for i in listpermintaan])
        }

        maxvalue = {
            'harga': max([int(i) for i in listharga]),
            'produksi': max([float(i) for i in listproduksi]),
            'ketersediaan': max([float(i) for i in listketersediaan]),
            'permintaan': max([float(i) for i in listpermintaan])
        }

        newmin = 0.1
        newmax = 0.9

        n_data = []
        n_harga = []
        n_produksi = []
        n_ketersediaan = []
        n_permintaan = []

        for x in listdata:
            data = {
                'bulan': x.bulan,
                'tahun': x.tahun,
                'harga': 0,
                'produksi': 0,
                'ketersediaan': 0,
                'permintaan': 0
            }
            n_data.append(data)

        for i, x in enumerate(listharga):
            n = (((int(x) - minvalue['harga']) * (newmax-newmin)) / (maxvalue['harga']-minvalue['harga'])) + newmin
            n_harga.append(n)
            n_data[i]['harga'] = float(n)

        for i, x in enumerate(listproduksi):
            n = (((float(x) - minvalue['produksi']) * (newmax - newmin)) / (maxvalue['produksi']-minvalue['produksi'])) + newmin
            n_produksi.append(n)
            n_data[i]['produksi'] = float(n)

        for i, x in enumerate(listketersediaan):
            n = (((float(x) - minvalue['ketersediaan']) * (newmax - newmin)) / (maxvalue['ketersediaan']-minvalue['ketersediaan'])) + newmin
            n_ketersediaan.append(n)
            n_data[i]['ketersediaan'] = float(n)

        for i, x in enumerate(listpermintaan):
            n = (((float(x) - minvalue['permintaan']) * (newmax - newmin)) / (maxvalue['permintaan']-minvalue['permintaan'])) + newmin
            n_permintaan.append(n)
            n_data[i]['permintaan'] = float(n)

        context = {
            'min': minvalue,
            'max': maxvalue,
            'newmin': newmin,
            'newmax': newmax,
            'n_data': n_data
        }

        return context

