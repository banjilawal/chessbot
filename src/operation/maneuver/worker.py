# src/operation/maneuver/worker.py

"""
Module: operation.maneuver.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverResult
from domain import Maneuver, Path, SquareRegister, SquareState
from exchange import ManeuverPermissionRequest, ManeuverRequest
from operation import Worker
from util import IdFactory, LoggingLevelRouter


class Mover(Worker[ManeuverResult]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces either an Maneuver, Deletion, Update
            or Search Result.

    Attributes:
        permitter: ManeuverAuthorizationResponder

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverResult

    Super Class:
        Worker
    """
    
    def __init__(
            self,
            permitter: Optional[ManeuverAuthorizationResponder] | None = None,
    ):
        """
        Args:
            permitter: Optional[ManeuverAuthorizationResponder]
        """
        super().__init__(
            permitter=permitter or ManeuverAuthorizationResponder()
        )
    
    @property
    def permitter(self) -> ManeuverAuthorizationResponder:
        return cast(ManeuverAuthorizationResponder, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverResult:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.permitter.execute(
            ManeuverPermissionRequest(
                candidate=request,
                id=IdFactory.next_id(class_name="ManeuverPermissionRequest")
            )
        )
        if decision.request_is_denied:
            return ManeuverResult.failure(
                MoverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MoverException.MSG,
                    err_code=MoverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        safe = cast(ManeuverRequest, decision.candidate)
        token = safe.token
        origin = safe.path.origin
        destination = safe.path.destination
        label = safe.path.label
        
        destination.occupant = token
        token.position = destination.coord
        destination.state = SquareState.OCCUPIED
        
        origin.occupant = None
        origin.state = SquareState.EMPTY
        
        maneuver = Maneuver(
            traveler=token,
            path=Path(
                label=label,
                endpoints=SquareRegister(
                    origin=origin,
                    destination=destination,
                )
            )
        )
        return ManeuverResult.success(maneuver)

        