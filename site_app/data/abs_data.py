from abc import ABC, abstractmethod
from typing import NamedTuple

from site_app.enums import CurrencyKind


class CurrencyRow(NamedTuple):
    name: str
    label: str
    kind: CurrencyKind

class AccountRow(NamedTuple):
    name: str
    label: str
    currency_name: str

class BaseDataSeeder(ABC):
    @classmethod
    @abstractmethod
    def get_currencies(cls) -> list[CurrencyRow]:
        pass

    @classmethod
    @abstractmethod
    def get_accounts(cls) -> list[AccountRow]:
        pass
