from django.core.validators import MinValueValidator
from django.db import models

from Online_shop.accounts.models import ShopUser


class Jewelry(models.Model):
    JEWELRY_NAME_MAX_LEN = 30
    MIN_QUANTITY = 1
    STEEL = 'Steel'
    GOLD = 'Gold'
    SILVER = 'Silver'
    MATERIALS = [(x, x) for x in (GOLD, STEEL, SILVER)]

    name = models.CharField(
        max_length=JEWELRY_NAME_MAX_LEN
    )
    quantity = models.IntegerField(
        validators=(
            MinValueValidator(MIN_QUANTITY),
        )
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    materials = models.CharField(
        max_length=max(len(x) for (x, _) in MATERIALS),
        choices=MATERIALS
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
    image = models.ImageField(
        upload_to='mediafiles/',

    )
    user_key = models.ForeignKey(
        ShopUser, on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.name

    def multiplied_quantity_with_price(self):
        return self.quantity * self.price


class Souvenir(models.Model):
    SOUVENIRS_NAME_MAX_LEN = 30
    MIN_QUANTITY = 1
    LUXARY = 'Luxary'
    NORMAL = 'Normal'
    TYPES = [(x, x) for x in (LUXARY, NORMAL)]
    name = models.CharField(
        max_length=SOUVENIRS_NAME_MAX_LEN
    )
    quantity = models.IntegerField(
        validators=(
            MinValueValidator(MIN_QUANTITY),
        )
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
    image = models.ImageField(
        upload_to='mediafiles/',

    )
    user_key = models.ForeignKey(
        ShopUser, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def multiplied_quantity_with_price(self):
        return self.quantity * self.price


class Flower(models.Model):
    FLOWERS_MAX_LEN = 50
    MIN_QUANTITY = 1
    BOUQUET = 'Bouquet'
    BASKET = 'Basket'
    TYPES = [(x, x) for x in (BOUQUET, BASKET)]
    name = models.CharField(
        max_length=FLOWERS_MAX_LEN
    )
    quantity = models.IntegerField(
        validators=(
            MinValueValidator(MIN_QUANTITY),
        )
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
    image = models.ImageField(
        upload_to='mediafiles/',

    )
    user_key = models.ForeignKey(
        ShopUser, on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name

    def multiplied_quantity_with_price(self):
        return self.quantity * self.price


class Plant(models.Model):
    PLANTS_MAX_LEN = 50
    MIN_QUANTITY = 1
    WINTER_PLANT = 'Winter plant'
    SUMMER_PLANT = 'Summer plant'
    SPRING_PLANT = 'Spring plant'
    AUTUMN_PLANT = 'Autumn plant'
    TYPES = [(x, x) for x in (WINTER_PLANT, SUMMER_PLANT, SPRING_PLANT, AUTUMN_PLANT)]
    name = models.CharField(
        max_length=PLANTS_MAX_LEN
    )
    quantity = models.IntegerField(
        validators=(
            MinValueValidator(MIN_QUANTITY),
        )
    )
    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )
    image = models.ImageField(
        upload_to='mediafiles/',

    )
    user_key = models.ForeignKey(
        ShopUser, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def multiplied_quantity_with_price(self):
        return self.quantity * self.price
class AskQuotation(models.Model):
    MAX_LEN_NAME_OF_QUOTATION=50
    user_name=models.CharField(
        max_length=MAX_LEN_NAME_OF_QUOTATION
    )
    email_to_contact=models.EmailField(
        null=True,
        blank=True,
    )
    description_for_quotation=models.TextField(
        null=True,
        blank=True,
    )
    user_key = models.ForeignKey(
        ShopUser, on_delete=models.CASCADE

    )