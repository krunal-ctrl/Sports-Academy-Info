from django.db import models
from django.urls import reverse

class Academy(models.Model):
    name=models.CharField(max_length=200)    
    desc = models.TextField(max_length=1000,help_text="Enter a brief desc of academy")
    address = models.TextField(max_length=1000,help_text="Enter address of academy")
    start_time = models.TimeField(auto_now=False,auto_now_add=False)
    end_time = models.TimeField(auto_now=False,auto_now_add=False)
    contact_no = models.IntegerField(null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('academy-detail', args = [str(self.id)])
        
class Coach(models.Model):
    academy = models.ForeignKey(Academy,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    exp = models.IntegerField()

    def __str__(self):
        return self.name

class Sports(models.Model):
    academy = models.ForeignKey(Academy,on_delete=models.SET_NULL,null=True)
    sports_name = models.CharField(max_length=200)
    sports_type = models.CharField(max_length=200)
    
    def __str__(self):        
        return self.sports_name