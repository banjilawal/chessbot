# src/domain/metadata/nulls/context/account/human/group.py

"""
Module: domain.metadata.nulls.context.account.human.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HumanAccount, AccountContextNullGroup
from err import HumanContextBlueprintNullException, HumanContextCarrierNullException, HumanContextNullException


class HumanAccountContextNullGroup(AccountContextNullGroup[HumanAccountContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a HumanAccount's integrity cycle.

    Attributes:
        model: HumanContextNullException
        carrier: HumanContextCarrierNullException
        blueprint: HumanContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[HumanContextNullException] | None = None,
            carrier: Optional[HumanContextCarrierNullException] | None = None,
            blueprint: Optional[HumanContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[HumanContextNullException]
            carrier: Optional[HumanContextCarrierNullException]
            blueprint: Optional[HumanContextBlueprintNullException]
        """
        super().__init__(
            model=model or HumanContextNullException(),
            carrier=carrier or HumanContextCarrierNullException(),
            blueprint=blueprint or HumanContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> HumanContextNullException:
        return cast(HumanContextNullException, super().model)
    
    @property
    def carrier(self) -> HumanContextCarrierNullException:
        return cast(HumanContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> HumanContextBlueprintNullException:
        return cast(HumanContextBlueprintNullException, super().blueprint)