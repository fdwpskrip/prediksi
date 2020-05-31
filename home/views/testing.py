from home.models import DataNormalisasiCbRawit, DataNormalisasiCbMerah


def get_normalisasi(datatype):

    # Data
    data = {
        'cbrawit': DataNormalisasiCbRawit.objects.all(),
        'cbmerah': DataNormalisasiCbMerah.objects.all()
    }

    data_normalisasi = []

    for x in data.get(datatype):
        data = {
            'no': x.no,
            'harga': x.harga,
            'produksi': x.produksi,
            'ketersediaan': x.ketersediaan,
            'permintaan': x.permintaan
        }
        data_normalisasi.append(data)

