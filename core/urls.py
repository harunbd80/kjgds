from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    
    path('menu',views.menu,name='menu'),
    path('boking',views.boking),
    path('team',views.team),
    path('testimonial',views.testimonial),
    path('contact',views.contract,name='contract'),
    path('service',views.service,name='service')
]