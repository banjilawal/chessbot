# src/domain/extract/struct/account/extract.py

"""
Module: domain.extract.struct.account.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import StructPrimeExtract, Account, AccountBlueprint
from transit import AccountCarrier

T = TypeVar("T", bound="Account")

class AccountPrimeExtract(StructPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for AccountValidator.

    Attributes:
        carrier: AccountCarrier
        blueprint: Optional[AccountBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: AccountCarrier[T],
            blueprint: Optional[AccountBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: AccountCarrier[T]
            blueprint: Optional[AccountBlueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> AccountCarrier[T]:
        return cast(AccountCarrier[T], super().carrier)
    
    @property
    def blueprint(self) -> Optional[AccountBlueprint[T]]:
        return cast(AccountBlueprint[T], super().blueprint)