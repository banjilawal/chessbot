# src/domain/metadata/blueprint/model/state/account/machine/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.account.machine.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import MachineAccount, AccountBlueprint
from err import MachineAccountNullException


class MachineAccountBlueprint(AccountBlueprint):
    """
    Role:
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a MachineAccount object.
    
    Attributes:
        name: str
        id: Optional[int]
        
        domain_class: Type[MachineAccount]
        domain_null_exception: MachineAccountNullException
    
    Provides:
    
    Super Class:
        AccountBlueprint
    """
    _name: str
    
    def __init__(self,
            name: str,
            domain_class: Optional[Type[MachineAccount]] | None = None,
            domain_null_exception: Optional[MachineAccountNullException] | None = None,
            id: Optional[int] | None = None,
        ):
        """
        Args:
            name: str
            domain_class: Optional[Type[MachineAccount]]
            domain_null_exception: Optional[MachineAccountNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            name=name,
            domain_class=domain_class or MachineAccount,
            domain_null_exception=domain_null_exception or MachineAccountNullException(),
        )
        self._name = name
        
    @property
    def name(self) -> str:
        return self._name
        

    @property
    def domain_class(self) -> Type[MachineAccount]:
        return cast(Type[MachineAccount], super().domain_class)
    
    @property
    def domain_null_exception(self) -> MachineAccountNullException:
        return cast(MachineAccountNullException, super().domain_null_exception)