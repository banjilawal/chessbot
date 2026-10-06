# src/domain/extract/model/account/human.extract.py

"""
Module: domain.extract.model.account.human.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HumanAccount, HumanAccountBlueprint, AccountPrimeExtract
from transit import HumanAccountCarrier


class HumanAccountPrimeExtract(AccountPrimeExtract[HumanAccount]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for HumanAccountValidator.

    Attributes:
        carrier: HumanAccountCarrier
        blueprint: Optional[HumanAccountBlueprint]

    Provides:

    Super Class:
        AccountPrimeExtract
    """

    def __init__(
            self,
            reference: HumanAccountCarrier,
            safe_blueprint: Optional[HumanAccountBlueprint] | None = None,
    ):
        """
        Args:
            reference: HumanAccountCarrier
            safe_blueprint: Optional[HumanAccountBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> HumanAccountCarrier:
        return cast(HumanAccountCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[HumanAccountBlueprint]:
        return cast(HumanAccountBlueprint, super().blueprint)