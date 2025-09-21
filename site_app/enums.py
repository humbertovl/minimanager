from enum import auto

from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyKind(models.IntegerChoices):
    # Government/country issued currency
    FIAT = auto(), _('Fiat')
    # Digital points with a stable equivalence to fiat
    POINT_UNITS = auto(), _('Point')
    # Debt to repay plus a certain interest at a fixed time
    BOND_UNITS = auto(), _('Bond')
    # Variable value investment unit
    EQUITY_UNITS = auto(), _('Equity')
    # Crypto currency
    CRYPTO_UNITS = auto(), _('Crypto')
    # Resource exchangable for money
    COMMODITY_UNITS = auto(), _('Commodity')
