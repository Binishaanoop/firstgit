from django.urls import path
from . import views
urlpatterns = [
   path('',views.fnavbar,name='fnavbar')
   path('',views.register,name='register')
]