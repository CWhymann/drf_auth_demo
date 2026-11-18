from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsStaffOrReadOnly, IsOwner
from .models import Note
from .serializers import NoteSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response(
                {"message": "Login successful", "user_id": user.id},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})


class ReadOnlyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({"message": "Anyone can read this"})

    def post(self, request):
        return Response({"message": "Only authenticated users can write this"})


class StaffWriteView(APIView):
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        return Response({"message": "Anyone can read this"})

    def post(self, request):
        return Response({"message": "Staff users can write here"})


class NoteDetailView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]


class NoteListView(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)