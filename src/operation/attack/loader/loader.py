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
from exchange import AttackPermissionDispatcher, AttackPermissionRequest, AttackRequest, PermissionDispatcher
from operation import Worker

T = TypeVar("T", bound="AttackRequest")

class AttackLoader(Worker[T], ABC, Generic[T]):
    
    def __init__(
            self,
            dispatcher: Optional[AttackPermissionDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AttackPermissionDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AttackPermissionDispatcher())
        
    @property
    def dispatcher(self) -> AttackPermissionDispatcher:
        return cast(AttackPermissionDispatcher, super().dispatcher)
        
    @property
    def execute(self, request: AttackRequest) -> AttackResult:
        method = f"{self.__class__.__name__}.execute"
        decision = self.dispatcher.execute(
            AttackPermissionRequest(authorization_applicant=request)
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
        
        
        