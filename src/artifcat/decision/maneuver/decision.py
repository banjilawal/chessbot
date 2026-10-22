# src/artifact/decision/maneuver/decision.py

"""
Module: artfifact.decision.maneuver.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision, Permission
from exchange import ManeuverRequest


class ManeuverDecision(Decision[ManeuverRequest]):
    """
    Role:
        - Authorization Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        request: ManeuverRequest
        permission: Permission
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(request: ManeuverRequest) -> ManeuverDecision
        -   def deny(request: ManeuverRequest, exception: Exception) -> ManeuverDecision

    Super Class:
        Decision
    """

  
    def __init__(
            self,
            permission: Permission,
            request: ManeuverRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: ManeuverRequest
            exception: Optional[Exception]
        """
        super().__init__(request=request, permission=permission, exception=exception)
    
    @property
    def request(self) -> ManeuverRequest:
        return cast(ManeuverRequest, super().request)
        

    @property
    def is_granted(self) -> bool:
        return super().is_granted and isinstance(self.request, ManeuverRequest)
    
    @property
    def is_denial(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant(cls, request: ManeuverRequest) -> ManeuverDecision:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def denial(cls, request: ManeuverRequest, exception: Exception) -> ManeuverDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def timed_out(cls, request: ManeuverRequest, exception: Exception) -> ManeuverDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.TIMED_OUT,
        )
    
    
