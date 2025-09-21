from typing import ClassVar

from django.db import models

from site_app.enums import CurrencyKind


class CurrencyManager(models.Manager):
    def get_by_natural_key(self, name: str):  # noqa: ANN201
        return self.get(name=name)

class Currency(models.Model):
    id = models.SmallAutoField('Id', primary_key=True,)
    name = models.CharField(
        'Name',
        max_length=20,
    )
    label = models.CharField(
        'Label',
        max_length=40,
    )
    kind = models.PositiveSmallIntegerField(
        'Currency type',
        choices=CurrencyKind,
    )

    # Managers
    objects = CurrencyManager()

    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_currency_name',
            ),
        ]
        ordering = ('name',)
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self) -> str:
        return f'{self.label} - {CurrencyKind(self.kind).label}'

    def save(self, *args, **kwargs) -> None:
        self.name = str(self.name).replace(' ', '_').lower()
        super().save(*args, **kwargs)

    @property
    def pk(self) -> int: return self.id

    def natural_key(self) -> tuple[str]:
        return (self.name,)
