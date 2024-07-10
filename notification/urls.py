from django.urls import path
from .views import ChatView

app_name = "notifications"

urlpatterns = [path("notifications", ChatView.as_view(), name="notifications")]