# src/domain/metadata/blueprint/model/state/account/human/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.account.human.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

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
        subscriber: Subscriber
        
        domain_class: Type[HumanAccount]
        domain_null_exception: HumanAccountNullException
    
    Provides:
    
    Super Class:
        AccountBlueprint
    """
    
    def __init__(self,
            subscriber: Subscriber,
            domain_class: Optional[Type[HumanAccount]] | None = None,
            domain_null_exception: Optional[HumanAccountNullException] | None = None,
            id: Optional[int] | None = None,
        ):
        """
        Args:
            subscriber: Subscriber
            domain_class: Optional[Type[HumanAccount]]
            domain_null_exception: Optional[HumanAccountNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or HumanAccount,
            domain_null_exception=domain_null_exception or HumanAccountNullException(),
        )
        self._subscriber = subscriber
        
    @property
    def subscriber(self) -> Subscriber:
        return self._subscriber

    @property
    def domain_class(self) -> Type[HumanAccount]:
        return cast(Type[HumanAccount], super().domain_class)
    
    @property
    def domain_null_exception(self) -> HumanAccountNullException:
        return cast(HumanAccountNullException, super().domain_null_exception)