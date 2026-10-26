# src/domain/metadata/nulls/context/maneuver/group.py

"""
Module: domain.metadata.nulls.context.maneuver.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Maneuver, ContextNullWarningSet
from err import (
    ManeuverContextBlueprintNullException, ManeuverContextCarrierNullException, ManeuverContextNullException
)


class ManeuverContextNullWarningSet(ContextNullWarningSet[ManeuverContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Maneuver's integrity cycle.

    Attributes:
        model: ManeuverContextNullException
        carrier: ManeuverContextCarrierNullException
        blueprint: ManeuverContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[ManeuverContextNullException] | None = None,
            carrier: Optional[ManeuverContextCarrierNullException] | None = None,
            blueprint: Optional[ManeuverContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[ManeuverContextNullException]
            carrier: Optional[ManeuverContextCarrierNullException]
            blueprint: Optional[ManeuverContextBlueprintNullException]
        """
        super().__init__(
            model=model or ManeuverContextNullException(),
            carrier=carrier or ManeuverContextCarrierNullException(),
            blueprint=blueprint or ManeuverContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> ManeuverContextNullException:
        return cast(ManeuverContextNullException, super().model)
    
    @property
    def carrier(self) -> ManeuverContextCarrierNullException:
        return cast(ManeuverContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ManeuverContextBlueprintNullException:
        return cast(ManeuverContextBlueprintNullException, super().blueprint)