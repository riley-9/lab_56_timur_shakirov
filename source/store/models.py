from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    FOOD = 'food', 'Food'
    NONFOOD = 'nonfood', 'Nonfood'
    OTHER = 'Other', 'other'


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')
    image = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        default='https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fdogopedyrussian%2Fimages%2F7%2F72%2F486840.jpeg%2Frevision%2Flatest%3Fcb%3D20181028100942%26path-prefix%3Dru&imgrefurl=https%3A%2F%2Fdogopedy.fandom.com%2Fru%2Fwiki%2F%25D0%2592%25D0%25B5%25D0%25BB%25D1%258C%25D1%2588-%25D0%25BA%25D0%25BE%25D1%2580%25D0%25B3%25D0%25B8&tbnid=2lPP-fXUyxQqaM&vet=12ahUKEwiQu6eFlLj9AhXYsSoKHVwPDwoQMygEegUIARC-AQ..i&docid=sFzpAu-vIEmXuM&w=1024&h=707&q=%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0%20%D0%BA%D0%BE%D1%80%D0%B3%D0%B8&ved=2ahUKEwiQu6eFlLj9AhXYsSoKHVwPDwoQMygEegUIARC-AQ',
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
