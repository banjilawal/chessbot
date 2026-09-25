# src/assurance/toolkit/model/attack/toolkit.py

"""
Module: assurance.toolkit.model.attack.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, AttackHelperTable
from domain import Attack, AttackManifest


class AttackValidatorToolkit(ModelValidatorToolkit[Attack]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Attack attribute validators and type metadata.

    Attributes:
        helper: AttackManifest
        metadata: AttackHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
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
        super().__init__(
            helper=helper or AttackHelperTable(),
            metadata=metadata or AttackManifest(),
        )
    
    @property
    def attribute(self) -> AttackHelperTable:
        return cast(AttackHelperTable, super().attribute)
    
    @property
    def metadata(self) -> AttackManifest:
        return cast(AttackManifest, super().metadata)