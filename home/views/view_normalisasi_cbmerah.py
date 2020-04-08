from django.views.generic import ListView, DetailView
from home.views import normalisasi
import logging

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'proses_normalisasi_cbmerah.html'
    context_object_name = 'data'

    def get_queryset(self):

        data_normalisasi = normalisasi.getnormalisasi_cbmerah()

        context = {
            'min': data_normalisasi['min'],
            'max': data_normalisasi['max'],
            'newmin': data_normalisasi['newmin'],
            'newmax': data_normalisasi['newmax'],
            'n_data': data_normalisasi['n_data']
        }

        return context

