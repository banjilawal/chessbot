# src/operation/attack/attacker.py

"""
Module: operation.attack.attacker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import AttackResult
from domain import Encounter
from exchange import AttackAuthorizationResponder, AttackPermissionRequest, AttackRequest, AuthorizationResponder
from operation import Worker

T = TypeVar("T", bound="AttackRequest")

class AttackLoader(Worker[T], ABC, Generic[T]):
    
    def __init__(
            self,
            authorization_responder: Optional[AttackAuthorizationResponder] | None = None,
    ):
        """
        Args:
            authorization_responder: Optional[AttackAuthorizationResponder]
        """
        super().__init__(authorization_responder=authorization_responder or AttackAuthorizationResponder())
        
    @property
    def authorization_responder(self) -> AttackAuthorizationResponder:
        return cast(AttackAuthorizationResponder, super().authorization_responder)
        
    @property
    def execute(self, request: AttackRequest) -> AttackResult:
        method = f"{self.__class__.__name__}.execute"
        decision = self.authorization_responder.execute(
            AttackPermissionRequest(candidate=request)
        )
        if decision.is_denial:
            return AttackResult.failure(
                AttackLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackLoaderException.MSG,
                    err_code=AttackLoaderException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        
        
        