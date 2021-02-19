from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_view, name='admin_product'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register_view, name='register'),
    path('product', views.all_products, name='all_products'),
    path('add_product', views.add_product, name='add_product'),
    path('add_tags', views.add_tags, name='add_tags'),
    path('add_storage/<int:id>', views.add_storage, name='add_storage'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('delete_image/<int:id>', views.delete_image, name='delete_image'),
    path('add_banner/', views.add_banner, name='add_banner'),
]