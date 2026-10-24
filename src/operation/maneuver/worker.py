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
from collection import SquareStackService
from domain import Maneuver, Path, SquareRegister, SquareState
from exchange import ManeuverAuthorizationRequest, ManeuverAuthorizationResponder, ManeuverRequest
from operation import Worker
from util import IdFactory, LoggingLevelRouter


class Mover(Worker[ManeuverResult]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces either an Maneuver, Deletion, Update
            or Search Result.

    Attributes:
        authorization_responder: ManeuverAuthorizationResponder

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverResult

    Super Class:
        Worker
    """
    
    def __init__(
            self,
            authorization_responder: Optional[ManeuverAuthorizationResponder] | None = None,
    ):
        """
        Args:
            authorization_responder: Optional[ManeuverAuthorizationResponder]
        """
        super().__init__(
            authorization_responder=authorization_responder or ManeuverAuthorizationResponder()
        )
    
    @property
    def authorization_responder(self) -> ManeuverAuthorizationResponder:
        return cast(ManeuverAuthorizationResponder, super().authorization_responder)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverResult:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.authorization_responder.execute(
            ManeuverAuthorizationRequest(
                candidate=request,
                id=IdFactory.next_id(class_name="ManeuverAuthorizationRequest")
            )
        )
        if decision.is_denial:
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

        