# src/space/linear/quadrant/northeast/space.py

"""
Module: space.linear.quadrant.northeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast




class NorthEastQuadrant(Quadrant):
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
        -   def next(current: Vector) -> ComputationResult
        -   def northeast(origin: Vector) -> Quadrant
        -   def northwest(origin: Vector) -> Quadrant
        -   def southeast(origin: Vector) -> Quadrant
        -   def southwest(origin: Vector) -> Quadrant

    Super Class:
        Space

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """
    _endpoints: QuadrantEndpointFactory
    _stepper: QuadrantStepper
    
    def __init__(self, stepper: QuadrantStepper, endpoints: QuadrantEndpointFactory):
        """
        Args:
            endpoints: QuadrantBounds
            stepper: QuadrantStepper
        """
        super().__init__(endpoints=endpoints, stepper=stepper)
        """INTERNAL: Use factory methods instead of direct constructor."""
        
    @property
    def bounds(self) -> QuadrantEndpointFactory:
        return cast(QuadrantEndpointFactory, self.bounds)
    
    @property
    def stepper(self) -> QuadrantStepper:
        return cast(QuadrantStepper, self.stepper)
    
    @property
    def origin(self) -> Vector:
        return self.bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self.bounds.terminus
    
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
             QuadrantException
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
                QuadrantException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantException.MSG,
                    err_code=QuadrantException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=computation.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Scalar, computation.payload))
    
    @LoggingLevelRouter.monitor
    def destination_vectors(self) -> ComputationResult[LinearTargetSet]:
        """
        Get DestinationVectors from the origin to the terminus

        Action:
            1.  Send an exception chain in the ComputationResult if the stepper aborts.
            2.  Otherwise, send the computed vector in the success result.
        Args:
        Returns:
            ComputationResult[LinearVectorSet]
        Raises:
             AxisException
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
                    AxisException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=AxisException.MSG,
                        err_code=AxisException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                        ex=computation.exception,
                    ),
                )
            # --- Cast and append the curso to the list. ---#
            cursor = cast(Vector, computation.payload)
            solutions.append(cursor)
        # Create the DestinationVector set.
        linear_vectors = LinearTargetSet(
            root=self.origin,
            entries=tuple(solutions)
        )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(linear_vectors)

    @classmethod
    def northeast(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            northeast => [u, Vector(num_columns - 1, 0)], (i, 0)
        Functions:
            f(x) = x + 1
            g(x) = -2x + 1
        """
        return cls(
            stepper=QuadrantStepper.northeast(),
            endpoints=QuadrantEndpointFactory.northeast(origin=origin)
        )
    
    @classmethod
    def northwest(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            northwest => [u, Vector(0, 0)], (i, 0)
        Functions:
            f(x) = x - 1
            g(x) = -2x + 1
        """
        return cls(
            stepper=QuadrantStepper.northwest(),
            endpoints=QuadrantEndpointFactory.northwest(origin=origin)
        )
    
    @classmethod
    def southeast(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            southeast => [u, Vector(num_columns - 1, num_rows - 1)], (i, 0)
        Functions:
            f(x) = x + 1
            g(x) = 2x + 1
        """
        return cls(
            stepper=QuadrantStepper.southeast(),
            endpoints=QuadrantEndpointFactory.southeast(origin=origin)
        )
    
    @classmethod
    def southwest(cls, origin: Vector) -> Quadrant:
        """
        Create a 2D space

        Bounds:
            southwest => [u, Vector(0, num_rows - 1)]
        Functions:
            f(x) = x - 1
            g(x) = 2x + 1
        """
        return cls(
            stepper=QuadrantStepper.southwest(),
            endpoints=QuadrantEndpointFactory.southwest(origin=origin)
        )
        
    