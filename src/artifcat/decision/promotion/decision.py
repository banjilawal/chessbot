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
from exchange import PermissionRequest, PromotionPermissionRequest, PromotionRequest


class PromotionDecision(Decision[PromotionPermissionRequest, PromotionRequest]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Promotion transaction is permitted.

    Attributes:
        approval: Optional[PromotionRequest]

    Provides:
        -   def grant(
                    approval: PromotionRequest,
                    permission_request: PermissionRequest,
            ) -> PromotionDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> PromotionDecision

    Super Class:
        Decision
    """
    
    def __init__(
            self,
            permission: Permission,
            permission_request: PromotionPermissionRequest,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[PromotionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            permission_request: PermissionRequest
            exception: Optional[Exception]
            transaction_request: Optional[PromotionRequest]
        """
        super().__init__(
            permission_request=permission_request,
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
        )
    
    @property
    def permission_request(self) -> PromotionPermissionRequest:
        return cast(PromotionPermissionRequest, super().permission_request)
    
    @property
    def transaction_request(self) -> Optional[PromotionRequest]:
        return cast(PromotionRequest, super().transaction_request)
    
    @property
    def request_is_granted(self) -> bool:
        return (
                super().request_is_granted and 
                isinstance(self.transaction_request, PromotionRequest)
        )
    
    @property
    def request_is_denied(self) -> bool:
        return not self.request_is_granted
    #
    # @classmethod
    # def grant(
    #         cls,
    #         approval: PromotionRequest,
    #         permission_request: PermissionRequest,
    # ) -> PromotionDecision:
    #     # role_request = cast(
    #     #     PromotionPermissionRequest,
    #     #     permission_request,
    #     # )
    #     return cls(
    #         approval=approval,
    #         permission_request=permission_request,
    #         permission=Permission.GRANTED,
    #     )
    #
    # @classmethod
    # def denial(
    #         cls,
    #         permission_request: PermissionRequest,
    #         exception: Exception,
    # ) -> PromotionDecision:
    #     role_request = cast(
    #         PromotionPermissionRequest,
    #         permission_request,
    #     )
    #     return cls(
    #         exception=exception,
    #         permission_request=role_request,
    #         permission=Permission.DENIED,
    #     )
    #

    
