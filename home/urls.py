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
    view_training_cbrawit, view_training_cbmerah, view_testing_cbrawit, view_testing_cbmerah, view_mse_cbmerah, \
    view_mse_cbrawit, view_denormalisasi_cbmerah, view_denormalisasi_cbrawit, view_chart_cbmerah, view_chart_cbrawit, \
    view_data_user

app_name = 'home'

urlpatterns = [
    path('data-user/', view_data_user.IndexView.as_view(), name='data-user'),
    path('detail-user/<int:pk>/', view_data_user.detail, name='detail-user'),
    path('edit-user/<int:pk>/', view_data_user.edit, name='edit-user'),
    path('create-user/', view_data_user.create, name='create-user'),
    path('delete-user/<int:pk>/', view_data_user.delete, name='delete-user'),
    path('logout', view_data_user.logout_view, name='logout'),

    path('dashboard/', view_data_user.dashboard, name='dashboard'),

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
    path('proses-testing-cbrawit/', view_testing_cbrawit.IndexView.as_view(), name='testing_cbrawit'),
    path('proses-testing-cbmerah/', view_testing_cbmerah.IndexView.as_view(), name='testing_cbmerah'),
    path('proses-mse-cbrawit/', view_mse_cbrawit.IndexView.as_view(), name='mse_cbrawit'),
    path('proses-mse-cbmerah/', view_mse_cbmerah.IndexView.as_view(), name='mse_cbmerah'),
    path('proses-denormalisasi-cbrawit/', view_denormalisasi_cbrawit.IndexView.as_view(), name='denormalisasi_cbrawit'),
    path('proses-denormalisasi-cbmerah/', view_denormalisasi_cbmerah.IndexView.as_view(), name='denormalisasi_cbmerah'),
    path('proses-chart-cbmerah/', view_chart_cbmerah.IndexView.as_view(), name='chart_cbmerah'),
    path('proses-chart-cbrawit/', view_chart_cbrawit.IndexView.as_view(), name='chart_cbrawit'),
    path('proses-data-chart-cbmerah/', view_chart_cbmerah.get_chart, name='data_chart_cbmerah'),
    path('proses-data-chart-cbrawit/', view_chart_cbrawit.get_chart, name='data_chart_cbrawit'),
]
