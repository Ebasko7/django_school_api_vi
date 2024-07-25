from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class All_students(APIView):
    def get(self, request):
        students = StudentSerializer(Student.objects.order_by('id'), many=True)
        return Response(students.data)

# Create your views here.
