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
from home.views import view_data, view_normalisasi, view_cbmerah, vnormalisasi_cbmerah

app_name = 'home'

urlpatterns = [
    path('data/', view_data.IndexView.as_view(), name='home_view'),
    path('cabairawit/<int:pk>/', view_data.DataDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', view_data.edit, name='edit'),
    path('create/', view_data.create, name='create'),
    path('delete/<int:pk>/', view_data.delete, name='delete'),
    path('datacbrawit/', view_data.DataView.as_view(), name='data_cbrawit'),

    path('cbMerah/', view_cbmerah.IndexView.as_view(), name='homeview_cbmerah'),
    path('cabaimerah/<int:pk>/', view_cbmerah.DataDetailView.as_view(), name='detail_cbmerah'),
    path('editCbMerah/<int:pk>/', view_cbmerah.edit, name='edit_cbmerah'),
    path('createCbMerah/', view_cbmerah.create, name='create_cbmerah'),
    path('deleteCbMerah/<int:pk>/', view_cbmerah.delete, name='delete_cbmerah'),
    path('dataCbMerah/', view_cbmerah.DataView.as_view(), name='data_cbmerah'),
    path('normalisasiCbMerah/', vnormalisasi_cbmerah.IndexView.as_view(), name='normalisasi_cbmerah'),

    path('normalisasi/', view_normalisasi.IndexView.as_view(), name='home_normalisasi'),
]
