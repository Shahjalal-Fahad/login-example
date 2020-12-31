from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home, name="home"),
    path('register/',register, name="register"),
    path('login/',login, name="login"),
    path('logout/',logout, name="logout"),
    # reset password part
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    # change password
    # path('change-password/',auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    path('change-password/',auth_views.PasswordChangeView.as_view(),
    ),
]
