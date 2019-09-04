from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
url(r'hello',views.hello,name='hello'),
url(r'upload',views.model_form_upload,name='upload'),
url(r'index',views.index1,name='index'),
url(r'display',views.Display_Image,name='display'),
url(r'register',views.Register,name='register'),
url(r'trainer',views.trainerRegistration,name='trainer_register'),
url(r'login',views.trainerLogin,name='login'),
]