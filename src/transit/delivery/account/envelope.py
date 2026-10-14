# src/transit/delivery/account/envelope.py

"""
Module: transit.delivery.account.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from domain import Account, AccountPrimeExtract
from transit import MachineAccountCarrier, HumanAccountCarrier, ProductEnvelope


T = TypeVar("T", bound="Account")

class RootAccountEnvelope(ProductEnvelope[T], Generic[T]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RooAccountValidator forwarded to client validators.

    Attributes:
        id: int
        prime_extract: AccountPrimeExtract[T]

    Provides:

    Super Class:
        ProductEnvelope
    """
    _id: int

    def __init__(
            self,
            id: int,
            prime_extract: AccountPrimeExtract[T],
    ):
        """
        Args:
            id: int
            prime_extract: AccountPrimeExtract[T]
        """
        super().__init__(prime_extract=prime_extract)
        self._id = id
    
    @property
    def prime_extract(self) -> AccountPrimeExtract[T]:
        return cast(AccountPrimeExtract[T], super().prime_extract)
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def for_machine_account_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, MachineAccountCarrier)
    
    @property
    def for_human_account_consumer(self) -> bool:
        return isinstance(self._prime_extract.reference, HumanAccountCarrier)

