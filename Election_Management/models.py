from django.db import models

# Create your models here.

class Voters_Information(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)
    pollingunit_id = models.IntegerField(max_length=13)
    
    

class Lga_Results(models.Model):
    result_id = models.IntegerField(max_length=11)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(max_length=11)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class Announced_Pu_Results(models.Model):
    result_id = models.IntegerField(max_length=11)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(max_length=11)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class Announced_State_Result(models.Model):
    result_id = models.IntegerField(max_length=11)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(max_length=11)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)
    
class Announced_Ward_Results(models.Model):
    result_id = models.IntegerField(max_length=11)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField(max_length=11)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class Lga(models.Model):
    lga_id = models.IntegerField(max_length=11)
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField(max_length=11)
    lga_description = models.CharField(max_length=50)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)
    

class Polling_Unit(models.Model):
    polling_unit_id = models.IntegerField(max_length=11)
    ward_id = models.IntegerField(max_length=11, null=True)
    lga_id = models.IntegerField(max_length=11, null=True)
    uniquewarsid = models.IntegerField(max_length=11, null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.CharField(max_length=50, null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=50, null=True)

class Ward(models.Model):
    ward_id = models.IntegerField(max_length=11)
    lga_id = models.IntegerField(max_length=11)
    ward_name = models.CharField(max_length=50)
    ward_description = models.CharField(max_length=50)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

class States(models.Model):
    state_id = models.IntegerField()
    state_name = models.CharField(max_length=50)