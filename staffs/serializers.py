from rest_framework import serializers
from .models import StaffProfessionalDetails
class StaffProfessionalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffProfessionalDetails
        fields=[
            'bennett_email',
            'first_name',
            'last_name',
            'faculty_id',
            'designation',
            'cabin_number',
            'intercom',
            'school_code',
            'department_code',
            'phd_date',
            'phd_institution',
            'favourite_courses',
            'batch_mentor',
            'status'
        ]