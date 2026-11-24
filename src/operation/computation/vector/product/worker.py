# src/operation/computation/vector/product/worker.py

"""
Module: operation.computation.vector.product.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Vector, VectorBlueprint
from err import ScalarProductException
from request import ScalarProductPermissionRequest, ScalarProductRequest, VectorBuildRequest
from transit import ScalarProductPermissionDispatcher, VectorCarrier

from util import IdFactory, LoggingLevelRouter


class ScalarProduct(VectorComputer[ScalarProductRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Compute the contents of a VectorRegister to each other producing either a new Vector or a Coord.

    Attributes:
            permitter: Optional[ScalarProductPermissionDispatcher]
            
    Provides:
        -   def execute(self, request: ScalarProductRequest) -> ComputationResult[Vector]

    Super Class:
        Computation
    """
    
    def __init__(
            self,
            permitter: Optional[ScalarProductPermissionDispatcher] | None = None,
    ):
        """
        Args:
            permitter: Optional[ScalarProductPermissionDispatcher]
        """
        super().__init__(permitter=permitter or ScalarProductPermissionDispatcher())
        
    @property
    def permitter(self) -> ScalarProductPermissionDispatcher:
        return cast(ScalarProductPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ScalarProductRequest) -> ComputationResult[Vector]:
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
            request: ScalarProductRequest
        Result:
            ComputationResult[Vector]
        Raises:
           ScalarProductException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=ScalarProductPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="PermissionRequest")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for productal processing. ---#
        permission_request = cast(ScalarProductPermissionRequest, decision.permission_request)
        transaction_request = cast(ScalarProductRequest, decision.transaction_request)
    
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return ComputationResult.failure(
                exception=ScalarProductException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=ScalarProductRequestNullException()
                )
            )
        # --- Extract the transaction participants. ---#
        scalar = transaction_request.scalar
        vector = transaction_request.vector
        
        # --- Perform transaction and state management work. ---#
        x = scalar.magnitude * vector.x
        y = scalar.magnitude * vector.y
        # Safely build the new vector.
        build = self.vector_builder.execute(
            request=VectorBuildRequest(
                id=IdFactory.next_id(class_name="VectorBuildRequest"),
                item=VectorCarrier(blueprint=VectorBlueprint(x=x, y=y))
            )
        )
        # Handle the case that the build did not produce a result.
        if build.is_failure:
            # Send the exception chain in the denial.
            return ComputationResult.failure(
                exception=ScalarProductException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        vector = cast(Vector, build.content)
        return ComputationResult.success(vector)

        