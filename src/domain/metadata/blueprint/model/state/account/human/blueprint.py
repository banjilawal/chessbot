# src/domain/metadata/blueprint/model/state/account/human/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.account.human.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, Optional, Type, cast

from domain import HumanAccount, AccountBlueprint
from err import HumanAccountNullException
from software import Subscriber


class HumanAccountBlueprint(AccountBlueprint[HumanAccount]):
    """
    Role:
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a HumanAccount object.
    
    Attributes:
        firstname: str
        lastname: str
        domain_class: Type[HumanAccount]
        domain_null_exception: HumanAccountNullException
    
    Provides:
    
    Super Class:
        AccountBlueprint
    """
    _firstname: str
    _lastname: str
    
    def __init__(self,
            firstname: str,
            lastname: str,
            domain_class: Optional[Type[HumanAccount]] | None = None,
            domain_null_exception: Optional[HumanAccountNullException] | None = None,
            id: Optional[int] | None = None,
        ):
        """
        Args:
            firstname: str
            lastname: str
            domain_class: Optional[Type[HumanAccount]]
            domain_null_exception: Optional[HumanAccountNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or HumanAccount,
            domain_null_exception=domain_null_exception or HumanAccountNullException(),
        )
        self._firstname = firstname
        self._lastname = lastname
        
    @property
    def firstname(self) -> str:
        return self._firstname
    
    @property
    def lastname(self) -> str:
        return self._lastname
    
    @property
    def names_dict(self) -> Dict[str, str]:
        return {"firstname": self._firstname, "lastname": self._lastname}

    @property
    def domain_class(self) -> Type[HumanAccount]:
        return cast(Type[HumanAccount], super().domain_class)
    
    @property
    def domain_null_exception(self) -> HumanAccountNullException:
        return cast(HumanAccountNullException, super().domain_null_exception)