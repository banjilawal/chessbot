# src/domain/metadata/unions/model/attack/check/types.py

"""
Module: domain.metadata.unions.attack.check.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import AttackTypeUnion, EncounterWarning, CheckWarningBlueprint
from transit import CheckWarningCarrier


class CheckWarningTypeUnion(AttackModelTypeUnion[EncounterWarning]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CheckWarning.

    Attributes:
        model: Type[CheckWarning]
        carrier: Type[CheckWarningCarrier]
        blueprint: Type[CheckWarningBlueprint]

    Provides:

    Super Class:
        AttackTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[EncounterWarning]] | None = None,
            carrier: Optional[Type[CheckWarningCarrier]] | None = None,
            blueprint: Optional[Type[CheckWarningBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[CheckWarning]]
            carrier: Optional[Type[CheckWarningCarrier]]
            blueprint: Optional[Type[CheckWarningBlueprint]]
        """
        super().__init__(
            model=model or EncounterWarning,
            carrier=carrier or CheckWarningCarrier,
            blueprint=blueprint or CheckWarningBlueprint
        )
    
    @property
    def model(self) -> Type[EncounterWarning]:
        return cast(Type[EncounterWarning], super().model)
    
    @property
    def carrier(self) -> Type[CheckWarningCarrier]:
        return cast(Type[CheckWarningCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[CheckWarningBlueprint]:
        return cast(Type[CheckWarningBlueprint], super().blueprint)