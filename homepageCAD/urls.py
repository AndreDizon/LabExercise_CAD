from django.contrib import admin
from django.urls import path
from salesapp import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Homepage: http://127.0.0.1:8000/
    path('', views.homepage, name='home'),
    
    # Login: http://127.0.0.1:8000/login/
    path('login/', views.login_view, name='login'),
    
    # About Us: http://127.0.0.1:8000/about/
    path('about/', views.about_view, name='about'),
    
    # Contact Us: http://127.0.0.1:8000/contact/
    path('contact/', views.contact_view, name='contact'),
]