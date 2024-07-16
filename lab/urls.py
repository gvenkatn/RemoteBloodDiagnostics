from django.urls import path
from .views import Dashboard, OrderDetails, upload_file
from django.utils.timezone import datetime

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>', OrderDetails.as_view(), name='order-details'),
    path ('orders/list/', upload_file, name='list'),
]