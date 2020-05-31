from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'proses_testing_cbrawit.html'
    context_object_name = 'data'

    def get_queryset(self):
        context = {

        }

        return context
