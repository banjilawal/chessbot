# src/domain/metadata/null/model/account/human/null.py

"""
Module: domain.metadata.null.model.account.human.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HumanAccount, AccountNullWarningSet
from err import HumanBlueprintNullException, HumanCarrierNullException, HumanNullException


class HumanAccountNullWarningSet(AccountNullWarningSet[HumanAccount]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a HumanAccount's integrity cycle.

    Attributes:
        model: HumanNullException
        carrier: HumanCarrierNullException
        blueprint: HumanBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[HumanNullException] | None = None,
            carrier: Optional[HumanCarrierNullException] | None = None,
            blueprint: Optional[HumanBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[HumanNullException]
            carrier: Optional[HumanCarrierNullException]
            blueprint: Optional[HumanBlueprintNullException]
        """
        super().__init__(
            model = model or HumanNullException(),
            carrier = carrier or HumanCarrierNullException(),
            blueprint = blueprint or HumanBlueprintNullException(),
        )
        
    @property
    def model(self) -> HumanNullException:
        return cast(HumanNullException, super().model)
    
    @property
    def carrier(self) -> HumanCarrierNullException:
        return cast(HumanCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> HumanBlueprintNullException:
        return cast(HumanBlueprintNullException, super().blueprint)