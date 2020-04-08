"""ProjectSkripsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from home.views import \
    view_data_cbrawit, view_data_cbmerah, \
    view_normalisasi_cbmerah, view_normalisasi_cbrawit, \
    view_training_cbrawit, view_training_cbmerah

app_name = 'home'

urlpatterns = [
    path('data-cbrawit/', view_data_cbrawit.IndexView.as_view(), name='home_view'),
    path('detail-cbrawit/<int:pk>/', view_data_cbrawit.DataDetailView.as_view(), name='detail'),
    path('edit-cabairawit/<int:pk>/', view_data_cbrawit.edit, name='edit'),
    path('create-cabairawit/', view_data_cbrawit.create, name='create'),
    path('delete-cabairawit/<int:pk>/', view_data_cbrawit.delete, name='delete'),
    path('proses-data-cbrawit/', view_data_cbrawit.DataView.as_view(), name='data_cbrawit'),

    path('data-cbmerah/', view_data_cbmerah.IndexView.as_view(), name='homeview_cbmerah'),
    path('detail-cbmerah/<int:pk>/', view_data_cbmerah.DataDetailView.as_view(), name='detail_cbmerah'),
    path('edit-cbmerah/<int:pk>/', view_data_cbmerah.edit, name='edit_cbmerah'),
    path('create-cbmerah/', view_data_cbmerah.create, name='create_cbmerah'),
    path('delete-cbmerah/<int:pk>/', view_data_cbmerah.delete, name='delete_cbmerah'),
    path('proses-data-cbmerah/', view_data_cbmerah.DataView.as_view(), name='data_cbmerah'),

    path('proses-normalisasi-cbrawit/', view_normalisasi_cbrawit.IndexView.as_view(), name='normalisasi_cbrawit'),
    path('proses-normalisasi-cbmerah/', view_normalisasi_cbmerah.IndexView.as_view(), name='normalisasi_cbmerah'),
    path('proses-training-cbrawit/', view_training_cbrawit.IndexView.as_view(), name='training_cbrawit'),
    path('proses-training-cbmerah/', view_training_cbmerah.IndexView.as_view(), name='training_cbmerah'),
]
