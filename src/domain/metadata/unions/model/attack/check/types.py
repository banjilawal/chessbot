# src/domain/metadata/unions/model/attack/home/types.py

"""
Module: domain.metadata.unions.attack.home.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import Attack, AttackTypeUnion, CheckAttackWarning


class CheckAttackTypeUnion(AttackTypeUnion[CheckKingAttack]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CheckAttackWarning.

    Attributes:
        model: Type[CheckAttackWarning]
        carrier: Type[CheckAttackCarrier]
        blueprint: Type[CheckAttackBlueprint]

    Provides:

    Super Class:
        AttackTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CheckAttackWarning]] | None = None,
            carrier: Optional[Type[CheckAttackCarrier]] | None = None,
            blueprint: Optional[Type[CheckWarningBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CheckAttack]]
            carrier: Optional[Type[CheckAttackCarrier]]
            blueprint: Optional[Type[CheckAttackBlueprint]]
        """
        super().__init__(
            model=model or CheckAttackWarning,
            carrier=carrier or CheckAttackCarrier,
            blueprint=blueprint or CheckAttackBlueprint
        )
    
    @property
    def model(self) -> Type[CheckAttackWarning]:
        return cast(Type[CheckAttackWarning], super().model)
    
    @property
    def carrier(self) -> Type[CheckAttackCarrier]:
        return cast(Type[CheckAttackCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CheckAttackBlueprint]:
        return cast(Type[CheckAttackBlueprint], super().blueprint)