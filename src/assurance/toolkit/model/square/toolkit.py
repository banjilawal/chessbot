# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import SquareHelperTable, ModelValidatorToolkit
from domain import Square, SquareManifest



class SquareValidatorToolkit(ModelValidatorToolkit[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Square attribute validators and type metadata.

    Attributes:
        helper: Optional[SquareManifest]
        metadata: Optional[SquareHelperTable]

    Provides:

    Super Class:
    """
    _metadata: SquareManifest
    _helper: SquareHelperTable
    
    def __init__(
            self,
            metadata: Optional[SquareManifest] | None = None,
            helper: Optional[SquareHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[SquareManifest]
            metadata: Optional[SquareHelperTable]
        """
        super().__init__(
            helper=helper or SquareHelperTable(),
            metadata=metadata or SquareManifest(),
        )
    
    @property
    def helper(self) -> SquareHelperTable:
        return cast(SquareHelperTable, super().helper)
    
    @property
    def metadata(self) -> SquareManifest:
        return cast(SquareManifest, super().metadata)
