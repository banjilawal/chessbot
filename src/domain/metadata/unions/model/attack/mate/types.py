# src/domain/metadata/unions/model/attack/mate/types.py

"""
Module: domain.metadata.unions.attack.mate.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import AttackTypeUnion, CheckmateAttack, CheckmateAttackBlueprint
from transit import CheckmateAttackCarrier


class CheckmateAttackTypeUnion(AttackModelTypeUnion[CheckmateAttack]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating 
            a CheckmateAttack.

    Attributes:
        model: Type[CheckmateAttack]
        carrier: Type[CheckmateAttackCarrier]
        blueprint: Type[CheckmateAttackBlueprint]

    Provides:

    Super Class:
        AttackTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[CheckmateAttack]] | None = None,
            carrier: Optional[Type[CheckmateAttackCarrier]] | None = None,
            blueprint: Optional[Type[CheckmateWarningBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CheckmateAttack]]
            carrier: Optional[Type[CheckmateAttackCarrier]]
            blueprint: Optional[Type[CheckmateAttackBlueprint]]
        """
        super().__init__(
            model=model or CheckmateAttack,
            carrier=carrier or CheckmateAttackCarrier,
            blueprint=blueprint or CheckmateAttackBlueprint
        )
    
    @property
    def model(self) -> Type[CheckmateAttack]:
        return cast(Type[CheckmateAttack], super().model)
    
    @property
    def carrier(self) -> Type[CheckmateAttackCarrier]:
        return cast(Type[CheckmateAttackCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CheckmateAttackBlueprint]:
        return cast(Type[CheckmateAttackBlueprint], super().blueprint)