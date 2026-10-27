# src/domain/context/model/account/context.py

"""
Module: domain.context.model.account.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Account, Context


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
        human_account: Optional[bool]
        machine_account: Optional[bool]

    Provides:
        - to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """

    _email: Optional[str]
    _firstname: Optional[str]
    _lastname: Optional[str]
    _machine_name: Optional[str]
    _human_account: Optional[bool]
    _machine_account: Optional[bool]
    
    def ___init__(
            self,
            id: Optional[int] | None = None,
            email: Optional[str] | None = None,
            firstname: Optional[str] | None = None,
            lastname: Optional[str] | None = None,
            machine_name: Optional[str] | None = None,
            human_account: Optional[bool] | None = None,
            machine_account: Optional[bool] | None = None,
    ):
        """
        Args:
            email: Optional[str]
            firstname: Optional[str]
            lastname: Optional[str]
            machine_name: Optional[str]
            human_account: Optional[str]
            machine_account: Optional[str
        """
        super().__init__(id=id)
        self._email = email
        self._lastname = lastname
        self._firstname = firstname
        self._machine_name = machine_name
        self._human_account = human_account
        self._machine_account = machine_account
        
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
    def human_account(self) -> Optional[bool]:
        return self._human_account
    
    @property
    def machine_account(self) -> Optional[bool]:
        return self._machine_account
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "email": self._email,
            "lastname": self._lastname,
            "firstname": self._firstname,
            "machine_name": self._machine_name,
            "human_account": self._human_account,
            "machine_account": self._machine_account,
        }
