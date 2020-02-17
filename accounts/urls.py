from django.urls import path, include
from .views import logout, login, profile, register
# , password_reset
 
urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    # path('password_reset/', password_reset, name='password_reset'),
]