# src/transit/dispatcher/computation/dispatcher.py

"""
Module: transit.dispatcher.computation.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Vector
from operation import VectorAddition
from request import VectorAdditionRequest
from transit import ComputationDispatcher
from util import LoggingLevelRouter



class VectorAdditionDispatcher(ComputationDispatcher[VectorAdditionRequest]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: VectorAddition

    Provides:
        -   def  execute(self, request: Q) -> R

    Super Class:
        ComputationDispatcher
    """
    
    def __init__(self, worker: Optional[VectorAddition] | None = None):
        """
        Args:
            worker: Optional[VectorAddition]
        """
        super().__init__(worker=worker or VectorAddition())
        
    @property
    def worker(self) -> VectorAddition:
        return cast(VectorAddition, super().worker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorAdditionRequest) -> ComputationResult:
        """
        Send VectorAdditionComputationRequest to a worker.

        Action:
            1.  Send an exception chain in the ComputationResult if the worker fails.
            2.  If the computation result is empy send a ComputationResult.empty otherwise, send
                the success result.
        Args:
            request: VectorAdditionComputationRequest
        Result:
            ComputationResult[List[VectorAddition]]
        Raises:
            VectorAdditionComputationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                VectorAdditionComputationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionComputationDispatcherException.MSG,
                    err_code=VectorAdditionComputationDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work addition to the caller. ---#
        value = cast(Vector, result.payload)
        return ComputationResult.success(value)
