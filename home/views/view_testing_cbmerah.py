from django.views.generic import ListView

from home.views import testing


class IndexView(ListView):
    template_name = 'proses_testing_cbmerah.html'
    context_object_name = 'data'

    def get_queryset(self):

        data_normalisasi = testing.get_data_testing('cbmerah')
        data_normalisasi_x = data_normalisasi['data_normalisasi_x']
        data_normalisasi_y = data_normalisasi['data_normalisasi_y']
        data_w_transpose = data_normalisasi['data_w_transpose']

        context = {
            'data_normalisasi_x': data_normalisasi_x,
            'data_normalisasi_y': data_normalisasi_y,
            'data_w_transpose': data_w_transpose,
            'display': 'block',
        }

        return context

