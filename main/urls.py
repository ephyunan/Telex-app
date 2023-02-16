from django.urls import include, path
from main.views import TutorRegistrationView, StudentRegistrationView

urlpatterns = [
    
    path('registration/tutor/', TutorRegistrationView.as_view(), name='register-tutor'),
    path('registration/student/', StudentRegistrationView.as_view(), name='register-student'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]