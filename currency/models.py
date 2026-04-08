from django.db import models
from django.conf import settings
from datetime import date

class OrbitWallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    balance = models.IntegerField(default=0)
    last_daily_claim = models.DateField(null=True, blank=True)
    
    def claim_daily(self):
        today = date.today()
        if self.last_daily_claim != today:
            self.balance += 10
            self.last_daily_claim = today
            self.save()
            return True
        return False
