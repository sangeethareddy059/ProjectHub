from django.urls import path

from .views import reviews, register, login, forgot_password, project_list, send_message, admin_login, delete_project


urlpatterns = [

    path('reviews/', reviews),
    
    path('projects/', project_list),

    path('register/', register),

    path('login/', login),

    path('forgot-password/', forgot_password),

    path('send-message/', send_message),

    path('admin-login/', admin_login),

    path('projects/<int:id>/', delete_project),

]