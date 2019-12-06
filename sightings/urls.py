from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
        path('',views.sightings_list,name='sightings'),
        path('<str:Unique_Squirrel_ID>',views.update,name='update'),
        path('add/', views.add, name='add'),
        path('stats/',views.stats,name='stats')
        ]