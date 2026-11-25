# src/transit/dispatcher/computation/vector/dispatcher.py

"""
Module: transit.dispatcher.computation.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Scalar
from operation import EuclideanDistance
from request import EuclideanDistanceRequest
from transit import DistanceDispatcher
from util import LoggingLevelRouter


class EuclideanDistanceDispatcher(DistanceDispatcher):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: EuclideanDistance

    Provides:
        -   def execute(request: EuclideanDistanceRequest) -> ComputationResult

    Super Class:
        DistanceDispatcher
    """
    
    def __init__(self, worker: Optional[EuclideanDistance] | None = None):
        """
        Args:
            worker: Optional[Distance]
        """
        super().__init__(worker=worker or EuclideanDistance())
        
    @property
    def worker(self) -> EuclideanDistance:
        return cast(EuclideanDistance, super().worker)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: EuclideanDistanceRequest) -> ComputationResult:
        """
        Send EuclideanDistanceRequest to a worker.

        Action:
            1.  Send an exception chain in the ComputationResult if the worker fails.
            2.  If the computation result is empy send a ComputationResult.empty otherwise,
                send the success result.
        Args:
            request: EuclideanDistanceRequest
        Result:
            ComputationResult[Scalar]
        Raises:
            EuclideanDistanceDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                EuclideanDistanceDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EuclideanDistanceDispatcherException.MSG,
                    err_code=EuclideanDistanceDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work distance to the caller. ---#
        value = cast(Scalar, result.payload)
        return ComputationResult.success(value)
