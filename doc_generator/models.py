from django.db import models
from django.urls import reverse


# Create your models here.
class StandardTesContract(models.Model):
    agent = models.ForeignKey("companies.OwnLoc", on_delete=models.CASCADE)
    customer = models.ForeignKey("companies.ClientLoc", on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=100, default='-')
    contract_date = models.CharField(max_length=100, default='-')
    contract_city = models.CharField(max_length=250, default='-')
    valid_until = models.CharField(max_length=100, default='-')
    blank = models.BooleanField(default=True)
    stamped = models.BooleanField(default=True)

    def __str__(self):
        return self.contract_number

    def get_absolute_url(self):
        return reverse('index')
