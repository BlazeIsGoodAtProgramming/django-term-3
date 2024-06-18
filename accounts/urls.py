from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_user, name='signup'),
    path('change_password/', change_password, name='change_password'),
    path('reset_password/', reset_password, name='reset_password'),
    path('reset_password_done/', reset_password_done, name='reset_password_done'),
    path('reset_password_confirm/', reset_password_confirm, name='reset_password_confirm'),
    path('reset_password_complete/', reset_password_complete, name='reset_password_complete'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
