from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('check-pin/', views.check_profile_pin_view, name='check-profile-pin'),
    path('enter-profile/', views.enter_profile_view, name='enter-profile'),
    path('session/', views.get_session_info_view, name='session-info')
]