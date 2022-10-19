from rest_framework import serializers
from .models import StudentCoinDetail
class StudentCoinDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentCoinDetail
        fields=[
            'alpha_coin',
            'sigma_coin',
            'xp',
            'level'
        ]