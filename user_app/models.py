from django.db import models

# Create your models here.

class RegisterForm(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    Password2 = models.CharField(max_length=100)
    
    class Meta:
       verbose_name_plural = "RegisterForms" 
    def __str__(self):
        return self.username