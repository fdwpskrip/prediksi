from home.models import DataNormalisasiCbRawit, DataNormalisasiCbMerah, DataWeightCbRawit, DataWeightCbMerah, \
    DataBiasCbRawit, DataBiasCbMerah


def get_data_testing(datatype):

    data_normalisasi = get_normalisasi(datatype)
    data_normalisasi_x = data_normalisasi['data_normalisasi_x']
    data_normalisasi_y = data_normalisasi['data_normalisasi_y']

    data_w_transpose = get_w_transpose(datatype)

    data_testing = {
        'data_normalisasi_x': data_normalisasi_x,
        'data_normalisasi_y': data_normalisasi_y,
        'data_w_transpose': data_w_transpose,
    }

    return data_testing


def get_normalisasi(datatype):

    data = {
        'cbrawit': DataNormalisasiCbRawit.objects.all(),
        'cbmerah': DataNormalisasiCbMerah.objects.all()
    }

    data_normalisasi_x = []
    data_normalisasi_y = []

    for x in data.get(datatype):
        data_x = {
            'no': x.no,
            'harga': x.harga,
            'produksi': x.produksi,
            'ketersediaan': x.ketersediaan
        }

        data_y = [float(x.permintaan)]

        data_normalisasi_x.append(data_x)
        data_normalisasi_y.append(data_y)

    data_testing = {
        'data_normalisasi_x': data_normalisasi_x,
        'data_normalisasi_y': data_normalisasi_y
    }

    return data_testing


def get_w_transpose(datatype):

    data = {
        'cbrawit': DataWeightCbRawit.objects.all(),
        'cbmerah': DataWeightCbMerah.objects.all()
    }

    data_harga = []
    data_produksi = []
    data_ketersediaan = []

    for x in data.get(datatype):
        data_harga.append(x.harga)
        data_produksi.append(x.produksi)
        data_ketersediaan.append(x.ketersediaan)

    data_weight_transpose = [data_harga, data_produksi, data_ketersediaan]

    return data_weight_transpose


def get_bias(datatype):

    data = {
        'cbrawit': DataBiasCbRawit.objects.all(),
        'cbmerah': DataBiasCbMerah.objects.all()
    }

    data_bias = []

    for x in data.get(datatype):
        data_bias.append(x)

    return data_bias