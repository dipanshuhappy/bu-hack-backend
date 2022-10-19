from .models import StudentProfessionalDetails
from rest_framework import generics
from .serializers import StudentProfessionalDetailSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError
class StudentDetailApiView(generics.RetrieveAPIView):
        queryset=StudentProfessionalDetails.objects.all()
        serializer_class=StudentProfessionalDetailSerializer
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
        
