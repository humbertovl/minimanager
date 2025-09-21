from abc import ABC, abstractmethod
from typing import NamedTuple

from site_app.enums import CurrencyKind


class CurrencyRow(NamedTuple):
    name: str
    label: str
    kind: CurrencyKind

class BaseDataSeeder(ABC):
    @classmethod
    @abstractmethod
    def get_currencies(cls) -> list[CurrencyRow]:
        pass
