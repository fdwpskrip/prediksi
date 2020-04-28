from django.views.generic import ListView
from home.views import training


class IndexView(ListView):
    template_name = 'proses_training_cbrawit.html'
    context_object_name = 'data'

    def get_queryset(self):

        data_training = training.calculate_hinit()

        context = {
            'data_x_training': data_training['data_x_training'],
            'data_y_training': data_training['data_y_training'],
            'hidden_neuron': data_training['hidden_neuron'],
            'data_weight': data_training['data_weight'],
            'data_bias': data_training['data_bias'],
            'data_weight_transpose': data_training['data_weight_transpose'],
            'data_h_init': data_training['data_h_init'],
            'data_h_eks': data_training['data_h_eks'],
            'data_h_transpose': data_training['data_h_transpose'],
            'data_matriks_h': data_training['data_matriks_h'],
            'data_matriks_inv': data_training['data_matriks_inv'],
            'data_matriks_mp': data_training['data_matriks_mp'],
            'data_output_weight': data_training['data_output_weight']
        }

        return context
