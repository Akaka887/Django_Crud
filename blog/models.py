from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class MyPost(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text= models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.created_date = timezone()
        self.save()
    

    def __str__(self):
        return self.title