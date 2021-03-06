from django.http import JsonResponse
from django.views.generic import ListView

from home.models import DataDenormalisasiCbMerah


class IndexView(ListView):
    model = DataDenormalisasiCbMerah
    template_name = 'proses_chart_cbmerah.html'


def get_chart(request):

    db = DataDenormalisasiCbMerah.objects.all()

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
