# src/transit/delivery/account/machine/envelope.py

"""
Module: transit.delivery.account.machine.envelope
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import MachineAccount, MachineAccountPrimeExtract
from transit import RootAccountEnvelope


class MachineAccountEnvelope(RootAccountEnvelope[MachineAccount]):
    """
    Role
        -   Data Transfer

    Responsibilities:
        1.  Data from a RooAccountValidator forwarded to client validators.

    Attributes:
        name: str

    Provides:

    Super Class:
        RootAccountEnvelope
    """
    _id: int
    _name: str

    def __init__(
            self,
            id: int,
            name: str,
            prime_extract: MachineAccountPrimeExtract,
    ):
        """
        Args:
            id: int
            name: str
            prime_extract: MachineAccountPrimeExtract
        """
        super().__init__(id=id, prime_extract=prime_extract)
        self._name = name
    
    @property
    def prime_extract(self) -> MachineAccountPrimeExtract:
        return cast(MachineAccountPrimeExtract, super().prime_extract)
    
    @property
    def name(self) -> str:
        return self._name

