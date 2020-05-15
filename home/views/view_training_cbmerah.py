from django.shortcuts import render
from django.views.generic import ListView
from home.views import training
from home.forms import TrainingForm


class IndexView(ListView):
    template_name = 'proses_training_cbmerah.html'
    context_object_name = 'data'

    def get_queryset(self):

        form = TrainingForm()

        context = {
            'data_x_training': [],
            'data_y_training': [],
            'hidden_neuron': 0,
            'data_weight': [],
            'data_bias': [],
            'data_weight_transpose': [],
            'data_h_init': [],
            'data_h_eks': [],
            'data_h_transpose': [],
            'data_matriks_h': [],
            'data_matriks_inv': [],
            'data_matriks_mp': [],
            'data_output_weight': [],
            'rasio_data_training': '(otomatis terisi jumlah data training)',
            'rasio_data_testing': '(otomatis terisi jumlah data testing)',
            'display': 'none',
            'form': form
        }

        return context

    # def training(self, request):
    #     return render(request, self.template_name, {'form': form})

    # Handle POST HTTP requests
    def post(self, request, *args, **kwargs):
        form = TrainingForm(request.POST)

        if form.is_valid():
            hidden_neuron = form.cleaned_data['hidden_neuron']
            rasio_data = form.cleaned_data['rasio_data']

            data_training = training.calculate_hinit(int(hidden_neuron), rasio_data)

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
                'data_output_weight': data_training['data_output_weight'],
                'rasio_data_training': data_training['rasio_data_training'],
                'rasio_data_testing': data_training['rasio_data_testing'],
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
        else:
            context = {
                'data_x_training': [],
                'data_y_training': [],
                'hidden_neuron': 0,
                'data_weight': [],
                'data_bias': [],
                'data_weight_transpose': [],
                'data_h_init': [],
                'data_h_eks': [],
                'data_h_transpose': [],
                'data_matriks_h': [],
                'data_matriks_inv': [],
                'data_matriks_mp': [],
                'data_output_weight': [],
                'rasio_data_training': '(otomatis terisi jumlah data training)',
                'rasio_data_testing': '(otomatis terisi jumlah data testing)',
                'display': 'none',
                'form': form
            }

            return render(request, self.template_name, {self.context_object_name: context})
