from django.urls import path
from .views import RegisterView

urlpatterns = [
    # API Auth
    path('register/', RegisterView.as_view())
]
