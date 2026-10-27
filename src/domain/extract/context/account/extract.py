# src/domain/extract/context/account/extract.py

"""
Module: domain.extract.context.account.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import AccountContext, AccountContextBlueprint, ContextPrimeExtract
from transit import AccountContextCarrier


class AccountContextPrimeExtract(ContextPrimeExtract[AccountContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for AccountValidator.

    Attributes:
        contextCarrier: AccountContextCarrier
        blueprint: Optional[AccountContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: AccountContextCarrier,
            blueprint: Optional[AccountContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: AccountContextCarrier
            blueprint: Optional[AccountContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> AccountContextCarrier:
        return cast(AccountContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[AccountContextBlueprint]:
        return cast(AccountContextBlueprint, super().blueprint)