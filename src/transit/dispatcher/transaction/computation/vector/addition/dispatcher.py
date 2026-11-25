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
from domain import Vector
from operation import VectorAddition
from request import VectorAdditionRequest
from transit import VectorComputationDispatcher
from util import LoggingLevelRouter



class VectorAdditionDispatcher(VectorComputationDispatcher[VectorAdditionRequest]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: VectorAdder
    Provides:
        -   def  execute(self, request: VectorAdditionRequest) -> ComputationResult

    Super Class:
        ComputationDispatcher
    """
    
    def __init__(self, worker: Optional[VectorAddition] | None = None):
        """
        Args:
            worker: Optional[VectorAdder]
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
            VectorAdditionDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                VectorAdditionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionDispatcherException.MSG,
                    err_code=VectorAdditionDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work addition to the caller. ---#
        value = cast(Vector, result.payload)
        return ComputationResult.success(value)
