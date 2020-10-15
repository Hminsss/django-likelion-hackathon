from django.urls import path
from . import views

urlpatterns = [
   path('custom_voice', views.custom_voice, name="custom_voice"),
   path('custom_voice_new', views.custom_voice_new, name="custom_voice_new"),
   path('custom_voice_detail', views.custom_voice_detail, name="custom_voice_detail"),
]
