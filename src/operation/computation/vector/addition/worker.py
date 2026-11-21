# src/operation/computation/vector/addition/worker.py

"""
Module: operation.computation.vector.addition.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Vector, VectorBlueprint
from err import VectorAdditionException
from exchange import VectorAdditionPermissionRequest, VectorAdditionRequest, VectorBuildRequest
from fabrication import VectorBuilder
from operation import ComputationWorker
from transit import VectorAdditionPermissionDispatcher, VectorCarrier

from util import IdFactory, LoggingLevelRouter


class VectorAddition(ComputationWorker[VectorAdditionRequest, ComputationResult]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Compute the contents of a VectorRegister to each other producing either a new Vector or a Coord.

    Attributes:
            permitter: Optional[VectorAdditionPermissionDispatcher]
            
    Provides:
        -   def execute(self, request: VectorAdditionRequest) -> ComputationResult[Vector]

    Super Class:
        Computation
    """
    _builder: VectorBuilder
    
    def __init__(
            self,
            builder: Optional[VectorBuilder] | None = None,
            permitter: Optional[VectorAdditionPermissionDispatcher] | None = None,
    ):
        """
        Args:
            builder: Optional[VectorBuilder]
            permitter: Optional[VectorAdditionPermissionDispatcher]
        """
        super().__init__(permitter=permitter or VectorAdditionPermissionDispatcher())
        self._builder = builder or VectorBuilder()
        
    @property
    def permitter(self) -> VectorAdditionPermissionDispatcher:
        return cast(VectorAdditionPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorAdditionRequest) -> ComputationResult[Vector]:
        """
        Add the contents of a VectorRegister to each other.

        Action:
            1.  Send an exception chain in the ComputationResult if any of
                these conditions occur
                    - The operand is null
                    - The operand is flagged unsafe.
                    - Building the other type fails.
            2.  Otherwise, send the success result.
        Args:
            request: VectorAdditionRequest
        Result:
            ComputationResult[Vector]
        Raises:
           VectorAdditionException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=VectorAdditionPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="PermissionRequest")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return ComputationResult.failure(
                VectorAdditionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = decision.permission_request
        transaction_request = decision.transaction_request
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return ComputationResult.failure(
                exception=VectorAdditionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=VectorAdditionPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return ComputationResult.failure(
                exception=VectorAdditionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=VectorAdditionRequestNullException()
                )
            )
        # --- Extract the transaction participants. ---#
        u = transaction_request.u
        v = transaction_request.v
        
        # --- Perform transaction and state management work. ---#
        x = u.x + v.x
        y = u.y + v.y
        # Safely build the new vector.
        build = self._builder.execute(
            request=VectorBuildRequest(
                id=IdFactory.next_id(class_name="VectorBuildRequest"),
                item=VectorCarrier(blueprint=VectorBlueprint(x=x, y=y))
            )
        )
        # Handle the case that the build did not produce a result.
        if build.is_failure:
            # Send the exception chain in the denial.
            return ComputationResult.failure(
                exception=VectorAdditionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        vector = cast(Vector, build.payload)
        return ComputationResult.success(vector)

        