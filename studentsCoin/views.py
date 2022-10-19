import imp
from .models import StudentCoinDetail
from rest_framework import generics
from .serializers import StudentCoinDetailSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class StudentCoinDetailApiView(generics.RetrieveAPIView):
        queryset=StudentCoinDetail.objects.all()
        serializer_class=StudentCoinDetailSerializer
        authentication_classes=[TokenAuthentication]
        permission_classes=[IsAuthenticated]
        lookup_field = 'student_professional_detail_id'