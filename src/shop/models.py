from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)


class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='products',
                                on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    image = models.URLField(null=False, blank=False)
    description = models.CharField(blank=False, null=False, max_length=2000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)


class ItemBasket(models.Model):
    basket = models.ForeignKey(Basket,
                                related_name='items',
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE,
                                primary_key=False)

    product = models.ForeignKey(Product,
                                related_name='itembaskets',
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE,
                                primary_key=False)
    qty = models.PositiveIntegerField()
