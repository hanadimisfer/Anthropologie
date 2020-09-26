from django.conf import settings
from django.shortcuts import reverse
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


CATEGORY_CHOICES = (
    ('F', 'Furniture'),
    ('D', 'Dining'),
    ('A', 'Accessories')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    Shipping_Address = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total


class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=50)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=5, validators=[RegexValidator(r'^[0-9]{5}$')])
    CCname = models.CharField(max_length=100)
    CCnumber = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]{10}$')])
    expiration = models.CharField(max_length=5, validators=[RegexValidator(r'(0[1-9]|10|11|12)/[0-9]{2}$')])
    cvv = models.CharField(max_length=3, validators=[RegexValidator(r'^[0-9]{3}$')])

    def __str__(self):
        return self.user.username
