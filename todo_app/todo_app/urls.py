"""todo_app URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
# from ..users import views as user_view
# from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html'),
         name='login'),
    path('user/', include('users.urls')),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', user_view.register, name='register'),
]