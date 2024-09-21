from django.db import models


    
class Province(models.Model):
    code = models.CharField(max_length=20, unique=True)
    code_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
class District(models.Model):
    code = models.CharField(max_length=20, unique=True)
    code_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name
    
class Ward(models.Model):
    code = models.CharField(max_length=20, unique=True)
    code_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')

    def __str__(self):
        return self.name
    

class Address(models.Model):
    email = models.EmailField(max_length=100)  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    specific_address = models.CharField(max_length=255)
    user = models.ForeignKey('user.user', on_delete=models.CASCADE)
    ward_code = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='address') 

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specific_address}"
