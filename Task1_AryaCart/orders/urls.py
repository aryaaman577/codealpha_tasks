from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('place-order/', views.place_order, name='place_order'),
    path('confirmation/<str:order_number>/', views.order_confirmation, name='order_confirmation'),
    path('history/', views.order_history, name='order_history'),
    path('detail/<str:order_number>/', views.order_detail, name='order_detail'),
    path('payment/<str:order_number>/', views.payment_gateway, name='payment_gateway'),
    path('process-payment/<str:order_number>/', views.process_payment, name='process_payment'),
]
