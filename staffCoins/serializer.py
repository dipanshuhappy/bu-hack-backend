from rest_framework import serializers
from .models import StaffCoinDetails
class StaffCoinDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffCoinDetails
        fields=[
            'sigma_coin',
        ]