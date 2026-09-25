# src/assurance/toolkit/model/maneuver/toolkit.py

"""
Module: assurance.toolkit.model.maneuver.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, ManeuverHelperTable
from domain import Maneuver, ManeuverManifest


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
            helper: Optional[ManeuverHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[ManeuverManifest]
            metadata: Optional[ManeuverHelperTable]
        """
        super().__init__(
            helper=helper or ManeuverHelperTable(),
            metadata=metadata or ManeuverManifest(),
        )
    
    @property
    def attribute(self) -> ManeuverHelperTable:
        return cast(ManeuverHelperTable, super().attribute)
    
    @property
    def metadata(self) -> ManeuverManifest:
        return cast(ManeuverManifest, super().metadata)