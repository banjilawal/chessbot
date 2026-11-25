# src/transit/dispatcher/computation/vector/dispatcher.py

"""
Module: transit.dispatcher.computation.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import ComputationResult
from domain import Scalar
from operation import DistanceComputer
from request import DistanceRequest
from transit import VectorComputationDispatcher
from util import LoggingLevelRouter



class DistanceDispatcher(VectorComputationDispatcher[DistanceRequest]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: Distance

    Provides:
        -   def  execute(request: DistanceRequest) -> ComputationResult

    Super Class:
        VectorComputationDispatcher
    """
    
    def __init__(self, worker: DistanceComputer):
        """
        Args:
            worker: Optional[Distance]
        """
        super().__init__(worker=worker)
        
    @property
    def worker(self) -> DistanceComputer:
        return cast(DistanceComputer, super().worker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: DistanceRequest) -> ComputationResult:
        """
        Send DistanceComputationRequest to a worker.

        Action:
            1.  Send an exception chain in the ComputationResult if the worker fails.
            2.  If the computation result is empy send a ComputationResult.empty otherwise,
                send the success result.
        Args:
            request: DistanceComputationRequest
        Result:
            ComputationResult[Scalar]
        Raises:
            DistanceDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                DistanceDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DistanceDispatcherException.MSG,
                    err_code=DistanceDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work distance to the caller. ---#
        value = cast(Scalar, result.payload)
        return ComputationResult.success(value)
