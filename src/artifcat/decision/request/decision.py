# src/artifact/decision/decision.py

"""
Module: artfifact.decision.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision, Permission
from domain import Request


class RequestDecision(Decision):
    """
    Role:
        - Authorization Reporting

    Responsibilities:
        1.  Report if an Authorizer grants a Request.

    Attributes:
        permission: Permission
        request: Optional[Request]
        exception: Optional[Exception]
        is_denied: bool
        is_granted

    Provides:
        - def grant(request: T) -> RequestDecision

    Super Class:
    """
    _request: Request

    
    def __init__(
            self,
            permission: Permission,
            request: Optional[Request] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: Optional[Request]
            exception: Optional[Exception]
        """
        super().__init__(permission=permission, exception=exception)
        self._request = request
    
    @property
    def request(self) -> Optional[Request]:
        return self._request
    
    @property
    def permission(self) -> Permission:
        return self._permission
    
    @property
    def is_denied(self) -> bool:
        return self._request is None and super().is_denied
    
    @property
    def is_granted(self) -> bool:
        return  self._request is not None and super().is_granted
    
    @classmethod
    def grant(cls, request: Request) -> RequestDecision:
        return cls(request=request, permission =Permission.GRANTED)
    
    @classmethod
    def deny(cls, exception: Exception) -> RequestDecision:
        return cast(RequestDecision, super().deny(exception))

    
    
