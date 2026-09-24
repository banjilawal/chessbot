# src/domain/metadata/manifest/model/attack/mate/manifest.py

"""
Module: domain.metadata.manifest.model.attack.mate.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    CheckmateAttackNullGroup, CheckmateAttack, AttackManifest, CheckmateAttackTypeUnion
)


class CheckcheckmateAttackManifest(AttackManifest[CheckmateAttack]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the CheckmateAttack
            security lifecycle.

     Attributes:
        types: CheckmateAttackTypeUnion
        nulls: CheckmateAttackNullGroup

     Provides:

     Super Class:
        AttackManifest
     """
    
    def __init__(
            self,
            types: Optional[CheckmateAttackTypeUnion] | None = None,
            nulls: Optional[CheckmateAttackNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CheckmateAttackTypeUnion]
            nulls: Optional[CheckmateAttackNullGroup]
        """
        super().__init__(
            types=types or CheckmateAttackTypeUnion(),
            nulls=nulls or CheckmateAttackNullGroup(),
        )
    
    @property
    def types(self) -> CheckmateAttackTypeUnion:
        return cast(CheckmateAttackTypeUnion, super().types)
    
    @property
    def nulls(self) -> CheckmateAttackNullGroup:
        return cast(CheckmateAttackNullGroup, super().nulls)