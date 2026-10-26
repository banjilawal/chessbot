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
        firstname: Optional[str]
        lastname: Optional[str]
        email: Optional[str]

    Provides:
        - to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """

    _email: Optional[str]
    _firstname: Optional[str]
    _lastname: Optional[str]
    
    def ___init__(
            self,
            id: Optional[int] | None = None,
            email: Optional[str] | None = None,
            firstname: Optional[str] | None = None,
            lastname: Optional[str] | None = None,
    ):
        """
        Args:
            email: Optional[str]
            firstname: Optional[str]
            lastname: Optional[str]
        """
        super().__init__(id=id)
        self._email = email
        self._firstname = firstname
        self._lastname = lastname
        
    @property
    def email(self) -> Optional[str]:
        return self._email
    
    @property
    def firstname(self) -> Optional[str]:
        return self._firstname
    
    @property
    def lastname(self) -> Optional[str]:
        return self._lastname
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "email": self._email,
            "firstname": self._firstname,
            "lastname": self._lastname,
        }
