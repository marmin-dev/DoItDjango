from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


# app_name = 'common'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
        template_name='common/login.html'
    ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/', include('allauth.urls')),

]
