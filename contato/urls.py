from django.urls import path
from .views import landpage, painel_mensagens
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', landpage, name='landpage'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="landpage"), name="logout"),
    path("painel/", painel_mensagens, name="painel"),
]