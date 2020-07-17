from home.models import DataCbRawit, DataTestingCbRawit, DataTestingCbMerah
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


def getnormalisasi_prediksi_cbrawit():
    listdata = DataTestingCbRawit.objects.all()
    listharga = DataTestingCbRawit.objects.values_list('harga', flat=True)
    listproduksi = DataTestingCbRawit.objects.values_list('produksi', flat=True)
    listketersediaan = DataTestingCbRawit.objects.values_list('ketersediaan', flat=True)
    listpermintaan = DataTestingCbRawit.objects.values_list('permintaan', flat=True)

    data_cbrawit = {
        'listdata': listdata,
        'listharga': listharga,
        'listproduksi': listproduksi,
        'listketersediaan': listketersediaan,
        'listpermintaan': listpermintaan
    }

    return getnormalisasi(data_cbrawit)


def getnormalisasi_prediksi_cbmerah():
    listdata = DataTestingCbMerah.objects.all()
    listharga = DataTestingCbMerah.objects.values_list('harga', flat=True)
    listproduksi = DataTestingCbMerah.objects.values_list('produksi', flat=True)
    listketersediaan = DataTestingCbMerah.objects.values_list('ketersediaan', flat=True)
    listpermintaan = DataTestingCbMerah.objects.values_list('permintaan', flat=True)

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

    if len(listharga) > 0:
        minharga = min([int(i) for i in listharga])
        maxharga = max([int(i) for i in listharga])
    else:
        minharga = 0
        maxharga = 0

    if len(listproduksi) > 0:
        minproduksi = min([float(i) for i in listproduksi])
        maxproduksi = max([float(i) for i in listproduksi])
    else:
        minproduksi = 0
        maxproduksi = 0

    if len(listketersediaan) > 0:
        minketersediaan = min([float(i) for i in listketersediaan])
        maxketersediaan = max([float(i) for i in listketersediaan])
    else:
        minketersediaan = 0
        maxketersediaan = 0

    if len(listpermintaan) > 0:
        minpermintaan = min([float(i) for i in listpermintaan])
        maxpermintaan = max([float(i) for i in listpermintaan])
    else:
        minpermintaan = 0
        maxpermintaan = 0

    minvalue = {
        'type': 'Min',
        'harga': minharga,
        'produksi': minproduksi,
        'ketersediaan': minketersediaan,
        'permintaan': minpermintaan
    }

    maxvalue = {
        'type': 'Max',
        'harga': maxharga,
        'produksi': maxproduksi,
        'ketersediaan': maxketersediaan,
        'permintaan': maxpermintaan
    }

    newmin = 0.1
    newmax = 0.9

    n_data_all = []
    n_data = []
    n_harga = []
    n_produksi = []
    n_ketersediaan = []
    n_permintaan = []

    for x in listdata:
        data = {
            'no': x.no,
            'bulan': x.bulan,
            'tahun': x.tahun,
            'harga': x.harga,
            'produksi': x.produksi,
            'ketersediaan': x.ketersediaan,
            'permintaan': x.permintaan
        }
        n_data_all.append(data)

    for x in listdata:
        data = {
            'no': x.no,
            'bulan': x.bulan,
            'tahun': x.tahun,
            'harga': 0,
            'produksi': 0,
            'ketersediaan': 0,
            'permintaan': 0
        }
        n_data.append(data)

    for i, x in enumerate(listharga):
        minmax = maxvalue['harga'] - minvalue['harga']
        if minmax > 0:
            n = (((int(x) - minvalue['harga']) * (newmax - newmin)) / minmax) + newmin
            n_harga.append(n)
            n_data[i]['harga'] = float(n)

    for i, x in enumerate(listproduksi):
        minmax = maxvalue['produksi'] - minvalue['produksi']
        if minmax > 0:
            n = (((float(x) - minvalue['produksi']) * (newmax - newmin)) / minmax) + newmin
            n_produksi.append(n)
            n_data[i]['produksi'] = float(n)

    for i, x in enumerate(listketersediaan):
        minmax = maxvalue['ketersediaan'] - minvalue['ketersediaan']
        if minmax > 0:
            n = (((float(x) - minvalue['ketersediaan']) * (newmax - newmin)) / minmax) + newmin
            n_ketersediaan.append(n)
            n_data[i]['ketersediaan'] = float(n)

    for i, x in enumerate(listpermintaan):
        minmax = maxvalue['permintaan'] - minvalue['permintaan']
        if minmax > 0:
            n = (((float(x) - minvalue['permintaan']) * (newmax - newmin)) / minmax) + newmin
            n_permintaan.append(n)
            n_data[i]['permintaan'] = float(n)

    normalisasi = {
        'listdata': n_data_all,
        'min': minvalue,
        'max': maxvalue,
        'newmin': newmin,
        'newmax': newmax,
        'n_data': n_data
    }

    return normalisasi
