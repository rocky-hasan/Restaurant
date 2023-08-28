from django.contrib.auth.models import User
from django.db import models


# Create your models here.


STATE_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('uttara_sec-1', 'uttara_sec-1'),
    ('Mirpur-2', 'Mirpur-2'),
    ('Muradpur', 'Muradpur'),
    ('Feni', 'Feni'),

)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=200)
    house_no = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)


class ContactModel(models.Model):
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.username


class AboutModel(models.Model):
    heading = models.CharField(max_length=200)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    line3 = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='about')


category_choice = (
    ('ST', 'STARTERS'),
    ('SL', 'SALAD'),
    ('SP', 'SPECIALITY'),
)


class AllFood(models.Model):
    food_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(choices=category_choice, max_length=10)
    food_image = models.ImageField(upload_to='FoodImage')

    def __str__(self):
        return str(self.id)


class SectionModel(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    section_image = models.ImageField(upload_to='SectionImage')

    def __str__(self):
        return str(self.title)


class EventsModel(SectionModel):
    price = models.FloatField()
    events_image = models.ImageField(upload_to='EventsImage')


class ChefsModel(SectionModel):
    name = models.CharField(max_length=50)
    chefs_image = models.ImageField(upload_to='ChefsImage')


class GalleryModel(SectionModel):
    gallery_image = models.ImageField(upload_to='GalleryImage')


class Booking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone_no = models.CharField(max_length=20)
    date = models.DateField(max_length=20)
    time = models.TimeField(max_length=20)
    people = models.IntegerField()
    msg = models.TextField()


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(AllFood, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.food.price


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(AllFood, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.food.price

