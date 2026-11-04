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
from domain import Maneuver, SquareState
from exchange import ManeuverRequest
from operation import Worker
from transit import ManeuverPermissionDispatcher
from util import LoggingLevelRouter


class Mover(Worker[ManeuverResult, ManeuverRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Execute a ManeuverRequest.

    Attributes:
        dispatcher: ManeuverPermissionDispatcher
        
    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverResult

    Super Class:
        Worker
    """
    
    
    def __init__(
            self,
            dispatcher: Optional[ManeuverPermissionDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ManeuverPermissionDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ManeuverPermissionDispatcher()
        )
        
    @property
    def dispatcher(self) -> ManeuverPermissionDispatcher:
        return cast(ManeuverPermissionDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverResult:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.dispatcher.execute(
            ManeuverPermissionRequest(
                authorization_applicant=request,
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
        # --- Extract the requests for additional processing. ---#
        permission_request = decision.permission_request
        transaction_request = decision.transaction_request
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return ManeuverResult.failure(
                exception=MoverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MoverException.MSG,
                    err_code=MoverException.ERR_CODE,
                    ex=ManeuverPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return ManeuverResult.failure(
                exception=MoverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MoverException.MSG,
                    err_code=MoverException.ERR_CODE,
                    ex=ManeuverRequestNullException()
                )
            )
        token = transaction_request.traveler
        path = transaction_request.path
        
        path.destination.occupant = token
        token.position = path.destination.coord
        path.destination.state = SquareState.OCCUPIED
        
        path.origin.occupant = None
        path.origin.state = SquareState.EMPTY
        maneuver = Maneuver(traveler=token, path=path)
        return ManeuverResult.success(maneuver)
        
        
        maneuver = None
        if isinstance(rank, Bishop):
            maneuver = Bishop()
        if isinstance(rank, Knight):
            maneuver = Knight()
        if isinstance(rank, Queen):
            maneuver = Queen()
        if isinstance(rank, Rook):
            maneuver = Rook()
        
        if maneuver is None or isinstance(maneuver, (Pawn, King)):
            return ManeuverResult.failure(
                MoverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=MoverException.MSG,
                    err_code=MoverException.ERR_CODE,
                    ex=ManeuverRouteException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverRouteException.MSG,
                        err_code=NoManeuverRouteException.ERR_CODE,
                    ),
                )
            )
        pawn_token.rank = maneuver
        pawn_token.maneuver_state = ManeuverState.PROMOTED
        return ManeuverResult.success(pawn_token)
        