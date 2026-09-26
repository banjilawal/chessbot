# src/assurance/toolkit/model/maneuver/toolkit.py

"""
Module: assurance.toolkit.model.maneuver.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, ManeuverValidationWrapperDict
from domain import Maneuver, ManeuverManifest, ManeuverNullGroup, ManeuverTypeUnion


class ManeuverValidatorToolkit(ModelValidatorToolkit[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Maneuver attribute validators and type metadata.

    Attributes:
        helper: ManeuverManifest
        metadata: ManeuverHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[ManeuverManifest] | None = None,
            wrapper: Optional[ManeuverValidationWrapperDict] | None = None,
    ):
        """
        Args:
            wrapper: Optional[ManeuverManifest]
            metadata: Optional[ManeuverHelperTable]
        """
        super().__init__(
            wrapper=wrapper or ManeuverValidationWrapperDict(),
            metadata=metadata or ManeuverManifest(),
        )
    
    @property
    def wrapper(self) -> ManeuverValidationWrapperDict:
        return cast(ManeuverValidationWrapperDict, super().wrapper)
    
    @property
    def metadata(self) -> ManeuverManifest:
        return cast(ManeuverManifest, super().metadata)
    
    @property
    def nulls(self) -> ManeuverNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> ManeuverTypeUnion:
        return self.metadata.types