import datetime
from django.db import models
from staffs.models import StaffProfessionalDetails
from students.models import StudentProfessionalDetails
class SigmaTransaction(models.Model):
    sender_id = models.ForeignKey(StaffProfessionalDetails,to_field="bennett_email",on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(StudentProfessionalDetails,to_field="bennett_email",on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    message = models.CharField(max_length=255,null=True, blank=True)
    current_timestamp=models.DateTimeField(null=True, blank=True, editable=False);
    def save(self, *args, **kwargs):
        self.current_timestamp =datetime.datetime.now()
        super(SigmaTransaction, self).save(*args, **kwargs)
class SigmaRequestTransaction(models.Model):
    sender_id = models.ForeignKey(StaffProfessionalDetails,to_field="bennett_email",on_delete=models.CASCADE)
    receiver_id = models.ForeignKey(StudentProfessionalDetails,to_field="bennett_email",on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    file = models.FileField(upload_to="media",null=True)
    message = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=False)
    current_timestamp=models.DateTimeField(null=True, blank=True, editable=False)
    def save(self, *args, **kwargs):
        self.current_timestamp =datetime.now()
        super(SigmaRequestTransaction, self).save(*args, **kwargs)
# Create your models here.
