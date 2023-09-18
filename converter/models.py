from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        return self.code
    
class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, related_name='rates', on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

class Conversion(models.Model):
    from_currency = models.ForeignKey(Currency, related_name='conversions', on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    result = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
