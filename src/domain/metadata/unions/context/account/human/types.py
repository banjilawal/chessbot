# src/domain/metadata/unions/context/account/human/types.py

"""
Module: domain.metadata.unions.context.account.human.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import HumanAccountContextBlueprint, HumanAccount, AccountContextTypeUnion
from transit import HumanAccountContextCarrier


class HumanAccountContextTypeUnion(AccountContextTypeUnion[HumanAccountContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            HumanAccount.

    Attributes:
        model: Type[HumanAccountContext]
        carrier: Type[HumanAccountContextCarrier]
        blueprint: Type[HumanAccountContextBlueprint]

    Provides:

    Super Class:
        AccountContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[HumanAccountContext]] | None = None,
            carrier: Optional[Type[HumanAccountContextCarrier]] | None = None,
            blueprint: Optional[Type[HumanAccountContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[HumanAccountContext]]
            carrier: Optional[Type[HumanAccountContextCarrier]
            blueprint: Optional[Type[HumanAccountContextBlueprint] 
        """
        super().__init__(
            model=model or HumanAccountContext, 
            carrier=carrier or HumanAccountContextCarrier, 
            blueprint=blueprint or HumanAccountContextBlueprint
        )
    
    @property
    def model(self) -> Type[HumanAccountContext]:
        return cast(Type[HumanAccountContext], super().model)
    
    @property
    def carrier(self) -> Type[HumanAccountContextCarrier]:
        return cast(Type[HumanAccountContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[HumanAccountContextBlueprint]:
        return cast(Type[HumanAccountContextBlueprint], super().contextBlueprint)