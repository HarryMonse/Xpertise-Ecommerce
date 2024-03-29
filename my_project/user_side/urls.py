from django.urls import path
from user_side import views


urlpatterns = [
    path('user_login/',views.signin,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path("", views.index, name="index"),
    path('user_login/', views.user_login, name='user_login'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('enter_otp/',views.enter_otp,name='enter_otp'),
    path('resend_otp/',views.resend_otp,name='resend_otp'),
    path('services/', views.services, name='services'),
    path('service/<int:category_id>/<int:service_id>', views.service_details, name='service_details'),
    path('search/',views.search,name='search'),
    path('add_to_cart/',views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_list, name='cart'),
    path('update_qty',views.qty_update,name='update_qty'),
    path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('user_account/', views.user_account, name='user_account'),
    path('add_address/', views.add_address, name='add_address'),
    path('edit-address/<int:address_id>/', views.edit_address, name='edit_address'),
    path('delete-address/<int:address_id>/', views.delete_address, name='delete_address'),
    path('order_items/<int:order_number>/', views.order_items, name='order_items'),
    path('cancell/<int:order_number>/',views.cancell,name='cancell'),
    path('change_password/', views.change_password, name='change_password'),
    path('add_wishlist/<int:service_id>/',views.add_wishlist,name='add_wishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('delete_wishlist/<int:wishlist_item_id>/',views.delete_wishlist,name='delete_wishlist'),
    path('filter-service/', views.filter_service,name='filter-service'),
















]