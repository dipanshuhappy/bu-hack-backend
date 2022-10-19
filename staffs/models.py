from datetime import datetime
from django.db import models
STATUS_CHOICES={
   ("MA","Mathematics"),
   ("PH","Physics"),
}
DESIGNATION_CHOICES = {
    ("CS","Computer Science"),
    ("MA","Mathematics")
}
class StaffProfessionalDetails(models.Model):
    bennett_email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    faculty_id = models.IntegerField(unique=True)
    designation = models.CharField(max_length=255, choices=DESIGNATION_CHOICES)
    cabin_number = models.CharField(max_length=255, null=True, blank=True)
    intercom = models.CharField(max_length=15, null=True, blank=True)
    school_code = models.CharField(max_length=255)
    department_code = models.CharField(max_length=255)
    phd_date = models.DateField(null=True, blank=True)
    phd_institution = models.CharField(max_length=255)
    favourite_courses = models.TextField(null=True, blank=True)
    batch_mentor = models.CharField(max_length=255)
    entry_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='ACTIVE')
    current_timestamp = models.DateTimeField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.current_timestamp = datetime.now()
        super(StaffProfessionalDetails, self).save(*args, **kwargs)

    def __str__(self):
        return self.bennett_email
