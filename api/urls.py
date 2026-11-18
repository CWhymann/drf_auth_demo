from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    LoginView,
    ProtectedView,
    ReadOnlyView,
    StaffWriteView,
    NoteDetailView,
    NoteListView,
    RegisterView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("token/", obtain_auth_token, name="api-token-auth"),
    path("register/", RegisterView.as_view(), name="register"),
    path("protected/", ProtectedView.as_view(), name="protected"),
    path("readonly/", ReadOnlyView.as_view(), name="readonly"),
    path("staff/", StaffWriteView.as_view(), name="staff"),
    path("notes/", NoteListView.as_view(), name="note-list"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
]