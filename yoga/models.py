from django.db import models
from django.urls import reverse

class Yoga(models.Model):
    name=models.CharField(max_length=200)    
    desc = models.TextField(max_length=1000,help_text="Enter brief desc of Yoga center")
    address = models.TextField(max_length=1000,help_text="Enter address of Yoga center")
    start_time = models.TimeField(auto_now=False,auto_now_add=False)
    end_time = models.TimeField(auto_now=False,auto_now_add=False)
    contact_no = models.IntegerField(null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('yoga-detail', args = [str(self.id)])

        
class Trainer(models.Model):
    yoga = models.ForeignKey(Yoga,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    exp = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
class TrainingLevel(models.Model):
    yoga = models.ForeignKey(Yoga, on_delete=models.SET_NULL, null=True)
    training_name = models.CharField(max_length=200)
    training_type = models.CharField(max_length=200)

    class Meta:
        ordering = ['training_name', 'training_type']

    def __str__(self):
        return self.training_name