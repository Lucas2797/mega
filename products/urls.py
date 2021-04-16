from django.urls import path
from . import views


urlpatterns = [
    #FRONT#
    path('home/', views.home_view, name='home_product'),
    path('list/', views.list_view, name='list_product'),
    path('list/<str:tag>/', views.list_view1, name='list_product1'),
    path('detail/<int:id>', views.detail_view, name='detail_product'),
    path('contact/', views.contact_view, name='contact'),
    path('chat/', views.chat_view, name='chat'),
    path('company/', views.company_view, name='company'),
    path('suport/', views.suport_view, name='suport'),
    path('search/', views.search_view, name='search'),
    path('test/', views.test_view, name='test'),
]
