import csv

from django.db import models


class Currency(models.Model):
    CRYPTO = 'CRYPTO'
    PHYSICAL = 'PHYSICAL'
    TYPE_CHOICES = (
        (CRYPTO, 'crypto'),
        (PHYSICAL, 'physical'),
    )

    code = models.CharField('Code', max_length=10)
    name = models.CharField('Name', max_length=64)
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, default=PHYSICAL)

    class Meta:
        """Meta definition for Currency."""

        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        """Unicode representation of Currency."""
        return self.code

    def get_currencies(self, file):
        with open(file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            data = (
                [
                    {
                        'code': currency[0],
                        'name': currency[1],
                    }
                    for currency in [
                        row[0].split(',')
                        for row in reader
                    ]
                    if len(currency) > 1
                ]
            )
        return data or {}

    def save_currencies(self):
        CURRENCIES = {
            self.CRYPTO: 'digital_currency_list.csv',
            self.PHYSICAL: 'physical_currency_list.csv',
        }
        if not Currency.objects.all():
            for currency_type, currency_file in CURRENCIES.items():
                currency_dict = self.get_currencies(currency_file)
                for currency in currency_dict:
                    Currency.objects.create(type=currency_type, **currency)


class CurrencyData(models.Model):
    symbol = models.ForeignKey('Currency')
    market = models.ForeignKey('Currency')
    volume = models.FloatField()
    market_cap = 
    updated_at = models.DateTimeField()


    class Meta:
        """Meta definition for CurrencyData."""

        verbose_name = 'CurrencyData'
        verbose_name_plural = 'CurrencyData'

    def __str__(self):
        """Unicode representation of CurrencyData."""
        pass


