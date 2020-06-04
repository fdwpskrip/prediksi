from home.models import DataCbRawit
from home.models import DataCbMerah


def getnormalisasi_cbrawit():
    listdata = DataCbRawit.objects.all()
    listharga = DataCbRawit.objects.values_list('harga', flat=True)
    listproduksi = DataCbRawit.objects.values_list('produksi', flat=True)
    listketersediaan = DataCbRawit.objects.values_list('ketersediaan', flat=True)
    listpermintaan = DataCbRawit.objects.values_list('permintaan', flat=True)

    data_cbrawit = {
        'listdata': listdata,
        'listharga': listharga,
        'listproduksi': listproduksi,
        'listketersediaan': listketersediaan,
        'listpermintaan': listpermintaan
    }

    return getnormalisasi(data_cbrawit)


def getnormalisasi_cbmerah():
    listdata = DataCbMerah.objects.all()
    listharga = DataCbMerah.objects.values_list('harga', flat=True)
    listproduksi = DataCbMerah.objects.values_list('produksi', flat=True)
    listketersediaan = DataCbMerah.objects.values_list('ketersediaan', flat=True)
    listpermintaan = DataCbMerah.objects.values_list('permintaan', flat=True)

    data_cbmerah = {
        'listdata': listdata,
        'listharga': listharga,
        'listproduksi': listproduksi,
        'listketersediaan': listketersediaan,
        'listpermintaan': listpermintaan
    }

    return getnormalisasi(data_cbmerah)


def getnormalisasi(list_data):

    listdata = list_data['listdata']
    listharga = list_data['listharga']
    listproduksi = list_data['listproduksi']
    listketersediaan = list_data['listketersediaan']
    listpermintaan = list_data['listpermintaan']

    minvalue = {
        'type': 'Min',
        'harga': min([int(i) for i in listharga]),
        'produksi': min([float(i) for i in listproduksi]),
        'ketersediaan': min([float(i) for i in listketersediaan]),
        'permintaan': min([float(i) for i in listpermintaan])
    }

    maxvalue = {
        'type': 'Max',
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
        n = (((int(x) - minvalue['harga']) * (newmax - newmin)) / (maxvalue['harga'] - minvalue['harga'])) + newmin
        n_harga.append(n)
        n_data[i]['harga'] = float(n)

    for i, x in enumerate(listproduksi):
        n = (((float(x) - minvalue['produksi']) * (newmax - newmin)) / (
                    maxvalue['produksi'] - minvalue['produksi'])) + newmin
        n_produksi.append(n)
        n_data[i]['produksi'] = float(n)

    for i, x in enumerate(listketersediaan):
        n = (((float(x) - minvalue['ketersediaan']) * (newmax - newmin)) / (
                    maxvalue['ketersediaan'] - minvalue['ketersediaan'])) + newmin
        n_ketersediaan.append(n)
        n_data[i]['ketersediaan'] = float(n)

    for i, x in enumerate(listpermintaan):
        n = (((float(x) - minvalue['permintaan']) * (newmax - newmin)) / (
                    maxvalue['permintaan'] - minvalue['permintaan'])) + newmin
        n_permintaan.append(n)
        n_data[i]['permintaan'] = float(n)

    normalisasi = {
        'min': minvalue,
        'max': maxvalue,
        'newmin': newmin,
        'newmax': newmax,
        'n_data': n_data
    }

    return normalisasi
