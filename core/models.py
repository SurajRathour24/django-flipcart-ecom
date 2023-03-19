from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
('Andhra Pradesh','Andhra Pradesh'),
('Amaravati','Amaravati'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Itanagar','Itanagar'),
('Assam','Assam'),
('Dispur','Dispur'),
('Bihar','Bihar'),
('Patna','Patna'),
('Chhattisgarh','Chhattisgarh'),
('Raipur','Raipur'),
('Goa','Goa'),
('Panaji','Panaji'),
('Gujarat','Gujarat'),
('Gandhinagar','Gandhinagar'),
('Haryana','Haryana'),
('Chandigarh','Chandigarh'),
('Himachal Pradesh','Himachal Pradesh'),
('Shimla','Shimla'),
('Jharkhand','Jharkhand'),
('Ranchi','Ranchi'),
('Karnataka','Karnataka'),
('Bangalore','Bangalore'),
('Kerala','Kerala'),
('Thiruvananthapuram','Thiruvananthapuram'),
('Madhya Pradesh','Madhya Pradesh'),
('Bhopal','Bhopal'),
('Maharashtra','Maharashtra'),
('Mumbai','Mumbai'),
('Manipur','Manipur'),
('Imphal','Imphal'),
('Meghalaya','Meghalaya'),
('Shillong','Shillong'),
('Mizoram','Mizoram'),
('Aizawl','Aizawl'),
('Nagaland','Nagaland'),
('Kohima','Kohima'),
('Odisha','Odisha'),
('Bhubaneshwar','Bhubaneshwar'),
('Punjab','Punjab'),
('Chandigarh','Chandigarh'),
('Rajasthan','Rajasthan'),
('Jaipur','Jaipur'),
('Sikkim','Sikkim'),
('Gangtok','Gangtok'),
('Tamil Nadu','Tamil Nadu'),
('Chennai','Chennai'),
('Telangana','Telangana'),
('Hyderabad','Hyderabad'),
('Tripura','Tripura'),
('Agartala','Agartala'),
('Uttarakhand','Uttarakhand'),
('Dehradun','Dehradun'),
('Uttar Pradesh','Uttar Pradesh'),
('Lucknow','Lucknow'),
('West Bengal','West Bengal'),
('Kolkata','Kolkata'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=80)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ('fashion', 'fashion'),
    ('electronics', 'electronics'),
    ('beauty', 'beauty'),
    ('home','home'),
    ('furniture', 'furniture'),
    ('grocery','grocery')
)
class Product(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length = 50)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length= 100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_image = models.ImageField(upload_to="productimage")

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    odered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATE_CHOICES, max_length=50, default='Pending')