# src/loader/attack/loader.py

"""
Module: loader.attack.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import AttackResult
from domain import Encounter, KillEncounter, Maneuver
from exchange import (
    AttackAuthorizationResponder, AttackPermissionRequest, AttackRequest, AuthorizationResponder,
    KillRequest
)
from operation import Mover, Worker
from util import IdFactory, LoggingLevelRouter

T = TypeVar("T", bound="AttackRequest")

class Killer(Worker[T], ABC, Generic[T]):
    
    _mover: Mover
    def __init__(
            self,
            mover: Optional[Mover] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
            authorization_responder: Optional[AttackAuthorizationResponder] | None = None,
    ):
        """
        Args:
            authorization_responder: Optional[AttackAuthorizationResponder]
        """
        super().__init__(authorization_responder=authorization_responder or AttackAuthorizationResponder())
        self._priming_validator = priming_validator
        self_mover = mover
        
    @property
    def authorization_responder(self) -> AttackAuthorizationResponder:
        return cast(AttackAuthorizationResponder, super().authorization_responder)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: KillRequest) -> AttackResult:
        method = f"{self.__class__.__name__}.execute"
        
        victim = request.victim
        maneuver_request = request.maneuver_request
        location = request.l
        location.occupant = None
        maneuver_result = self._mover.execute(maneuver_request)
        if maneuver_result.is_failure:
            return AttackResult.failure(
                KillerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillerException.MSG,
                    err_code=KillerException.ERR_CODE,
                    ex=maneuver_result.exception,
                )
            )
        maneuver = cast(Maneuver, maneuver_result.payload)
        victim.captor = maneuver.traveler
        
        encounter = KillEncounter(
            victim=victim,
            attacker_maneuver=maneuver,
            location=location,
            id=IdFactory.next_id(class_name="KillEncounter")
        )
        return AttackResult.success(encounter)