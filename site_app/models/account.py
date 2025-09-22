from typing import ClassVar

from django.db import models

from .currency import Currency


class AccountManager(models.Manager):
    def get_by_natural_key(self, name: str):  # noqa: ANN201
        return self.get(name=name)


class Account(models.Model):
    id = models.SmallAutoField(
        'Id',
        primary_key=True,
    )
    name = models.CharField(
        'Name',
        max_length=50,
    )
    label = models.CharField(
        'Label',
        max_length=50,
    )
    currency = models.ForeignKey(
        to=Currency,
        on_delete=models.PROTECT,
    )

    objects = AccountManager()

    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_account_name',
            ),
        ]
        ordering = ('name',)
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self) -> str:
        return f'{self.label} - {self.currency.label}'

    def save(self, *args, **kwargs) -> None:
        self.name = str(self.name).replace(' ', '_').lower()
        super().save(*args, **kwargs)

    @property
    def pk(self) -> int: return self.id

    def natural_key(self) -> tuple[str]:
        return (self.name,)
