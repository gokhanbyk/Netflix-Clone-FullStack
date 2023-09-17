from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
    path('profile/', profile_request, name='profile_page'),
    path('profile-yonetimi/', profile_manage, name='yonetim'),
    path('change-pass/', change_pass, name='change'),
    path('hesap-ayarlari/', hesap_ayarlari, name='hesap'),
]
