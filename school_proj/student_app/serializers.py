from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number", "locker_combination", "good_student", 'subjects']

    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        subjects = [subject.name for subject in subjects]
        return subjects


class StudentAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['id']