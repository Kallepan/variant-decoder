from django.urls import path

from .views import TranscriptView, ValidateGDNAView

urlpatterns = [
    path('transcript/', TranscriptView.as_view()),
    path('validate-gdna/', ValidateGDNAView.as_view()),
]