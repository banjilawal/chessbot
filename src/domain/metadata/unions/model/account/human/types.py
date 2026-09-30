# src/domain/metadata/unions/model/account/human/types.py

"""
Module: domain.metadata.unions.account.human.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import HumanAccountBlueprint, HumanAccount, AccountTypeUnion
from transit import HumanAccountCarrier


class HumanAccountTypeUnion(AccountTypeUnion[HumanAccount]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            HumanAccount.

    Attributes:
        model: Type[HumanAccount]
        carrier: Type[HumanAccountCarrier]
        blueprint: Type[HumanAccountBlueprint]

    Provides:

    Super Class:
        AccountTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[HumanAccount]] | None = None,
            carrier: Optional[Type[HumanAccountCarrier]] | None = None, 
            blueprint: Optional[Type[HumanAccountBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[HumanAccount]]
            carrier: Optional[Type[HumanAccountCarrier]
            blueprint: Optional[Type[HumanAccountBlueprint] 
        """
        super().__init__(
            model=model or HumanAccount,
            carrier=carrier or HumanAccountCarrier, 
            blueprint=blueprint or HumanAccountBlueprint
        )
    
    @property
    def model(self) -> Type[HumanAccount]:
        return cast(Type[HumanAccount], super().model)
    
    @property
    def carrier(self) -> Type[HumanAccountCarrier]:
        return cast(Type[HumanAccountCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[HumanAccountBlueprint]:
        return cast(Type[HumanAccountBlueprint], super().blueprint)