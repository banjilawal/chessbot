# src/transit/dispatcher/maneuver/dispatcher.py

"""
Module: transit.dispatcher.maneuver.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverResult
from domain import Maneuver
from err import ManeuverDispatcherException
from exchange import ManeuverRequest
from operation import Mover
from transit import TransactionDispatcher
from util import LoggingLevelRouter

class ManeuverDispatcher(TransactionDispatcher[ManeuverRequest, ManeuverResult]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute ManeuverRequests among workers then send the result to the correct client

    Attributes:
        worker: Mover

    Provides:
        -   def  execute(self, request: ManeuverRequest) -> ManeuverResult

    Super Class:
        TransactionDispatcher
    """
    
    
    def __init__(self, worker: Optional[Mover] | None = None):
        """
        Args:
            worker: Optional[Mover]
        """
        super().__init__(worker=worker or Mover())
        
    @property
    def worker(self) -> Mover:
        return cast(Mover, super().worker)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverResult:
        """
        Distribute ManeuverRequests among workers then forward the results.
        
        Action:
            1.  Send an exception chain in the Result if the request cannot be satisfied.
            2.  Otherwise, send the success result.
        Args:
            request: ManeuverRequest
        Returns:
            ManeuverResult
        Raises:
            ManeuverDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return ManeuverResult.failure(
                ManeuverDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverDispatcherException.MSG,
                    err_code=ManeuverDispatcherException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        maneuver = cast(Maneuver, result.payload)
        return ManeuverResult.success(maneuver)
        