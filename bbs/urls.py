"""seoul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import bbs.views

app_name = 'bbs'

urlpatterns = [
    path('selectAll', bbs.views.SelectAll.as_view(), name='selectAll'),
    path('deltail/<int:pk>', bbs.views.Detail.as_view(), name='detail'),
    path('update/<int:pk>', bbs.views.Update.as_view(), name='update'),
    path('delete', bbs.views.delete, name='delete'),
    path('create', bbs.views.Create.as_view(), name='create'),
]
