from datetime import datetime
from django.db import models

class StaffCoinDetails(models.Model): 
     staff_professional_detail_id = models.ForeignKey('staffs.StaffProfessionalDetails',to_field="bennett_email", on_delete=models.CASCADE)
     sigma_coin=models.PositiveBigIntegerField()
     current_timestamp=models.DateTimeField(null=True, blank=True, editable=False);
     def save(self, *args, **kwargs):
        self.current_timestamp =datetime.now() 
        super(StaffCoinDetails, self).save(*args, **kwargs)