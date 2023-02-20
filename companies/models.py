from django.db import models
from django.urls import reverse


class ClientLoc(models.Model):
    company_type = models.CharField(max_length=100, default='-')
    company_name = models.CharField(max_length=250, default='-')
    pos_per_acc = models.CharField(max_length=250, default='-')
    position_nom = models.CharField(max_length=250, default='-')
    person_nom = models.CharField(max_length=250, default='-')
    acting_on = models.CharField(max_length=100, default='-')
    legal_addr = models.CharField(max_length=500, default='-')
    passport_series = models.CharField(max_length=250, default='-')
    passport_number = models.CharField(max_length=250, default='-')
    pass_issued_by = models.CharField(max_length=250, default='-')
    pass_issued_date = models.CharField(max_length=100, default='-')
    pass_issued_code = models.CharField(max_length=500, default='-')
    postal_addr = models.CharField(max_length=500, default='-')
    registration_addr = models.CharField(max_length=500, default='-')
    tel = models.CharField(max_length=100, default='-')
    email = models.CharField(max_length=100, default='-')
    bank_name = models.CharField(max_length=250, default='-')
    bic = models.CharField(max_length=50, default='-')
    curr_acc = models.CharField(max_length=250, default='-')
    corr_acc = models.CharField(max_length=250, default='-')
    inn = models.CharField(max_length=250, default='-')
    kpp = models.CharField(max_length=250, default='-')
    ogrn = models.CharField(max_length=250, default='-')
    okpo = models.CharField(max_length=250, default='-')

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('index')

class OwnLoc(models.Model):
    company_type = models.CharField(max_length=100, default='-')
    company_name = models.CharField(max_length=250, default='-')
    pos_per_acc = models.CharField(max_length=250, default='-')
    position_nom = models.CharField(max_length=250, default='-')
    person_nom = models.CharField(max_length=250, default='-')
    acting_on = models.CharField(max_length=100, default='-')
    legal_addr = models.CharField(max_length=500, default='-')
    passport_series = models.CharField(max_length=250, default='-')
    passport_number = models.CharField(max_length=250, default='-')
    pass_issued_by = models.CharField(max_length=250, default='-')
    pass_issued_date = models.CharField(max_length=100, default='-')
    pass_issued_code = models.CharField(max_length=500, default='-')
    postal_addr = models.CharField(max_length=500, default='-')
    registration_addr = models.CharField(max_length=500, default='-')
    tel = models.CharField(max_length=100, default='-')
    email = models.CharField(max_length=100, default='-')
    bank_name = models.CharField(max_length=250, default='-')
    bic = models.CharField(max_length=50, default='-')
    curr_acc = models.CharField(max_length=250, default='-')
    corr_acc = models.CharField(max_length=250, default='-')
    inn = models.CharField(max_length=250, default='-')
    kpp = models.CharField(max_length=250, default='-')
    ogrn = models.CharField(max_length=250, default='-')
    okpo = models.CharField(max_length=250, default='-')

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('index')


class CompanyInt(models.Model):
    company_name = models.CharField(max_length=250)
    pos_per_acc = models.CharField(max_length=250)
    position_nom = models.CharField(max_length=250)
    person_nom = models.CharField(max_length=250)
    acting_on = models.CharField(max_length=100)
    legal_addr = models.CharField(max_length=500)
    postal_addr = models.CharField(max_length=500)
    tel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
