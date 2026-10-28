# src/transit/delivery/account/human/envelope.py

"""
Module: transit.delivery.account.human.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import HumanAccount, HumanAccountPrimeExtract
from transit import AccountEnvelope


class HumanAccountEnvelope(AccountEnvelope[HumanAccount]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RooAccountValidator forwarded to client validators.

    Attributes:
        firstname: str

    Provides:

    Super Class:
        RootAccountEnvelope
    """
    _id: int
    _firstname: str
    _lastname: str

    def __init__(
            self,
            id: int,
            firstname: str,
            lastname: str,
            prime_extract: HumanAccountPrimeExtract,
    ):
        """
        Args:
            id: int
            firstname: str
            lastname: str
            prime_extract: HumanAccountPrimeExtract
        """
        super().__init__(id=id, prime_extract=prime_extract)
        self._firstname = firstname
        self._lastname = lastname
    
    @property
    def prime_extract(self) -> HumanAccountPrimeExtract:
        return cast(HumanAccountPrimeExtract, super().prime_extract)
    
    @property
    def firstname(self) -> str:
        return self._firstname
    
    @property
    def lasstname(self) -> str:
        return self._lastname

