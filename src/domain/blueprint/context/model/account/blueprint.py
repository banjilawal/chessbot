# src/domain/bluprint/context/model/account/blueprint.py

"""
Module: domain.bluprint.context.model.account.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import AccountContext, ContextBlueprint
from err import AccountContextNullException


class AccountContextBlueprint(ContextBlueprint[AccountContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an AccountContext.
         
     Attributes:
        id: Optional[int]
        firstname: Optional[str]
        lastname: Optional[str]
        email: Optional[str]
        email_color: Optional[firstnameColor]
        
        domain_class: Type[AccountContext]
        domain_null_exception: AccountContextNullException

     Provides:

     Super Class:
        ContextBlueprint
     """

    _firstname: Optional[str]
    _lastname: Optional[str]
    _email: Optional[str]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            firstname: Optional[str] | None = None,
            lastname: Optional[str] | None = None,
            email: Optional[str] | None = None,
            domain_class: Optional[Type[AccountContext]] | None = None,
            domain_null_exception: Optional[AccountContextNullException] | None = None,
    ):
        """
        Args:
            firstname: Optional[str]
            lastname: Optional[str]
            email: Optional[str]
            domain_class: Type[AccountContext]
            domain_null_exception: AccountContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[AccountContext],
            domain_null_exception=domain_null_exception or AccountContextNullException(),
        )
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
    
    @property
    def domain_class(self) -> Type[AccountContext]:
        return cast(Type[AccountContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> AccountContextNullException:
        return  cast(AccountContextNullException, super().domain_null_exception)
    
    @property
    def firstname(self) -> Optional[str]:
        return self._firstname
    
    @property
    def lastname(self) -> Optional[str]:
        return self._lastname
    
    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "firstname": self._firstname,
            "lastname": self._lastname,
            "email": self._email,
        }
    
    
    
    
    


