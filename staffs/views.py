from django.shortcuts import render
from .models import StaffProfessionalDetails
from .serializers import StaffProfessionalDetailSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError
class StaffDetailsApiView(generics.RetrieveAPIView):
        queryset=StaffProfessionalDetails.objects.all()
        serializer_class=StaffProfessionalDetailSerializer
        authentication_classes=[TokenAuthentication]
        permission_classes=[IsAuthenticated]
        lookup_field = 'bennett_email'
        def validate(self):
                try:
                        validate_email(self.kwargs["bennett_email"])
                except Exception:
                        raise ValidationError({"detail":f"{self.kwargs['bennett_email']} is not a valid Email "},code=422)

        def get_queryset(self):
                self.validate()
                return super().get_queryset()
