# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ManeuverHelperTable, ModelValidationToolkit
from domain import Maneuver, ManeuverManifest



class ManeuverValidationToolkit(ModelValidationToolkit[Maneuver]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Maneuver attribute validators and type metadata.

    Attributes:
        helper: Optional[ManeuverManifest]
        metadata: Optional[ManeuverHelperTable]

    Provides:

    Super Class:
    """
    _metadata: ManeuverManifest
    _helper: ManeuverHelperTable
    
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
        self._helper = helper or ManeuverHelperTable()
        self._metadata = metadata or ManeuverManifest()
    
    @property
    def helper(self) -> ManeuverHelperTable:
        return cast(ManeuverHelperTable, super().helper)
    
    @property
    def metadata(self) -> ManeuverManifest:
        return cast(ManeuverManifest, super().metadata)
