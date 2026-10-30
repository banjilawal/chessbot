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
from exchange import PermissionRequest, AttackPermissionRequest, AttackRequest


class AttackDecision(Decision[AttackRequest]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Attack transaction is permitted.

    Attributes:
        approval: Optional[AttackRequest]

    Provides:
        -   def grant(
                    approval: AttackRequest,
                    permission_request: PermissionRequest,
            ) -> AttackDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> AttackDecision

    Super Class:
        Decision
    """
    
    def __init__(
            self,
            permission: Permission,
            permission_request: AttackPermissionRequest,
            exception: Optional[Exception] | None = None,
            approval: Optional[AttackRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            permission_request: PermissionRequest
            exception: Optional[Exception]
            approval: Optional[AttackRequest]
        """
        super().__init__(
            permission_request=permission_request,
            approval=approval,
            exception=exception,
            permission=permission,
        )
    
    @property
    def permission_request(self) -> AttackPermissionRequest:
        return cast(AttackPermissionRequest, super().permission_request)
    
    @property
    def approval(self) -> Optional[AttackRequest]:
        return cast(AttackRequest, super().approval)
    
    @property
    def request_is_granted(self) -> bool:
        return (
                super().request_is_granted and 
                isinstance(self.approval, AttackRequest)
        )
    
    @property
    def request_is_denied(self) -> bool:
        return not self.request_is_granted
    
    @classmethod
    def grant(
            cls, 
            approval: AttackRequest, 
            permission_request: PermissionRequest,
    ) -> AttackDecision:
        role_request = cast(
            AttackPermissionRequest, 
            permission_request,
        )
        return cls(
            approval=approval,
            permission_request=role_request,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(
            cls, 
            permission_request: PermissionRequest,
            exception: Exception,
    ) -> AttackDecision:
        role_request = cast(
            AttackPermissionRequest,
            permission_request,
        )
        return cls(
            exception=exception,
            permission_request=role_request,
            permission=Permission.DENIED,
        )


    
