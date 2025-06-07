from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('farmer', 'Farmer'),
        ('vet', 'Vet'),
        ('admin', 'Admin'),
        ('supplier', 'Supplier'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Create your models here.

class Login(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

class Farmer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    location = models.CharField(max_length=200)
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"{self.company_name} ({self.user.username})"


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    descriptions = models.TextField()
    image_url = models.URLField()

class Order(models.Model):
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=50)
    delivery_date = models.DateField()
    payment_status = models.CharField(max_length=50)

class Report(models.Model):
    descriptions = models.TextField()
    image_url = models.URLField()

class Vet(models.Model):
    full_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    location = models.CharField(max_length=200)

class Consultation(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    issue = models.TextField()
    notes = models.TextField()
    recommendation = models.TextField()
    consultation_date = models.DateField()

class AI(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    confidence_score = models.FloatField()
    diagnosis = models.CharField(max_length=200)
    recommended_product = models.CharField(max_length=200)
