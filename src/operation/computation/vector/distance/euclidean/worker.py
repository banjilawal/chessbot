# src/operation/computation/vector/addition/worker.py

"""
Module: operation.computation.vector.addition.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from math import sqrt
from typing import cast

from artifcat import ComputationResult
from domain import Scalar, ScalarBlueprint
from operation import DistanceComputer
from request import DistanceComputationPermissionRequest, EuclideanDistanceRequest, ScalarBuildRequest
from transit import ScalarCarrier
from util import IdFactory, LoggingLevelRouter


class EuclideanDistance(DistanceComputer[EuclideanDistanceRequest]):
    """
    Role:
        - Computation

    Responsibilities:
        1.  Compute the contents of a VectorRegister to each other producing either a new Vector or a Coord.

    Attributes:
            permitter: Optional[DistanceComputationPermissionDispatcher]
            
    Provides:
        -   def execute(self, request: EuclideanDistanceRequest) -> ComputationResult[Vector]

    Super Class:
        DistanceComputer
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: EuclideanDistanceRequest) -> ComputationResult[Scalar]:
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
            request: EuclideanDistanceRequest
        Result:
            ComputationResult[Vector]
        Raises:
           EuclideanDistanceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Get work authorization. ---#
        decision = self.permitter.execute(
            candidate=DistanceComputationPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="PermissionRequest")
            )
        )
        # Handle the case that the request is not authorized.
        if decision.request_is_denied:
            return ComputationResult.failure(
                EuclideanDistanceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EuclideanDistanceException.MSG,
                    err_code=EuclideanDistanceException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        transaction_request = cast(EuclideanDistanceRequest, decision.transaction_request)

        # --- Extract the transaction participants. ---#
        u = transaction_request.u
        v = transaction_request.v
        
        # --- Perform transaction and state management work. ---#
        magnitude = cast(int, sqrt((u.y - v.y) ** 2 + (u.x - v.x) ** 2))
        # Safely build the new vector.
        build = self.scalar_builder.execute(
            request=ScalarBuildRequest(
                id=IdFactory.next_id(class_name="ScalarBuildRequest"),
                item=ScalarCarrier(blueprint=ScalarBlueprint(magnitude=magnitude))
            )
        )
        # Handle the case that the build did not produce a result.
        if build.is_failure:
            # Send the exception chain in the denial.
            return ComputationResult.failure(
                exception=EuclideanDistanceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EuclideanDistanceException.MSG,
                    err_code=EuclideanDistanceException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        scalar = cast(Scalar, build.payload)
        return ComputationResult.success(scalar)

        