# src/domain/metadata/nulls/struct/node/warning/group.py

"""
Module: domain.metadata.nulls.struct.node.warning.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarningNode, NodeNullGroup
from err import EncounterWarningNodeCarrierNullException


class EncounterWarningNodeNullGroup(NodeNullGroup[EncounterWarningNode]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a EncounterWarningNode's integrity cycle.

    Attributes:
        model: EncounterWarningNodeNullException
        carrier: EncounterWarningNodeCarrierNullException
        blueprint:EncounterWarningNodeBlueprintNullException

    Provides:

    Super Class:
        NodeNullGroup
    """

    
    def __init__(
            self,
            model: Optional[EncounterWarningNodeNullException] | None = None,
            carrier: Optional[EncounterWarningNodeCarrierNullException] | None = None,
            blueprint: Optional[EncounterWarningNodeBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[EncounterWarningNodeNullException]
            carrier: Optional[EncounterWarningNodeCarrierNullException]
            blueprint: Optional[EncounterWarningNodeBlueprintNullException]
        """
        super().__init__(
            model=model or EncounterWarningNodeNullException(),
            carrier=carrier or EncounterWarningNodeCarrierNullException(),
            blueprint=blueprint or EncounterWarningNodeBlueprintNullException(),
        )
        
    @property
    def struct(self) -> EncounterWarningNodeNullException:
        return cast(EncounterWarningNodeNullException, super().model)
    
    @property
    def model(self) -> EncounterWarningNodeNullException:
        return self.struct
    
    @property
    def carrier(self) -> EncounterWarningNodeCarrierNullException:
        return cast(EncounterWarningNodeCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> EncounterWarningNodeBlueprintNullException:
        return cast(EncounterWarningNodeBlueprintNullException, super().blueprint)