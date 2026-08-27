# src/artifact/decision/request/decision.py

"""
Module: artfifact.decision.request.decision
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
        request: Request
        permission: Permission
        exception: Optional[Exception]

    Provides:
        - def grant(request: Request) -> RequestDecision
        - def deny(request: Request, exception: Exception) -> RequestDecision

    Super Class:
    """
    _request: Request
    
    def __init__(
            self,
            request: Request,
            permission: Permission,
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
    def request(self) -> Request:
        return self._request
    
    @classmethod
    def grant(cls, request: Request) -> RequestDecision:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def deny(cls, request: Request, exception: Exception) -> RequestDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.Denied,
        )

    
    
