# src/space/offset/offset.py

"""
Module: space.offset.category.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import List, Optional, cast

from container import VectorSet
from err import TraversalPatternExceptionException
from math import Stepper
from model import LinearTargetSet, Scalar, TargetVectorSet, Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space import MovementPattern
from toolkit import MathToolkit
from util import LoggingLevelRouter



class TraversalPattern(MovementPattern):
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Get the series of targets on a line between the origin and terminus

    Attributes:
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:
        -   def distance() -> ComputationResult[Scalar]
        -   def target_vectors() -> ComputationResult[LinearTargetSet]:

    Super Class:
        Space
    """
    _stepper: Stepper
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            stepper: Stepper,
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            stepper: Stepper
            math_toolkit: Optional[MathToolkit]
        """
        self._stepper = stepper
        self._math_toolkit = math_toolkit
    
    @property
    def stepper(self) -> Stepper:
        return self._stepper
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    
    @LoggingLevelRouter.monitor
    def execute(self, endpoints: VectorRegister) -> ComputationResult[LinearTargetSet]:
        """
        Get DestinationVectors from the origin to the terminus

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper aborts.
            2.  Otherwise, send the computed vector in the success result.
        Args:
        Returns:
            ComputationResult[LinearVectorSet]
        Raises:
             LinearSpaceException
        """
        method = f"{self.__class__.__name__}.next"
        
        # --- Set up looping variables ---#
        cursor = endpoints.u
        solutions: List[Vector] = []
        
        # --- Less than is not a good choice for iterating through vectors.  ---#
        while cursor != endpoints.v:
            # --- Request the next Vector for the stepper. ---#
            computation = self._stepper.next(cursor)
            
            # Handle the case that, the computation is aborted.
            if computation.is_failure:
                # Send an exception chain in the result.
                return ComputationResult.failure(
                    TraversalPatternExceptionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TraversalPatternExceptionException.MSG,
                        err_code=TraversalPatternExceptionException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    ),
                )
            # --- Cast and append the curso to the list. ---#
            cursor = cast(Vector, computation.payload)
            solutions.append(cursor)
        
        # Create the DestinationVector set.
        
        target_set = VectorSet(tuple(solutions))
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(
            LinearTargetSet(
                endpoints=endpoints, group=target_set
            )
        )