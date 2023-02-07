from django.shortcuts import render
from rest_framework.views import APIView
from .models import Tutor
from .serializer import TutorSerializer

from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdminOrReadOnly

class TutorList(APIView):
    def get(self, request, format=None):
        tutor = Tutor.objects.all()
        serializers = TutorSerializer(tutor, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = TutorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)
    