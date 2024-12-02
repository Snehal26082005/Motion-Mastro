from django.db import models

class Home_feedbacks(models.Model):
        name=models.CharField(max_length=122)
        feedback=models.CharField(max_length=122)
        date=models.DateField()

