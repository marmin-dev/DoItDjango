from django.contrib import admin
from django.urls import path,include
from pybo.views import base_views
from common import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/',include('common.urls')),
    path('',base_views.index, name='index'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
