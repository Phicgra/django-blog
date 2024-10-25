from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('allposts/<str:pd>', views.allposts, name='allposts'),

    
]
