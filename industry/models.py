from django.db import models

# Create your models here.
class Industry(models.Model):
    name = models.CharField(max_length = 100)
    adinfo = models.TextField(blank=True,null=True)
    url = models.URLField(null=True)
    trending = models.BooleanField(null=True, default=False)
    def __str__(self):
        return self.name

class Qnai(models.Model):
    industry = models.ForeignKey('Industry',related_name='questioni',on_delete=models.CASCADE)

    number = models.IntegerField(null=True)
    urlref = models.URLField(null=True)
    question = models.TextField(blank=True,null=True)
    answer = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.question

class Equipment(models.Model):
    industry = models.ManyToManyField('Industry',related_name = 'equipment')
    name = models.CharField(max_length = 50, null=True)
    adinfo = models.TextField(blank=True,null=True)
    url = models.URLField(null=True)
    trending = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name

class Qnae(models.Model):
    equipment = models.ForeignKey('Equipment',related_name='questione',on_delete=models.CASCADE)

    number = models.IntegerField(null=True)
    urlref = models.URLField(null=True)
    question = models.TextField(blank=True,null=True)
    answer = models.TextField(blank=True,null=True)
    




