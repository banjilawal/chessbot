# src/logic/token/service/operation/arithmetic/distance/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.distance.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from math import sqrt

from system import ComputationResult
from logic.coord import Coord, EuclideanDistanceException, CoordService

class EuclideanDistance:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  ComputationWorker the Euclidean distance between two Coords.
        
    Attributes:
        
    Properties:
        -   def compute(
                    u: Coord,
                    v: Coord,
                    coord_service: CoordService,
            ) -> ComputationResult[int]
    
    Super Class:
    """
    
    @classmethod
    def compute(
            cls,
            u: Coord,
            v: Coord,
            coord_service: CoordService = CoordService(),
    ) -> ComputationResult[int]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                -   The coord does not pass a validation check.
                -   The scalar does not pass a validation check.
                -   Their product does not satisfy the constraints of the Coord.
            2.  Otherwise, send the success result.
        Args:
            u: Coord,
            v: Coord,
            coord_service: CoordService
        Returns:
            ComputationResult[int]
        Raises:
            VectorEuclideanException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, the either coord does not pass a validation check.
        for coord in (u, v):
            coord_validation_result =coord_service.validator.validate(coord)
            if coord_validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    EuclideanDistanceException(
                        cls_mthd=method,
                        cls_name=method.__name__,
                        op=EuclideanDistanceException.OP,
                        msg=EuclideanDistanceException.MSG,
                        err_code=EuclideanDistanceException.ERR_CODE,
                        rslt_type=EuclideanDistanceException.RSLT_TYPE,
                        ex=coord_validation_result.exception,
                    )
                )
        # ---Calculate the distance then, forward the work product to the caller. ---#
        distance = sqrt(pow(base=(u.row - v.row), exp=2) + pow(base=(u.column - v.column), exp=2))
        return ComputationResult.success(distance)

    
