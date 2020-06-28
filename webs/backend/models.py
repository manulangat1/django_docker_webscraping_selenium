from django.db import models

# Create your models here.

class BaseModel(models.Model):
    scrap_date = models.DateTimeField(auto_now_add=True)

class Articles(BaseModel):
    title = models.CharField(max_length=200,blank=True)
    post = models.TextField()
    user = models.CharField(max_length=80)
    comments = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
class Records(BaseModel):
    start_time = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)

    def __str__(self):
        return "{0}".format(str(success))
