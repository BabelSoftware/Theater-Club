from django.db import models

# Create your models here.

class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=100)
    
    fullfilment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name