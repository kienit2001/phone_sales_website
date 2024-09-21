from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    verification_code = models.CharField(max_length=255, null=True, blank=True)
    roles = models.ManyToManyField('Role', related_name='users')  # Many-to-many relation

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Role(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name