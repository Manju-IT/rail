from django.db import models


class RegisterTable(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    