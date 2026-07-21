# src/space/offset/offset.py

"""
Module: space.offset.category.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, Optional, cast

from container import VectorSet
from err import TraversalPatternExceptionException
from math import Stepper
from model import LinearTargetSet, Scalar, Vector
from register import VectorRegister
from result import ComputationResult, MethodResultType
from space import MovementPattern
from util import LoggingLevelRouter


class LinearSpace:
    """
    Role:
        -   Dataset

    Responsibilities:
        1.  Get the series of targets on a line between the origin and terminus

    Attributes:
        endpoints: VectorRegister
        stepper: Stepper
        math_toolkit: Optional[MathToolkit]

    Provides:
        -   def distance() -> ComputationResult[Scalar]
        -   def target_vectors() -> ComputationResult[LinearTargetSet]:

    Super Class:
        Space
    """
    _endpoints: VectorRegister
    _stepper: Stepper[T]
    _math_toolkit: Optional[MathToolkit]
    
    def __init__(
            self,
            endpoints: VectorRegister,
            stepper: LinearStepper,
            math_toolkit: Optional[MathToolkit] | None = MathToolkit(),
    ):
        """
        Args:
            endpoints: VectorRegister
            stepper: Stepper
            math_toolkit: Optional[MathToolkit]
        """
        self._endpoints = endpoints
        self._stepper = stepper
        self._math_toolkit = math_toolkit
        
    @property
    def endpoints(self) -> VectorRegister:
        return self._endpoints
    
    @property
    def origin(self) -> Vector:
        return self._endpoints.u
    
    @property
    def terminus(self) -> Vector:
        return self._endpoints.v
    
    @property
    def stepper(self) -> LinearStepper:
        return self._stepper
    
    @property
    def math(self) -> MathToolkit:
        return self._math_toolkit
    
    @property
    def is_empty(self) -> bool:
        return self._endpoints.is_empty
    
    @property
    def is_cycle(self) -> bool:
        return self._endpoints.is_cycle
    
    @LoggingLevelRouter.monitor
    def distance(self) -> ComputationResult[Scalar]:
        """
        Get the Euclidean distance between the Space's endpoints.

        Action:
            1.  Send an exception chain in the ComputationResult if the math toolkit
                cannot produce a solution.
            2.  Otherwise, send the computed vector in the success result.
        Args:
        Returns:
            ComputationResult[Scalar]
        Raises:
             LinearSpaceException
        """
        method = f"{self.__class__.__name__}.distance"
        
        # Request the Euclidean distance
        computation = self.math.euclidean_distance.execute(
            register=VectorRegister(u=self.origin, v=self.terminus)
        )
        # Handle the case that, the computation is not satisfied.
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
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Scalar, computation.payload))
    
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
             LinearSpaceException
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
        linear_vectors = LinearTargetSet(
            endpoints=self.endpoints,
            group=target_set
        )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(linear_vectors)