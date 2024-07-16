"""
URL configuration for diagnostic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from patient.views import Index, About, Order, OrderConfirmation, OrderPayConfirmation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('lab/',include('lab.urls')),
    path('', Index.as_view(), name = 'Index'),
    path('about/', About.as_view(), name = 'About'),
    path('order/', Order.as_view(), name = 'Order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name = 'Order-Confirmation'),
    path('order-pay-confirmation/<int:pk>', OrderPayConfirmation.as_view(), name = 'Order-Pay-Confirmation'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
