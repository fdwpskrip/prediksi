from home.views import normalisasi
import logging
import math
import numpy as np

logger = logging.getLogger(__name__)


def calculate_hinit():

    # Normalisasi
    data_x_training = get_normalisasi()['data_x_training']
    data_y_training = get_normalisasi()['data_y_training']

    # Jumlah Hidden Neuron
    hidden_neuron = 3

    # Weight
    data_weight = get_weight()

    # Bias
    data_bias = get_bias()

    # Weight Transpose
    data_weight_transpose = get_w_transpose(data_weight)

    # H-Init
    data_h_init = get_h_init(data_x_training, data_bias, data_weight_transpose)

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
        'data_output_weight': data_output_weight
    }

    return data_training


# Normalisasi
def get_normalisasi():
    data = normalisasi.getnormalisasi_cbrawit()
    data_normalisasi = data['n_data']

    data_x = []
    data_y = []
    data_x_training = []
    data_y_training = []
    data_training_len = 7

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
    if len(data_normalisasi) >= 10:
        for i in range(data_training_len):
            data_x_training.append(data_x[i])
            data_y_training.append(data_y[i])

    data_n = {
        'data_x_training': data_x_training,
        'data_y_training': data_y_training,
    }

    return data_n


# Set Nilai Weight
def get_weight():
    weight_1 = {
        'harga': 0.061770227,
        'produksi': 0.052824088,
        'ketersediaan': 0.157952941
    }
    weight_2 = {
        'harga': 0.179735009,
        'produksi': 0.59817741,
        'ketersediaan': 0.008778016
    }
    weight_3 = {
        'harga': 0.731199281,
        'produksi': 0.386755785,
        'ketersediaan': 0.361700354
    }

    data_weight = [weight_1, weight_2, weight_3]

    return data_weight


# Set Nilai Bias
def get_bias():
    data_bias = [0.195826602, 0.248667800, 0.07703571]
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
def get_h_init(data_x_training, data_bias, data_weight_transpose):

    data_h_init = []
    hidden_neuron = 3

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

    logger.error(data_y_training)

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
