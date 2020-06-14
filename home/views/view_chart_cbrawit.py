from django.http import JsonResponse
from django.views.generic import ListView

from home.models import DataDenormalisasiCbRawit


class IndexView(ListView):
    model = DataDenormalisasiCbRawit
    template_name = 'proses_chart_cbrawit.html'


def get_chart(request):

    db = DataDenormalisasiCbRawit.objects.all()

    labels = []
    data1 = []
    data2 = []

    for x in db:
        labels.append(x.bulan)
        data1.append(x.denormalisasi)
        data2.append(x.hasil)

    return JsonResponse(data={
        'labels': labels,
        'data1': data1,
        'data2': data2
    })
