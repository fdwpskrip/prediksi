from home.views import normalisasi
import logging

logger = logging.getLogger(__name__)


def calculate_hinit():

    # Normalisasi
    data_x_training = get_normalisasi()['data_x_training']
    data_y_training = get_normalisasi()['data_y_training']

    # Weight
    data_weight = get_weight()

    # Bias
    data_bias = get_bias()

    # Weight Transpose
    data_weight_transpose = get_w_transpose()

    data_training = {
        'data_x_training': data_x_training,
        'data_y_training': data_y_training,
        'data_weight': data_weight,
        'data_bias': data_bias,
        'data_weight_transpose': data_weight_transpose
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
        y = {
            'permintaan': dt['permintaan']
        }

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
    bias = {
        '1': 0.195826602,
        '2': 0.248667800,
        '3': 0.07703571
    }

    data_bias = [bias]

    return data_bias


# W-Transpose
def get_w_transpose():
    data_weight = get_weight()
    data_harga = []
    data_produksi = []
    data_ketersediaan = []

    for i in range(len(data_weight)):
        data_harga.append(data_weight[i]['harga'])
        data_produksi.append(data_weight[i]['produksi'])
        data_ketersediaan.append(data_weight[i]['ketersediaan'])

    data_weight_transpose = [data_harga, data_produksi, data_ketersediaan]

    return data_weight_transpose


# H Init
def get_h_init():
    data_x_training = get_normalisasi()['data_x_training']
    data_bias = get_bias()
    data_weight_transpose = get_w_transpose()

    data_h_init = []

    for i, x in enumerate(data_x_training):
        h_init = []
        for j in range(len(data_weight_transpose)):
            wt_1 = 0
            wt_2 = 0
            wt_3 = 0

            if  j == 0:
                wt_1 = float(data_weight_transpose[0]['harga'])
                wt_2 = float(data_weight_transpose[1]['harga'])
                wt_3 = float(data_weight_transpose[1]['harga'])
            if  j == 0:
                wt_1 = float(data_weight_transpose[0]['produksi'])
                wt_2 = float(data_weight_transpose[1]['produksi'])
                wt_3 = float(data_weight_transpose[1]['produksi'])
            if  j == 0:
                wt_1 = float(data_weight_transpose[0]['ketersediaan'])
                wt_2 = float(data_weight_transpose[1]['ketersediaan'])
                wt_3 = float(data_weight_transpose[1]['ketersediaan'])

            x1 = float(x['harga']) * wt_1
            x2 = float(x['produksi']) * wt_2
            x3 = float(x['ketersediaan']) * wt_3
