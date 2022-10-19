from rest_framework import generics
from .models import StaffCoinDetails
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import StaffCoinDetailSerializer
class StaffCoinDetailApiView(generics.RetrieveAPIView):
        queryset=StaffCoinDetails.objects.all()
        serializer_class=StaffCoinDetailSerializer
        authentication_classes=[TokenAuthentication]
        permission_classes=[IsAuthenticated]
        lookup_field = 'staff_professional_detail_id'