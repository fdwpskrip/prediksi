from django.shortcuts import render
from django.views.generic import ListView

from home.views import testing


class IndexView(ListView):
    template_name = 'proses_testing_cbmerah.html'
    context_object_name = 'data'

    def get_queryset(self):

        context = {
            'data_normalisasi_x': [],
            'data_normalisasi_y': [],
            'hidden_neuron': 0,
            'data_w_transpose': [],
            'data_bias': [],
            'data_h_init': [],
            'data_h_eks': [],
            'data_prediksi_y': [],
            'display': 'none'
        }

        return context

    # Handle POST HTTP requests
    def post(self, request, *args, **kwargs):

        data_testing = testing.get_data_testing('cbmerah', 'testing')

        data_normalisasi_x = data_testing['data_normalisasi_x']
        data_normalisasi_y = data_testing['data_normalisasi_y']
        hidden_neuron = data_testing['hidden_neuron']
        data_w_transpose = data_testing['data_w_transpose']
        data_bias = data_testing['data_bias']
        data_h_init = data_testing['data_h_init']
        data_h_eks = data_testing['data_h_eks']
        data_prediksi_y = data_testing['data_prediksi_y']

        context = {
            'data_normalisasi_x': data_normalisasi_x,
            'data_normalisasi_y': data_normalisasi_y,
            'hidden_neuron': hidden_neuron,
            'data_w_transpose': data_w_transpose,
            'data_bias': data_bias,
            'data_h_init': data_h_init,
            'data_h_eks': data_h_eks,
            'data_prediksi_y': data_prediksi_y,
            'display': 'block'
        }

        return render(request, self.template_name, {self.context_object_name: context})
