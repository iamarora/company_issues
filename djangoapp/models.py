from django.db import models


# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=255)
    ticker_symbol = models.CharField(max_length=10)
    animal_testing = models.BooleanField()
    nuclear_weapons = models.BooleanField()
    coal_power = models.BooleanField()
    rainforest_destruction = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "companies"
        verbose_name_plural = "companies"
        indexes = [
            models.Index(fields=['name', ]),
            models.Index(fields=['ticker_symbol', ]),
        ]
        ordering = ['name']
