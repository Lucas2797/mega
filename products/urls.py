from django.urls import path
from . import views


urlpatterns = [
    #FRONT#
    path('home/', views.amp_home, name='home_product'),
    path('list/', views.list_view, name='list_product'),
    path('detail/<int:id>', views.detail_view, name='detail_product'),
    path('contact/', views.contact_view, name='contact'),
    path('chat/', views.chat_view, name='chat'),
    path('company/', views.company_view, name='company'),
    path('suport/', views.suport_view, name='suport'),
    path('search/', views.search_view, name='search'),
]
