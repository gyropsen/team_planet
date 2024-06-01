from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # Базовый функционал пользователя
    # path("login/", login, name="login"),
]
