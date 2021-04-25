from django.urls import path, include
from .views import UserRegister, Login, FileVilla

urlpatterns = [
    path('signup', UserRegister.as_view(),  name='registeruser'),
    path('', Login.as_view(),  name='signinuser'),
    path('home', FileVilla.as_view(), name='home'),
    path('home/<str:name>/<str:content_type>', FileVilla.as_view(), name='viewfile'),
]