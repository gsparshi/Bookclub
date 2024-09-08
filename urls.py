"""
URL configuration for typelitproject project.

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
from django.urls import path
from typelitapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookdata',show),
    path('firstpage',homepage),
    path('card',register),
    path('addbook/',addbook),
    path('register',login),
    path('login',login1),
    path('logout',logout1),
    path('vision',vision),
    path('blog',blog),
    path('volunteer',volunteer),
    path('tc',tc),
    path('delete_book/<id>/',deletebook)
  
    
     

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



