from  django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('destinations', views.destinations, name='destinations'),
    path('packages', views.packages, name='packages'),
    path('northindia',views.northindia,name='northindia'),
    path('southindia',views.southindia,name='southindia'),
    path('eastindia',views.eastindia,name='eastindia'),
    path('westindia',views.westindia,name='westindia'),
    path('kashmirbook',views.kashmirbook,name='kashmirbook'),
    path('keralabook', views.keralabook, name='keralabook'),
    path('biharbook',views.biharbook,name='biharbook'),
    path('rajasthanbook',views.rajasthanbook,name='rajasthanbook'),
    path('punjabbook', views.punjabbook, name='punjabbook'),
    path('himachalpradeshbook', views.himachalpradeshbook, name='himachalpradeshbook'),
    path('delhibook', views.delhibook, name='delhibook'),
    path('andhrapradeshbook', views.andhrapradeshbook, name='andhrapradeshbook'),
    path('karnatakabook', views.karnatakabook, name='karnatakabook'),
    path('tamilnadubook', views.tamilnadubook, name='tamilnadubook'),
    path('jharkhandbook', views.jharkhandbook, name='jharkhandbook'),
    path('orissabook', views.orissabook, name='orissabook'),
    path('westbengalbook', views.westbengalbook, name='westbengalbook'),
    path('gujaratbook', views.gujaratbook, name='gujaratbook'),
    path('maharashtrabook', views.maharashtrabook, name='maharashtrabook'),
    path('madhyapradeshbook', views.madhyapradeshbook, name='madhyapradeshbook'),

]