from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name='index' ),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('recent_works/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('joinus/',views.joinus,name='joinus'),
    path('request_services/',views.booking,name='booking'),

]     