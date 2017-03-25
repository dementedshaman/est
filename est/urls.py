"""est URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from core import views as core

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    
    # Analise
    url(r'^core/$', core.index, name='index'),
    url(r'^core/new$', core.AvaliationNew.as_view(success_url="/core/"), name='core_new'),
    url(r'^core/view/(?P<id>\w+)$', core.view, name='view'),
    
    # Data
    url(r'^data/view/(?P<id>\w+)$', core.dataView, name='data-view'),
    url(r'^data/edit/(?P<id>\w+)$', core.DataUpdate.as_view(success_url="/view/"), name='data-edit'),


] + static(settings.MEDIA_URL_PROXY, document_root=settings.MEDIA_ROOT)
