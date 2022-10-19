"""buplayBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .authentication  import CustomAuthToken,RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/',include('students.urls')),
    path('api/auth/',CustomAuthToken.as_view()),
    path('api/sign-up',RegisterView.as_view()),
    path('api/studentsCoin/',include('studentsCoin.urls')),
    path('api/staff/',include('staffs.urls')),
    path('api/staffCoin/',include('staffCoins.urls')),
    path('api/transaction/sigma/',include('sigmaCoinTransactions.urls')),
    path('api/transaction/alpha/',include('alphaCoinTransactions.urls'))
]
