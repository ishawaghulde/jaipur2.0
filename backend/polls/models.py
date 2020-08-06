from django.db import models

# Create your models here.

class login_user(models.Model):

  
    email = models.EmailField()  
    name = models.CharField(max_length=100)  
    password = models.CharField(max_length=15)  
    class Meta:  
        db_table = "Employee"  


class feedback1_routes(models.Model):

    route_name = models.CharField(max_length=200)
    illumination = models.FloatField()
    overall_safety = models.FloatField()
    road_condition = models.FloatField()
    hazardous_contruction = models.FloatField()
    no_of_reviews= models.FloatField()
    danger_score= models.FloatField()
    class Meta:
        db_table= "feedback1_routes"

class feedback1_text(models.Model):
    
    route_name= models.CharField(max_length=200)
    review_text= models.CharField(max_length=300)
    class Meta:
        db_table="feedback1_text"

class tag1(models.Model):

    word= models.CharField(max_length=200)
    no_of_occurance= models.FloatField()
    class Meta:
        db_table="tag1"
