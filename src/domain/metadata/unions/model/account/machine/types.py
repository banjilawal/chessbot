# src/domain/metadata/unions/model/account/machine/types.py

"""
Module: domain.metadata.unions.account.machine.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import MachineAccountBlueprint, MachineAccount, AccountTypeUnion
from transit import MachineAccountCarrier


class MachineAccountTypeUnion(AccountTypeUnion[MachineAccount]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            MachineAccount.

    Attributes:
        model: Type[MachineAccount]
        carrier: Type[MachineAccountCarrier]
        blueprint: Type[MachineAccountBlueprint]

    Provides:

    Super Class:
        AccountTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[MachineAccount]] | None = None,
            carrier: Optional[Type[MachineAccountCarrier]] | None = None, 
            blueprint: Optional[Type[MachineAccountBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[MachineAccount]]
            carrier: Optional[Type[MachineAccountCarrier]
            blueprint: Optional[Type[MachineAccountBlueprint] 
        """
        super().__init__(
            model=model or MachineAccount,
            carrier=carrier or MachineAccountCarrier, 
            blueprint=blueprint or MachineAccountBlueprint
        )
    
    @property
    def model(self) -> Type[MachineAccount]:
        return cast(Type[MachineAccount], super().model)
    
    @property
    def carrier(self) -> Type[MachineAccountCarrier]:
        return cast(Type[MachineAccountCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[MachineAccountBlueprint]:
        return cast(Type[MachineAccountBlueprint], super().blueprint)