from django.urls import path,include
from . import views

urlpatterns = [
    path('api/tutor/', views.TutorList.as_view()),
   
]