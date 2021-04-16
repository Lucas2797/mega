"""mega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from products.views import home_view
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from products import views

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('config/', include('config.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('allauth.urls')),
    path('home/', home_view, name='home'),
    path('', (TemplateView.as_view(template_name="admin/sw.js", content_type='application/javascript', extra_context={'name': 'caco'} )), name='sw.js'),
    path('manifest.json/', (TemplateView.as_view(template_name="admin/manifest.json", content_type='application/json', )), name='manifestjson'),
    path('install_sw/', (TemplateView.as_view(template_name="admin/install_sw.html", content_type='text/html', )), name='install_sw'),
    path('test_amp/', views.test_amp_view, name='test_amp'),
    path('test/', views.test_view, name='test'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
