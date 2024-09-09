"""
URL configuration for LMSproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls, name='django_admin_page'),
    path('api/v1/admin/', include('admin_page.urls'), name='admin'),
    path('api/v1/authors/', include('authors.urls'), name='authors'),
    path('api/v1/books/', include('books.urls'), name='books'),
    path('api/v1/borrow/', include('borrows.urls'), name='borrow'),
    path('api/v1/login/', include('login.urls'), name='login'),
    path('api/v1/reservation/', include('reservations.urls'), name='reservation'),
    path('api/v1/search/', include('search.urls'), name='search'),
    path('api/v1/profile/', include('user_profile.urls'), name='user_profile'),

]
