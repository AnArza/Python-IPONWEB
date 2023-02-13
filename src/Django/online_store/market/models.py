from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.html import mark_safe


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="store/",
                               default="noimage.png")

    def __str__(self):
        return self.user.username


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="store/",
                               default="noimage.png")

    def __str__(self):
        return self.user.username


class StoreCategory(models.Model):
    name = models.TextField()
    picture = models.ImageField(upload_to="store/",
                                default="noimage.png")

    def picture_preview(self):
        return mark_safe(f'<img src = "{self.picture.url}" width = 100/>')

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.TextField()
    picture = models.ImageField(upload_to="store/",
                                default="noimage.png")

    def picture_preview(self):
        return mark_safe(f'<img src = "{self.picture.url}" width = 100/>')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(StoreOwner, on_delete=models.PROTECT)
    store_category = models.ForeignKey(StoreCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.TextField()
    picture = models.ImageField(upload_to="store/",
                                default="noimage.png")
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    info = models.TextField(blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT)

    def picture_preview(self):
        return mark_safe(f'<img src = "{self.picture.url}" width = 100/>')

    def __str__(self):
        return self.name


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    @property
    def total_price(self):
        total = 0
        for item in Item.objects.filter(mybag__id=self.id):
            total += item.price
        return total


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    buy_time = models.DateTimeField(default=timezone.now)

    @property
    def total_price(self):
        total = 0
        for item in Item.objects.filter(purchase__id=self.id):
            total += item.price
        return total
