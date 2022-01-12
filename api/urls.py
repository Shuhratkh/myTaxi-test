from django.urls import path
from .views import createOrder, apiOverview, updateOrder, listOrder, listOrderbyClient

urlpatterns=[
    path('', apiOverview, name='overview'),
    path('create/', createOrder, name='create'),
    path('list/', listOrder, name='list'),
    path('update-status/', updateOrder, name='update'),
    path('orders/clients/<str:client_id>/', listOrderbyClient, name='listbyclient'),
]