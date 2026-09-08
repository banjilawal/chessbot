# src/domain/metadata/nulls/model/walk/maneuver/group.py

"""
Module: domain.metadata.nulls.model.walk.maneuver.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import ManeuverBlueprintNullException, ManeuverCarrierNullException, ManeuverNullException


class ManeuverNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Maneuver's integrity cycle.

    Attributes:
        model: ManeuverNullException
        carrier: ManeuverCarrierNullException
        blueprint: ManeuverBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[ManeuverNullException] | None = None,
            carrier: Optional[ManeuverCarrierNullException] | None = None,
            blueprint: Optional[ManeuverBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[ManeuverNullException]
            carrier: Optional[ManeuverCarrierNullException]
            blueprint: Optional[ManeuverBlueprintNullException]
        """
        super().__init__(
            model = model or ManeuverNullException(),
            carrier = carrier or ManeuverCarrierNullException(),
            blueprint = blueprint or ManeuverBlueprintNullException(),
        )
        
    @property
    def model(self) -> ManeuverNullException:
        return cast(ManeuverNullException, super().model)
    
    @property
    def carrier(self) -> ManeuverCarrierNullException:
        return cast(ManeuverCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ManeuverBlueprintNullException:
        return cast(ManeuverBlueprintNullException, super().blueprint)