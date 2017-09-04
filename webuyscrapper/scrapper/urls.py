from django.conf.urls import url

from .views import getInfoCsv

urlpatterns = [
    url(r'productsCsv/$', getInfoCsv.as_view(), name='products_csv')
]
