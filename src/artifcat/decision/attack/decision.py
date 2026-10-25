# src/artifact/decision/attack/decision.py

"""
Module: artfifact.decision.attack.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision, Permission
from exchange import AttackPermissionRequest, AttackRequest


class AttackDecision(Decision[AttackPermissionRequest]):
    """
    Role:
        - Authorization Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        permission: Permission
        exception: Optional[Exception]
        request: AttackAuthorizationRequest
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(request: AttackRequest) -> AttackDecision
        -   def deny(request: AttackRequest, exception: Exception) -> AttackDecision

    Super Class:
        Decision
    """

  
    def __init__(
            self,
            permission: Permission,
            request: AttackRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: AttackRequest
            exception: Optional[Exception]
        """
        super().__init__(request=request, permission=permission, exception=exception)
    
    @property
    def request(self) -> AttackRequest:
        return cast(AttackRequest, super().request)
        

    @property
    def is_granted(self) -> bool:
        return super().is_granted and isinstance(self.request, AttackRequest)
    
    @property
    def is_denial(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant(cls, request: AttackRequest) -> AttackDecision:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def denial(cls, request: AttackRequest, exception: Exception) -> AttackDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def timed_out(cls, request: AttackRequest, exception: Exception) -> AttackDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.TIMED_OUT,
        )
    
    
