from email.policy import default
from rest_framework import serializers
from .models import SigmaTransaction
class SigmaTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=SigmaTransaction
        fields=[
            'id',
            'sender_id',
            'receiver_id',
            'amount',
            'current_timestamp'
        ]
TIME_PERIOD_CHOICES=(
    "week",
    "month"
)
class SigmaTransactionListQuerySerializer(serializers.Serializer):
    sender_id = serializers.EmailField(allow_blank=True,required=False)
    receiver_id = serializers.EmailField(allow_blank=True,required=False)
    latest = serializers.BooleanField(default=False,required=False)
    time_period = serializers.ChoiceField(choices=TIME_PERIOD_CHOICES,required=False)
    def validate(self, data):
        if not(bool(data.get("sender_id")) or bool(data.get("receiver_id"))) or (bool(data.get("sender_id")) and bool(data.get("receiver_id"))):
            raise serializers.ValidationError("Need only one receiver or sender id")
        if data.get("sender_id")==data.get("receiver_id"):
            raise serializers.ValidationError("Both sender and reciever can't be the same")
        if not bool(data.get("latest")) and not bool(data.get("time_period")):
            raise serializers.ValidationError("Need at least latest or time_period field")
        return data
class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField();
    remark = serializers.CharField(max_length = 255)
    sender_id = serializers.EmailField()
# class SigmaRequestTransactionSerializer(serializers.ModelSerializer):
#     def validate(self, attrs):
#         if(not is_sender_same_batch_with_receiver(attrs["sender_id"],attrs["receiver_id"])):
#             raise serializers.ValidationError("You don't have access to request for this batch")
#         return attrs
#     class Meta:
#         //model=SigmaRequestTransaction
#         fields=(
#             'id',
#             'sender_id',
#             'receiver_id',
#             'amount',
#             'message',
#             'file',
#             'current_timestamp'
#         )
# class SigmaRequestTransactionGetSerializer(serializers.ModelSerializer):
#       class Meta:
#         model=SigmaRequestTransaction
#         fields=(
#             'id',
#             'sender_id',
#             'receiver_id',
#             'amount',
#             'message',
#             'file',
#             'is_valid',
#             'current_timestamp'
#         )
# class TransactionResultsQuerySerializer(serializers.Serializer):
#     sender_id = serializers.EmailField(allow_blank=True,required=False)
#     receiver_id = serializers.EmailField(allow_blank=True,required=False)
#     is_valid= serializers.BooleanField(default=False)
#     def validate(self, data):
#         if not(bool(data.get("sender_id")) or bool(data.get("receiver_id"))):
#             raise serializers.ValidationError("Need at least receiver or sender id")
#         return data;
# class VerifyTransactionSerializer(serializers.Serializer):
#     receiver_id=serializers.EmailField()
#     sender_id = serializers.EmailField()
#     id=serializers.IntegerField()
#     def validate(self, attrs):
#         if(not is_sender_same_batch_with_receiver(attrs["sender_id"],attrs["receiver_id"])):
#             raise serializers.ValidationError("You don't have access to request for this batch")
#         return attrs