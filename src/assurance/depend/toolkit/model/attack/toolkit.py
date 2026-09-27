# src/assurance/depend/toolkit/model/attack/toolkit.py

"""
Module: assurance.depend.toolkit.model.attack.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, AttackWrapperDependency
from domain import Attack, AttackManifest, AttackNullGroup, AttackTypeUnion


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
            wrapper: Optional[AttackWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[AttackManifest]
            metadata: Optional[AttackHelperTable]
        """
        super().__init__(
            wrapper=wrapper or AttackWrapperDependency(),
            metadata=metadata or AttackManifest(),
        )
    
    @property
    def wrapper(self) -> AttackWrapperDependency:
        return cast(AttackWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> AttackManifest:
        return cast(AttackManifest, super().metadata)
    
    @property
    def nulls(self) -> AttackNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> AttackTypeUnion:
        return self.metadata.types