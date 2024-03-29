from django.urls import path
from .import views

urlpatterns = [
    path('',views.checkout,name='checkout'),
    path('payment/',views.payment,name="payment"),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('online_place_order', views.online_place_order, name='online_place_order'),
    path('place_order/',views.place_order,name="place_order"),
    path('order_success/', views.order_success, name='order_success'),
    path('wallet_place_order', views.wallet_place_order, name='wallet_place_order'),
    path('invoice/<int:order_id>/',views.invoice,name='invoice'),


]
