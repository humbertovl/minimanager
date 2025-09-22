from enum import StrEnum, auto

from site_app.data.abs_data import AccountRow, BaseDataSeeder, CurrencyRow
from site_app.enums import CurrencyKind


class SeedCurrency(StrEnum):
    usd = auto()

class SeedAccount(StrEnum):
    cash = auto()

class DataSeeder(BaseDataSeeder):
    @classmethod
    def get_currencies(cls) -> list[CurrencyRow]:
        return [
            CurrencyRow(
                SeedCurrency.usd,
                'USD',
                CurrencyKind.FIAT,
            ),
        ]

    @classmethod
    def get_accounts(cls) -> list[AccountRow]:
        return [
            AccountRow(
                SeedAccount.cash,
                'Cash',
                SeedCurrency.usd,
            )
        ]
