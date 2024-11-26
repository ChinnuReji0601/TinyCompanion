from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.

class Profile(models.Model):
    jk=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    phone=models.IntegerField()
class Cat(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.FileField(upload_to="documents",default="image.jpg")

class Kitten(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="documents",default="image.jpg")
    description = models.TextField()
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    image = models.FileField(upload_to="documents",default="image.jpg")
class Food(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="documents",default="image.jpg")
class Foodk(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="documents",default="image.jpg")
class Toy(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="documents",default="image.jpg")
class Aboutus(models.Model):
    description=models.TextField()
class Contactus(models.Model):
    phone=models.IntegerField()
    email = models.EmailField()
    address=models.TextField()
from django.db import models

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_on_card = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)




class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    doctor = models.CharField(max_length=255)
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Reference to the model
    object_id = models.PositiveIntegerField()  # ID of the object
    content_object = GenericForeignKey('content_type', 'object_id')  # Actual object
    purchased = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


