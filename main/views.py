from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from main.serializers import (
    TutorCustomRegistrationSerializer, StudentCustomRegistrationSerializer
    )

class TutorRegistrationView(RegisterView):
    serializer_class = TutorCustomRegistrationSerializer


class StudentRegistrationView(RegisterView):
    serializer_class = StudentCustomRegistrationSerializer