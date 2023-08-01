
from django.urls import path
from . import views

urlpatterns = [
   path('',views.view),
   path('home1',views.view),
   path('register',views.register),
   path('add',views.add),
   path('registred',views.registred),
   path('mlog',views.ad),
   path('welcome',views.welcome),
   path('a',views.log),
   path('search',views.search),
   path('perfom',views.perfom),
   path('perform',views.perform),
   path('drop',views.delete),
   path('do',views.do),
   path('show',views.show),
    path('ab',views.logs),
    path('get',views.get),
    path('store',views.store),
    path('customer',views.customers), 
    path('welcom',views.wel), 
    path('reg',views.reg),
    path('bill',views.bills),
    path('update',views.update), 
    path('new',views.new), 
    path('view',views.vi),
     path('see',views.see),
      path('es',views.es),
    
    
    
    
]