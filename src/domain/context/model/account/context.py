# src/domain/context/model/account/context.py

"""
Module: domain.context.model.account.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Account, AccountType, Context


class AccountContext(Context[Account]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply AccountSearcher with targeting criteria.

    Attributes:
        id: Optional[int]
        email: Optional[str]
        lastname: Optional[str]
        firstname: Optional[str]
        machine_name: Optional[str]
        account_type: Optional[AccountType]

    Provides:
        - to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """

    _email: Optional[str]
    _firstname: Optional[str]
    _lastname: Optional[str]
    _machine_name: Optional[str]
    _account_type: Optional[AccountType]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            email: Optional[str] | None = None,
            firstname: Optional[str] | None = None,
            lastname: Optional[str] | None = None,
            machine_name: Optional[str] | None = None,
            account_type: Optional[AccountType] | None = None,
    ):
        """
        Args:
            email: Optional[str]
            firstname: Optional[str]
            lastname: Optional[str]
            machine_name: Optional[str]
            account_type: Optional[AccountType]
        """
        super().__init__(id=id)
        self._email = email
        self._lastname = lastname
        self._firstname = firstname
        self._machine_name = machine_name
        self._account_type = account_type
        
    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @property
    def firstname(self) -> Optional[str]:
        return self._firstname
    
    @property
    def lastname(self) -> Optional[str]:
        return self._lastname
    
    @property
    def machine_name(self) -> Optional[str]:
        return self._machine_name
    
    @property
    def account_type(self) -> Optional[AccountType]:
        return self._account_type
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "email": self._email,
            "lastname": self._lastname,
            "firstname": self._firstname,
            "machine_name": self._machine_name,
            "account_type": self._account_type,
        }
