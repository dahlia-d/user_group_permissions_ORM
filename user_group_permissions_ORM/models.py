from django.db import models

# Create your models here.
class Permission(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.TextField()

    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

class User(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()

    permissions = models.ManyToManyField(Permission)

    groups = models.ManyToManyField(Group)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'