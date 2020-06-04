from django.views.generic import ListView

from home.models import DataDenormalisasiCbRawit


class IndexView(ListView):
    template_name = 'proses_denormalisasi_cbrawit.html'
    context_object_name = 'data'

    def get_queryset(self):

        data_denormalisasi = []
        db = DataDenormalisasiCbRawit.objects.all()

        for i, x in enumerate(db):
            d = {
                'no': x.no,
                'denormalisasi': x.denormalisasi,
                'hasil': x.hasil
            }
            data_denormalisasi.append(d)

        context = {
            'data_denormalisasi': data_denormalisasi
        }

        return context
