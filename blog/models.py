from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Appearing date")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title


class Motor(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=25)
    motor = models.OneToOneField(Motor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through='Offer', related_name='+')
    products_without_price = models.ManyToManyField(Product, related_name="sellers")

    def __str__(self):
        return self.name


class Offer(models.Model):
    price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} sold by {self.seller}"

