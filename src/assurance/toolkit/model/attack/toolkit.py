# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import AttackHelperTable, ModelValidationToolkit
from domain import Attack, AttackManifest



class AttackValidationToolkit(ModelValidationToolkit[Attack]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Attack attribute validators and type metadata.

    Attributes:
        helper: Optional[AttackManifest]
        metadata: Optional[AttackHelperTable]

    Provides:

    Super Class:
    """
    _metadata: AttackManifest
    _helper: AttackHelperTable
    
    def __init__(
            self,
            metadata: Optional[AttackManifest] | None = None,
            helper: Optional[AttackHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[AttackManifest]
            metadata: Optional[AttackHelperTable]
        """
        self._helper = helper or AttackHelperTable()
        self._metadata = metadata or AttackManifest()
    
    @property
    def helper(self) -> AttackHelperTable:
        return cast(AttackHelperTable, super().helper)
    
    @property
    def metadata(self) -> AttackManifest:
        return cast(AttackManifest, super().metadata)
