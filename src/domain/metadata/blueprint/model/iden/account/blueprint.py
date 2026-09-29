# src/domain/metadata/blueprint/model/iden/account/blueprint.py

"""
Module: domain.metadata.blueprint.model.iden.account.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar, cast

from domain import Account, IdentifiableModelBlueprint
from err import AccountNullException
from game import GameAdviser

T = TypeVar("T", bound="Account")

class AccountBlueprint(IdentifiableModelBlueprint[T], Generic[T]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Account object.

    Attributes:
        id: Optional[int]
        
        domain_class: Type[Account]
        search_context_class: Type[AccountContext]
        domain_null_exception: AccountNullException

    Provides:

     Super Class:
        IdentifiableModelBlueprint
     """
    
    def __init__(self,
            domain_class: Optional[Type[T]] | None = None,
            domain_null_exception: Optional[AccountNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[T]]
            domain_null_exception: Optional[AccountNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[T],
            domain_null_exception=domain_null_exception or AccountNullException(),
        )
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> AccountNullException:
        return cast(AccountNullException, super().domain_null_exception)
    
    