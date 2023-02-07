from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from main.models import Tutor, Student

class TutorCustomRegistrationSerializer(RegisterSerializer):
    tutor = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    area = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(TutorCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'area' : self.validated_data.get('area', ''),
                'address' : self.validated_data.get('address', ''),
                'description': self.validated_data.get('description', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(TutorCustomRegistrationSerializer, self).save(request)
        user.is_tutor = True
        user.save()
        tutor = Tutor(tutor=user, area=self.cleaned_data.get('area'), 
                address=self.cleaned_data.get('address'),
                description=self.cleaned_data.get('description'))
        tutor.save()
        return user


class StudentCustomRegistrationSerializer(RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    country = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(StudentCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'country' : self.validated_data.get('country', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(StudentCustomRegistrationSerializer, self).save(request)
        user.is_student = True
        user.save()
        student = Student(student=user,country=self.cleaned_data.get('country'))
        student.save()
        return user