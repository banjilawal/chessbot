# src/space/linear/quadrant/space.py

"""
Module: space.linear.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from container import VectorSet
from err import QuadrantException
from model import Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space import LinearSpace, LinearTargetSet, QuadrantStepper
from util import LoggingLevelRouter


class Quadrant(LinearSpace):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Define a bounded linear function from 2D space.
        2.  Provide the next point in the direction of travel.

    Attributes:
        endpoints: VectorRegister
        stepper: QuadrantStepper

    Provides:

    Super Class:
        LinearSpace
    """    
    def __init__(self, endpoints: VectorRegister, stepper: QuadrantStepper,):
        """
        Args:
            endpoints: QuadrantBounds
            stepper: QuadrantStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        
    @property
    def stepper(self) -> QuadrantStepper:
        return cast(QuadrantStepper, self.stepper)
    
    @LoggingLevelRouter.monitor
    def target_vectors(self) -> ComputationResult[LinearTargetSet]:
        """
        Get DestinationVectors from the origin to the terminus

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper aborts.
            2.  Otherwise, send the computed vector in the success result.
        Args:
        Returns:
            ComputationResult[LinearVectorSet]
        Raises:
             QuadrantException
        """
        method = f"{self.__class__.__name__}.next"
        
        # --- Set up looping variables ---#
        terminus = self.terminus
        cursor = self.origin
        solutions: List[Vector] = []
        
        # --- Less than is not a good choice for iterating through vectors.  ---#
        while cursor != terminus:
            # --- Request the next Vector for the stepper. ---#
            computation = self._stepper.next(cursor)
            
            # Handle the case that, the computation is aborted.
            if computation.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    QuadrantException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=QuadrantException.MSG,
                        err_code=QuadrantException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    ),
                )
            # --- Cast and append the curso to the list. ---#
            cursor = cast(Vector, computation.payload)
            solutions.append(cursor)
        
        # Create the DestinationVector set.
        target_set = VectorSet(tuple(solutions))
        linear_vectors = LinearTargetSet(
            endpoints=self.endpoints,
            targets=target_set
        )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(linear_vectors)
        
    