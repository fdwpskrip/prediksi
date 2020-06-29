import math

from home.models import DataNormalisasiCbRawit, DataNormalisasiCbMerah, DataWeightCbRawit, DataWeightCbMerah, \
    DataBiasCbRawit, DataBiasCbMerah, DataOutputWeightCbRawit, DataOutputWeightCbMerah, DataMseCbRawit, DataMseCbMerah, \
    DataMinMaxCbRawit, DataMinMaxCbMerah, DataNewMinMaxCbRawit, DataNewMinMaxCbMerah, DataDenormalisasiCbRawit, \
    DataDenormalisasiCbMerah, DataCbRawit, DataCbMerah, DataTestingCbMerah, DataTestingCbRawit
from home.views import normalisasi


def get_data_testing(datatype):

    data_normalisasi = get_normalisasi(datatype)
    data_normalisasi_x = data_normalisasi['data_normalisasi_x']
    data_normalisasi_y = data_normalisasi['data_normalisasi_y']

    # Weight Transpose
    data_w = get_w_transpose(datatype)
    hidden_neuron = data_w['hidden_neuron']
    data_w_transpose = data_w['data_w_transpose']

    # Bias
    data_bias = get_bias(datatype)

    # H-Init
    data_h_init = get_h_init(hidden_neuron, data_normalisasi_x, data_bias, data_w_transpose)

    # H-Eksponensial
    data_h_eks = get_h_eksponensial(data_h_init)

    # Prediksi Y
    data_prediksi_y = get_prediksi_y(datatype, data_h_eks)

    # Denormalisasi
    data_denormalisasi = get_denormalisasi(datatype, data_prediksi_y, data_normalisasi_y)

    print(data_prediksi_y)
    print(data_denormalisasi)

    if datatype == 'cbrawit':
        for i, x in enumerate(data_denormalisasi):
            db = DataTestingCbRawit.objects.filter(no=x['no'])
            if len(db) > 0:
                data_d = db[0]
                data_d.permintaan = x['denormalisasi']
                data_d.save()
    else:
        for i, x in enumerate(data_denormalisasi):
            db = DataTestingCbMerah.objects.filter(no=x['no'])
            if len(db) > 0:
                data_d = db[0]
                data_d.permintaan = x['denormalisasi']
                data_d.save()


def get_normalisasi(datatype):

    if datatype == 'cbrawit':
        listnormalisasi = normalisasi.getnormalisasi_prediksi_cbrawit()['n_data']
    else:
        listnormalisasi = normalisasi.getnormalisasi_prediksi_cbmerah()['n_data']

    data_normalisasi_x = []
    data_normalisasi_y = []

    for x in listnormalisasi:
        data_x = {
            'no': x['no'],
            'harga': x['harga'],
            'produksi': x['produksi'],
            'ketersediaan': x['ketersediaan']
        }
        data_normalisasi_x.append(data_x)

        db = get_data_training(x['no'], datatype)
        if len(db) > 0:
            data_y = {
                'no': db[0].no,
                'bulan': db[0].bulan,
                'tahun': db[0].tahun,
                'permintaan': x['permintaan']
            }
            data_normalisasi_y.append(data_y)

    data_testing = {
        'data_normalisasi_x': data_normalisasi_x,
        'data_normalisasi_y': data_normalisasi_y
    }

    return data_testing


def get_data_training(no, datatype):
    dt = {
        'cbrawit': DataCbRawit.objects.filter(no=no),
        'cbmerah': DataCbMerah.objects.filter(no=no)
    }
    return dt.get(datatype)


def get_w_transpose(datatype):

    data = {
        'cbrawit': DataWeightCbRawit.objects.all(),
        'cbmerah': DataWeightCbMerah.objects.all()
    }

    hidden_neuron = len(data.get(datatype))

    data_harga = []
    data_produksi = []
    data_ketersediaan = []

    for x in data.get(datatype):
        data_harga.append(x.harga)
        data_produksi.append(x.produksi)
        data_ketersediaan.append(x.ketersediaan)

    data_w_transpose = [data_harga, data_produksi, data_ketersediaan]

    data_w = {
        'hidden_neuron': hidden_neuron,
        'data_w_transpose': data_w_transpose
    }

    return data_w


def get_bias(datatype):

    data = {
        'cbrawit': DataBiasCbRawit.objects.all(),
        'cbmerah': DataBiasCbMerah.objects.all()
    }

    data_bias = []

    for x in data.get(datatype):
        data_bias.append(float(x.bias))

    return data_bias


def get_h_init(hidden_neuron, data_x_training, data_bias, data_weight_transpose):

    data_h_init = []

    for i, x in enumerate(data_x_training):

        h_init = []
        for j in range(hidden_neuron):

            wt_1 = float(data_weight_transpose[0][j])
            wt_2 = float(data_weight_transpose[1][j])
            wt_3 = float(data_weight_transpose[2][j])

            x1 = float(x['harga']) * wt_1
            x2 = float(x['produksi']) * wt_2
            x3 = float(x['ketersediaan']) * wt_3

            h = x1 + x2 + x3 + data_bias[j]

            h_init.append(h)

        data_h_init.append(h_init)

    return data_h_init


def get_h_eksponensial(data_h_init):

    data_h_eks = []

    for i, x in enumerate(data_h_init):

        h_eks = []
        for j, y in enumerate(x):

            h = 1 / (1 + math.exp(-1 * y))

            h_eks.append(h)

        data_h_eks.append(h_eks)

    return data_h_eks


def get_prediksi_y(datatype, data_h_eks):

    data = {
        'cbrawit': DataOutputWeightCbRawit.objects.all(),
        'cbmerah': DataOutputWeightCbMerah.objects.all()
    }

    data_output_weight = []

    for x in data.get(datatype):
        data_output_weight.append(float(x.weight))

    data_prediksi_y = []

    for i, x in enumerate(data_h_eks):

        sm = []

        for j, y in enumerate(x):

            for k, z in enumerate(data_output_weight):

                m = y * z

                if j == 0:
                    sm.append(m)
                else:
                    sm[k] = sm[k] + m

        if len(sm) > 0:
            data_prediksi_y.append(sm[0])

    print(data_prediksi_y)

    return data_prediksi_y


def get_denormalisasi(datatype, data_prediksi_y, data_normalisasi_y):

    data_min = 0
    data_max = 0
    data_newmin = 0
    data_newmax = 0
    data_denormalisasi = []

    data_minmax = {
        'cbrawit': DataMinMaxCbRawit.objects.all(),
        'cbmerah': DataMinMaxCbMerah.objects.all()
    }

    data_newminmax = {
        'cbrawit': DataNewMinMaxCbRawit.objects.all(),
        'cbmerah': DataNewMinMaxCbMerah.objects.all()
    }

    if len(data_minmax.get(datatype)) > 1:
        data_min = float(data_minmax.get(datatype)[0].permintaan)
        data_max = float(data_minmax.get(datatype)[1].permintaan)

    if len(data_newminmax.get(datatype)) > 0:
        data_newmin = float(data_newminmax.get(datatype)[0].newmin)
        data_newmax = float(data_newminmax.get(datatype)[0].newmax)

    if data_newmax > 0 and data_newmin > 0:
        for i, x in enumerate(data_prediksi_y):
            n = (((float(x) - data_newmin) / (data_newmax - data_newmin)) * (data_max - data_min)) + data_min

            data = {
                'no': data_normalisasi_y[i]['no'],
                'denormalisasi': str(n)
            }

            data_denormalisasi.append(data)

    return data_denormalisasi
