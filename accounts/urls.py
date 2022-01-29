from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('account/', profile_view, name="profile"),


    # reset password urls
    # reset password page: enter email for sending reset password url
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset-password/password-reset.html"), name="reset_password"),

    # email sent message page: it will show a message that email has been sent
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="reset-password/password-reset-done.html"), name="password_reset_done"),

    # main reset password page: enter old and new pass and confirm it
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset-password/password-reset-confirm.html"), name="password_reset_confirm"),

    # password reset successfully message: it will show reset password message successfully
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="reset-password/password-reset-complete.html"), name="password_reset_complete"),


    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="change-password/password_change_form.html")),


    path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(template_name="change-password/password-change-done.html"), name="password_change_done"),
]
