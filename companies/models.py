from django.db import models


class CompanyLoc(models.Model):
    company_name = models.CharField(max_length=250)
    pos_per_acc = models.CharField(max_length=250)
    position_nom = models.CharField(max_length=250)
    person_nom = models.CharField(max_length=250)
    acting_on = models.CharField(max_length=100)
    legal_addr = models.CharField(max_length=500)
    postal_addr = models.CharField(max_length=500)
    tel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=250)
    bic = models.CharField(max_length=50)
    curr_acc = models.CharField(max_length=250)
    corr_acc = models.CharField(max_length=250)
    inn = models.CharField(max_length=250)
    kpp = models.CharField(max_length=250)
    ogrn = models.CharField(max_length=250)
    okpo = models.CharField(max_length=250)

    def __str__(self):
        return self.company_name


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
