from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    OTHER = 'other', 'Other'
    JACKETS = 'jackets', 'Jackets'
    SHOES = 'shoes', 'Shoes'
    JEANS = 'jeans', 'Jeans'
    SHIRTS = 'shirts', 'Shirts'


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    image = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        default='https://99px.ru/sstorage/56/2015/01/image_560401151755269388068.jpg',
        verbose_name='Image'
    )
    category = models.CharField(
        verbose_name='Category',
        choices=StatusChoices.choices,
        max_length=100,
        default=StatusChoices.OTHER)
    rest = models.PositiveIntegerField(null=False, blank=False, verbose_name='Rest')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='Price')

    def __str__(self):
        return f"{self.title} - {self.category} - {self.price}"
