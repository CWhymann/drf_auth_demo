from django.urls import path
from .views import LoginView, ProtectedView, ReadOnlyView, StaffWriteView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("protected/", ProtectedView.as_view(), name="protected"),
    path("readonly/", ReadOnlyView.as_view(), name="readonly"),
    path("staff/", StaffWriteView.as_view(), name="staff"),
]