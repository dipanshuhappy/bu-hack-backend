from datetime import datetime
from django.db import models
MINOR_HONOUR_CHOICES={
   ("MA","Mathematics"),
   ("PH","Physics")
}
class StudentProfessionalDetails(models.Model):
    bennett_email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    enrollment_number = models.CharField(max_length=255, unique=True)
    school_code = models.CharField(max_length=255, null=True, blank=True)
    department_code = models.CharField(max_length=255, null=True, blank=True)
    scholarship_percentage = models.PositiveSmallIntegerField(null=True, default=0)
    minor = models.CharField(max_length=255, choices=MINOR_HONOUR_CHOICES, null=True)
    honor = models.CharField(max_length=255, choices=MINOR_HONOUR_CHOICES, null=True)
    batch = models.CharField(max_length=255, null=True, blank=True)
    program = models.CharField(max_length=255, null=True, blank=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    admission_date = models.DateField(null=True)
    current_semester = models.SmallIntegerField(default=1)
    exit_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, default='ACTIVE')
    status_change_date = models.DateTimeField(null=True, blank=True)
    current_timestamp = models.DateTimeField(null=True, blank=True, editable=False)
    def save(self, *args, **kwargs):
        self.current_timestamp =datetime.now()
        super(StudentProfessionalDetails, self).save(*args, **kwargs)
    def __str__(self):
        return self.bennett_email
# Create your models here.
