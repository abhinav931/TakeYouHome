from django.db import models
from django.urls import reverse
#TOTAL MODELS = 10

class divisionDistrict(models.Model):
    div_no = models.IntegerField()
    district_name = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.div_no}. {self.district_name}'
    
class Instructions(models.Model):
    message = models.TextField(max_length = 200)
    
    def __str__(self):
        return f'Help from people'
    
    
class BhopalData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
class ChambalData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
class GwaliorData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
class IndoreData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
class JabalpurData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'

class NarmadapuramData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)       
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
class RewaData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
class SagarData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
    
class ShahdolData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'
    
class UjjainData(models.Model):
    stucked_district = models.CharField(max_length = 40)
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 8)
    aadhaar_no = models.BigIntegerField()
    contact_no = models.IntegerField()
    email = models.EmailField(max_length = 40)
    reason = models.CharField(max_length = 40)
    current_address = models.CharField(max_length = 60)
    permanent_address = models.CharField(max_length = 40)
    comments = models.CharField(max_length = 40)
    
    def __str__(self):
        return f'{self.stucked_district}. {self.first_name}'