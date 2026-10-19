# src/artifact/decision/promotion/decision.py

"""
Module: artfifact.decision.promotion.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision, Permission
from exchange import PromotionRequest


class PromotionDecision(Decision[PromotionRequest]):
    """
    Role:
        - Authorization Reporting

    Responsibilities:
        1.  Report if an action is permitted.
        
    Attributes:
        request: PromotionRequest
        permission: Permission
        exception: Optional[Exception]
        
        is_granted: bool
        is_denied: bool
        
    Provides:
        -   def grant(request: PromotionRequest) -> PromotionDecision
        -   def deny(request: PromotionRequest, exception: Exception) -> PromotionDecision

    Super Class:
        Decision
    """

  
    def __init__(
            self,
            permission: Permission,
            request: PromotionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            request: PromotionRequest
            exception: Optional[Exception]
        """
        super().__init__(request=request, permission=permission, exception=exception)
    
    @property
    def request(self) -> PromotionRequest:
        return cast(PromotionRequest, super().request)
        

    @property
    def is_granted(self) -> bool:
        return super().is_granted and isinstance(self.request, PromotionRequest)
    
    @property
    def is_denied(self) -> bool:
        return not self.is_granted
    
    @classmethod
    def grant(cls, request: PromotionRequest) -> PromotionDecision:
        return cls(request=request, permission=Permission.GRANTED)
    
    @classmethod
    def deny(cls, request: PromotionRequest, exception: Exception) -> PromotionDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.DENIED,
        )
    
    @classmethod
    def timed_out(cls, request: PromotionRequest, exception: Exception) -> PromotionDecision:
        return cls(
            request=request,
            exception=exception,
            permission=Permission.TIMED_OUT,
        )
    
    
