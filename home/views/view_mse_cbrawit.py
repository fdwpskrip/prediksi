from django.views.generic import ListView

from home.models import DataMseCbRawit


class IndexView(ListView):
    template_name = 'proses_mse_cbrawit.html'
    context_object_name = 'data'

    def get_queryset(self):

        data_mse = 0
        db = DataMseCbRawit.objects.all()

        if len(db) > 0:
            data_mse = db[0].mse

        context = {
            'data_mse': data_mse
        }

        return context
