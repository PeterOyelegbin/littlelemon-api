from django.db import models
from phone_field import PhoneField
from uuid import uuid4


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255, unique=True, db_index=True)
    
    def __str__(self):
        return self.title


class MenuItem(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255, unique=True, db_index=True)
    cover_image = models.ImageField(upload_to='littleLemon/menu/')
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True, default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} -> {self.price} -> {self.category.title}'


class Booking(models.Model):
    occasion_choices = (
        ("Birthday", "Birthday"),
        ("Wedding", "Wedding"),
        ("Reunion", "Reunion"),
        ("Date", "Date"),
        ("Others", "Others"),
    )

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    full_name = models.CharField(max_length=255)    
    email = models.EmailField()
    phone = PhoneField()
    number_of_guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.SmallIntegerField()
    occasion = models.CharField(max_length=20, choices=occasion_choices, default='Birthday')
    
    def __str__(self):
        return f'{self.full_name} - {self.date}, {self.time}'
