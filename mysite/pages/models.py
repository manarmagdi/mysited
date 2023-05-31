from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

    
    
    
      
class Signup(models.Model):
    Email= models.CharField(max_length=100, null= True)
    Phone= models.CharField(max_length=100, null= True)
    Address= models.CharField(max_length=100, null= True)
    Password= models.CharField(max_length=100, null= True)
    Username= models.CharField(max_length=100 , null= True)
    Image = models.ImageField(upload_to="media/"  , null= True) 
    
    def __str__(self):
        return str(self.Email) 



class Product1(models.Model):
    name = models.CharField(max_length=60)
    material = models.CharField(max_length=50)
    fabric_finish = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    characteristic = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="media/")
    def re(self):
         return reverse('add', args=[self.id])
    
    def __str__(self):
        return self.name 

   #btkhlyy kol product ba3mlu add yezhr fel database be esmuu 
    
    class Meta:
        verbose_name= 'scarf'
        
   #btghyrly el esm el ra'esyyy lel table fel database -> (ADD "Scarf")
   
   
class Product2(models.Model):
    name= models.CharField(max_length=60)
    color= models.CharField(max_length=60)
    material= models.CharField(max_length=60)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    Length_from_shoulder_to_feet= models.CharField(max_length=60)
    image=models.ImageField(upload_to="media/")
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name= 'Prayer dress'
        
class Cart(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     products = models.ManyToManyField(Product1)
     
    