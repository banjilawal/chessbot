# src/domain/metadata/unions/context/account/machine/types.py

"""
Module: domain.metadata.unions.context.account.machine.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import MachineAccountContextBlueprint, MachineAccount, AccountContextTypeUnion
from transit import MachineAccountContextCarrier


class MachineAccountContextTypeUnion(AccountContextTypeUnion[MachineAccountContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            MachineAccount.

    Attributes:
        model: Type[MachineAccountContext]
        carrier: Type[MachineAccountContextCarrier]
        blueprint: Type[MachineAccountContextBlueprint]

    Provides:

    Super Class:
        AccountContextTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[MachineAccountContext]] | None = None,
            carrier: Optional[Type[MachineAccountContextCarrier]] | None = None,
            blueprint: Optional[Type[MachineAccountContextBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[MachineAccountContext]]
            carrier: Optional[Type[MachineAccountContextCarrier]
            blueprint: Optional[Type[MachineAccountContextBlueprint] 
        """
        super().__init__(
            model=model or MachineAccountContext, 
            carrier=carrier or MachineAccountContextCarrier, 
            blueprint=blueprint or MachineAccountContextBlueprint
        )
    
    @property
    def model(self) -> Type[MachineAccountContext]:
        return cast(Type[MachineAccountContext], super().model)
    
    @property
    def carrier(self) -> Type[MachineAccountContextCarrier]:
        return cast(Type[MachineAccountContextCarrier], super().contextCarrier)
    
    @property
    def blueprint(self) -> Type[MachineAccountContextBlueprint]:
        return cast(Type[MachineAccountContextBlueprint], super().contextBlueprint)