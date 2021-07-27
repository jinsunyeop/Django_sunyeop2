from django.db import models



class basic_model(models.Model):

    text = models.CharField(max_length=10,null=False)

