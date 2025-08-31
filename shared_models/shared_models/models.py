from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        app_label = 'shared_models'

class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'shared_models'
