from rest_framework import serializers
from .models import StudentProfessionalDetails
class StudentProfessionalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentProfessionalDetails
        fields=[
            'id',
            'bennett_email',
            'first_name',
            'last_name',
            'enrollment_number',
            'school_code',
            'department_code',
            'batch',
            'program',
            'current_semester'
        ]