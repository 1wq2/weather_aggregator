from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser


class UserRole(models.Model):
    USER = 'User'
    ADMIN = 'Admin'
    ROLES = (
        (USER, USER),
        (ADMIN, ADMIN)
    )
    role_name = models.CharField(max_length=15, choices=ROLES, default=USER)

    def __str__(self):
        return self.role_name


class User(AbstractUser):
    role = models.ForeignKey(UserRole, null=True, blank=False, on_delete=models.CASCADE)


class WedQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    temp = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.city + self.temp + str(self.date)


class WedHistQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(ax_length=100)
    city = models.CharField(max_length=100)
    temp = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.city + self.temp + str(self.date)



class WedApi(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name
