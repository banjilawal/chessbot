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
            permitter: Optional[AttackAuthorizationResponder] | None = None,
    ):
        """
        Args:
            permitter: Optional[AttackAuthorizationResponder]
        """
        super().__init__(permitter=permitter or AttackAuthorizationResponder())
        
    @property
    def permitter(self) -> AttackAuthorizationResponder:
        return cast(AttackAuthorizationResponder, super().permitter)
        
    @property
    def execute(self, request: AttackRequest) -> AttackResult:
        method = f"{self.__class__.__name__}.execute"
        decision = self.permitter.execute(
            AttackPermissionRequest(candidate=request)
        )
        if decision.request_is_denied:
            return AttackResult.failure(
                AttackLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackLoaderException.MSG,
                    err_code=AttackLoaderException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        
        
        