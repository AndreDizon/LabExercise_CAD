from django.contrib import admin
from django.urls import path
from salesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    
    # Updated paths for Lab 2
    path('login/', views.login_view, name='login'),
    path('users/', views.user_list_view, name='user_list'),
]