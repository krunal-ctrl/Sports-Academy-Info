from django.db import models
from django.urls import reverse

class Fitness(models.Model):
    name=models.CharField(max_length=200)    
    desc = models.TextField(max_length=1000,help_text="Enter brief desc of Fitness club(i.e gym/yoga)")
    address = models.TextField(max_length=1000,help_text="Enter address of Fitness club(i.e gym/yoga)")
    start_time = models.TimeField(auto_now=False,auto_now_add=False)
    end_time = models.TimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fitness-detail', args = [str(self.id)])

        
class Trainer(models.Model):
    fitness = models.ForeignKey(Fitness,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    exp = models.IntegerField()

    def __str__(self):
        return self.name

class TrainingLevel(models.Model):
    fitness = models.ForeignKey(Fitness, on_delete=models.SET_NULL, null=True)
    training_name = models.CharField(max_length=200)
    training_type = models.CharField(max_length=200)

    def __str__(self):
        return self.training_name