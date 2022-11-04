from django.urls import path
from home.api.views.register import RegisterView
from home.api.views.login import LoginView

urlpatterns = [
    path('login/', LoginView),
    path('register/', RegisterView)
]