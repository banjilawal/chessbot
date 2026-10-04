# src/domain/extract/model/account/extract.py

"""
Module: domain.extract.model.account.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import ModelPrimeExtract, Account, AccountBlueprint
from transit import AccountCarrier

T = TypeVar("T", bound="Account")

class AccountPrimeExtract(ModelPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for AccountValidator.

    Attributes:
        carrier: AccountCarrier[T]
        blueprint: Optional[AccountBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
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
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> AccountCarrier[T]:
        return cast(AccountCarrier[T], super().carrier)
    
    @property
    def blueprint(self) -> Optional[AccountBlueprint[T]]:
        return cast(AccountBlueprint[T], super().blueprint)