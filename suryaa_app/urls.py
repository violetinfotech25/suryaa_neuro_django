from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'suryaa_app'  # Namespace for this app’s URLs

urlpatterns = [
   path('', views.index, name='home'),
   path('about/', views.about, name='about'),
   path('appoinment/', views.appoinment, name='appoinment'),
   path('blogsidebar/', views.blogsidebar, name='blogsidebar'),
   path('blogsingle/', views.blogsingle, name='blogsingle'),
   path('confirmation/', views.confirmation, name='confirmation'),
   path('contact/', views.contact, name='contact'),
   path('departmentsingle/', views.departmentsingle, name='departmentsingle'),
   path('department/', views.department, name='department'),
   path('doctorsingle/', views.doctorsingle, name='doctorsingle'),
   path('doctor/', views.doctor, name='doctor'),
   path('service/', views.service, name='service'),
   path('service/<slug:slug>/', views.service_detail, name='service_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)