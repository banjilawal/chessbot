# src/domain/metadata/nulls/model/encounter/checkmate/group.py

"""
Module: domain.metadata.nulls.model.encounter.checkmate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckmateEncounter, EncounterNullGroup
from err import (
    CheckmateEncounterBlueprintNullException, CheckmateEncounterCarrierNullException,
    CheckmateEncounterNullException
)


class CheckmateEncounterNullGroup(EncounterNullGroup[CheckmateEncounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CheckmateEncounter's integrity cycle.

    Attributes:
        model: CheckmateEncounterNullException
        carrier: CheckmateEncounterCarrierNullException
        blueprint: CheckmateEncounterBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[CheckmateEncounterNullException] | None = None,
            carrier: Optional[CheckmateEncounterCarrierNullException] | None = None,
            blueprint: Optional[CheckmateEncounterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CheckmateEncounterNullException]
            carrier: Optional[CheckmateEncounterCarrierNullException]
            blueprint: Optional[CheckmateEncounterBlueprintNullException]
        """
        super().__init__(
            model =model or CheckmateEncounterNullException(),
            carrier =carrier or CheckmateEncounterCarrierNullException(),
            blueprint =blueprint or CheckmateEncounterBlueprintNullException(),
        )
        
    @property
    def model(self) -> CheckmateEncounterNullException:
        return cast(CheckmateEncounterNullException, super().model)
    
    @property
    def carrier(self) -> CheckmateEncounterCarrierNullException:
        return cast(CheckmateEncounterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CheckmateEncounterBlueprintNullException:
        return cast(CheckmateEncounterBlueprintNullException, super().blueprint)