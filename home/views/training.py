from home.models import DataNormalisasiCbRawit, DataNormalisasiCbMerah, DataWeightCbRawit, DataWeightCbMerah, \
    DataBiasCbRawit, DataBiasCbMerah, DataOutputWeightCbRawit, DataOutputWeightCbMerah
from home.views import normalisasi
import logging
import math
import random
import numpy as np

logger = logging.getLogger(__name__)


def calculate_hinit(datatype, hidden_neuron, rasio):

    # Data
    data = {
        'cbrawit': normalisasi.getnormalisasi_cbrawit()['n_data'],
        'cbmerah': normalisasi.getnormalisasi_cbmerah()['n_data']
    }

    data_normalisasi = data.get(datatype)
    data_size = len(data_normalisasi)

    rasio_data_training = {
        '-': math.ceil(data_size * 0.5),
        '50:50': math.ceil(data_size * 0.5),
        '60:40': math.ceil(data_size * 0.6),
        '70:30': math.ceil(data_size * 0.7),
        '80:20': math.ceil(data_size * 0.8),
        '90:10': math.ceil(data_size * 0.9),
        '10:90': math.ceil(data_size * 0.1),
        '20:80': math.ceil(data_size * 0.2),
        '30:70': math.ceil(data_size * 0.3),
        '40:60': math.ceil(data_size * 0.4)
    }

    rasio_data_testing = {
        '-': data_size - math.ceil(data_size * 0.5),
        '50:50': data_size - math.ceil(data_size * 0.5),
        '60:40': data_size - math.ceil(data_size * 0.6),
        '70:30': data_size - math.ceil(data_size * 0.7),
        '80:20': data_size - math.ceil(data_size * 0.8),
        '90:10': data_size - math.ceil(data_size * 0.9),
        '10:90': data_size - math.ceil(data_size * 0.1),
        '20:80': data_size - math.ceil(data_size * 0.2),
        '30:70': data_size - math.ceil(data_size * 0.3),
        '40:60': data_size - math.ceil(data_size * 0.4)
    }

    # Normalisasi
    dt_normalisasi = get_normalisasi(data_normalisasi, rasio_data_training.get(rasio), rasio_data_testing.get(rasio))
    data_x_training = dt_normalisasi['data_x_training']
    data_y_training = dt_normalisasi['data_y_training']
    data_x_testing = dt_normalisasi['data_x_testing']
    data_y_testing = dt_normalisasi['data_y_testing']

    # Weight
    data_weight = get_weight(hidden_neuron)

    # Bias
    data_bias = get_bias(hidden_neuron)

    # Weight Transpose
    data_weight_transpose = get_w_transpose(data_weight)

    # H-Init
    data_h_init = get_h_init(hidden_neuron, data_x_training, data_bias, data_weight_transpose)

    # H-Eksponensial
    data_h_eks = get_h_eksponensial(data_h_init)

    # H-Transpose
    data_h_transpose = get_h_transpose(data_h_eks)

    # Matriks H
    data_matriks_h = get_matriks_h(data_h_transpose, data_h_eks)

    # Matriks Invers
    data_matriks_inv = get_matriks_inv(data_matriks_h)

    # Matriks Moore-Penrose
    data_matriks_mp = get_matriks_mp(data_matriks_inv, data_h_transpose)

    # Output Weight
    data_output_weight = get_output_weight(data_matriks_mp, data_y_training)

    # Save to DB
    if datatype == 'cbrawit':
        # Normalisasi
        DataNormalisasiCbRawit.objects.all().delete()
        for i, x in enumerate(data_x_testing):
            db = DataNormalisasiCbRawit()
            db.no = str(i+1)
            db.harga = x['harga']
            db.produksi = x['produksi']
            db.ketersediaan = x['ketersediaan']
            db.permintaan = data_y_testing[i][0]
            db.save()

        # Weight
        DataWeightCbRawit.objects.all().delete()
        for i, x in enumerate(data_weight):
            db = DataWeightCbRawit()
            db.no = str(i + 1)
            db.harga = x['harga']
            db.produksi = x['produksi']
            db.ketersediaan = x['ketersediaan']
            db.save()

        # Bias
        DataBiasCbRawit.objects.all().delete()
        for i, x in enumerate(data_bias):
            db = DataBiasCbRawit()
            db.no = str(i + 1)
            db.bias = x
            db.save()

        # Output Weight
        DataOutputWeightCbRawit.objects.all().delete()
        for i, x in enumerate(data_output_weight):
            db = DataOutputWeightCbRawit()
            db.no = str(i + 1)
            db.weight = x
            db.save()

    if datatype == 'cbmerah':
        # Normalisasi
        DataNormalisasiCbMerah.objects.all().delete()
        for i, x in enumerate(data_x_testing):
            db = DataNormalisasiCbMerah()
            db.no = str(i+1)
            db.harga = x['harga']
            db.produksi = x['produksi']
            db.ketersediaan = x['ketersediaan']
            db.permintaan = data_y_testing[i][0]
            db.save()

        # Weight
        DataWeightCbMerah.objects.all().delete()
        for i, x in enumerate(data_weight):
            db = DataWeightCbMerah()
            db.no = str(i + 1)
            db.harga = x['harga']
            db.produksi = x['produksi']
            db.ketersediaan = x['ketersediaan']
            db.save()

        # Bias
        DataBiasCbMerah.objects.all().delete()
        for i, x in enumerate(data_bias):
            db = DataBiasCbMerah()
            db.no = str(i + 1)
            db.bias = x
            db.save()

        # Output Weight
        DataOutputWeightCbMerah.objects.all().delete()
        for i, x in enumerate(data_output_weight):
            db = DataOutputWeightCbMerah()
            db.no = str(i + 1)
            db.weight = x
            db.save()

    data_training = {
        'data_x_training': data_x_training,
        'data_y_training': data_y_training,
        'hidden_neuron': hidden_neuron,
        'data_weight': data_weight,
        'data_bias': data_bias,
        'data_weight_transpose': data_weight_transpose,
        'data_h_init': data_h_init,
        'data_h_eks': data_h_eks,
        'data_h_transpose': data_h_transpose,
        'data_matriks_h': data_matriks_h,
        'data_matriks_inv': data_matriks_inv,
        'data_matriks_mp': data_matriks_mp,
        'data_output_weight': data_output_weight,
        'rasio_data_training': rasio_data_training.get(rasio),
        'rasio_data_testing': rasio_data_testing.get(rasio)
    }

    return data_training


# Normalisasi
def get_normalisasi(data_normalisasi, rasio_training, rasio_testing):

    data_x = []
    data_y = []
    data_training_len = rasio_training
    data_testing_len = rasio_testing

    for dt in data_normalisasi:
        x = {
            'harga': dt['harga'],
            'produksi': dt['produksi'],
            'ketersediaan': dt['ketersediaan']
        }

        # y = {
        #     'permintaan': dt['permintaan']
        # }

        y = [float(dt['permintaan'])]

        data_x.append(x)
        data_y.append(y)

    # Data Normalisasi
    data_x_training = data_x[:data_training_len]
    data_y_training = data_y[:data_training_len]

    data_x_testing = data_x[-data_testing_len:]
    data_y_testing = data_y[-data_testing_len:]

    data_n = {
        'data_x_training': data_x_training,
        'data_y_training': data_y_training,
        'data_x_testing': data_x_testing,
        'data_y_testing': data_y_testing
    }

    return data_n


# Set Nilai Weight
def get_weight(hidden_neuron):
    # dummy
    # weight_1 = {
    #     'harga': 0.061770227,
    #     'produksi': 0.052824088,
    #     'ketersediaan': 0.157952941
    # }
    # weight_2 = {
    #     'harga': 0.179735009,
    #     'produksi': 0.59817741,
    #     'ketersediaan': 0.008778016
    # }
    # weight_3 = {
    #     'harga': 0.731199281,
    #     'produksi': 0.386755785,
    #     'ketersediaan': 0.361700354
    # }

    data_weight = []

    for i in range(hidden_neuron):
        weight = {
            'harga': random.uniform(-1, 1),
            'produksi': random.uniform(-1, 1),
            'ketersediaan': random.uniform(-1, 1)
        }
        data_weight.append(weight)

    return data_weight


# Set Nilai Bias
def get_bias(hidden_neuron):
    data_bias = []
    for i in range(hidden_neuron):
        bias = random.uniform(-1, 1)
        data_bias.append(bias)

    return data_bias


# W-Transpose
def get_w_transpose(data_weight):
    data_harga = []
    data_produksi = []
    data_ketersediaan = []

    for i in range(len(data_weight)):
        data_harga.append(data_weight[i]['harga'])
        data_produksi.append(data_weight[i]['produksi'])
        data_ketersediaan.append(data_weight[i]['ketersediaan'])

    data_weight_transpose = [data_harga, data_produksi, data_ketersediaan]

    return data_weight_transpose


# H-Init
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


# H-Eksponensial
def get_h_eksponensial(data_h_init):

    data_h_eks = []

    for i, x in enumerate(data_h_init):

        h_eks = []
        for j, y in enumerate(x):

            h = 1 / (1 + math.exp(-1 * y))

            h_eks.append(h)

        data_h_eks.append(h_eks)

    return data_h_eks


# H-Transpose
def get_h_transpose(data_h_eks):

    data_h_transpose = []

    for i, x in enumerate(data_h_eks):

        for j, y in enumerate(x):

            if i == 0:
                h = [y]
                data_h_transpose.append(h)
            else:
                data_h_transpose[j].append(y)

    return data_h_transpose


# Matriks H
def get_matriks_h(data_h_transpose, data_h_eks):

    data_matriks_h = []

    for i, x in enumerate(data_h_transpose):

        sm = []

        for j, y in enumerate(x):

            for k, z in enumerate(data_h_eks[j]):

                m = y * z

                if j == 0:
                    sm.append(m)
                else:
                    sm[k] = sm[k] + m

        data_matriks_h.append(sm)

    return data_matriks_h


# Matriks Invers
def get_matriks_inv(data_matriks_h):
    m = np.array(data_matriks_h)
    m_inv = np.linalg.inv(m)

    return m_inv


# Matriks Moore-Penrose
def get_matriks_mp(data_matriks_inv, data_h_transpose):

    data_matriks_mp = []

    for i, x in enumerate(data_matriks_inv):

        sm = []

        for j, y in enumerate(x):

            for k, z in enumerate(data_h_transpose[j]):

                m = y * z

                if j == 0:
                    sm.append(m)
                else:
                    sm[k] = sm[k] + m

        data_matriks_mp.append(sm)

    return data_matriks_mp


# Output Weight
def get_output_weight(data_matriks_mp, data_y_training):

    data_output_weight = []

    for i, x in enumerate(data_matriks_mp):

        sm = []

        for j, y in enumerate(x):

            for k, z in enumerate(data_y_training[j]):

                m = y * z

                if j == 0:
                    sm.append(m)
                else:
                    sm[k] = sm[k] + m

        data_output_weight.append(sm)

    return data_output_weight
