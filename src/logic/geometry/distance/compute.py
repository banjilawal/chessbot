# src/logic/token/service/operation/arithmetic/distance/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.distance.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from math import sqrt
from typing import Union

from logic.system import ComputationResult, LoggingLevelRouter, NumberValidator
from logic.scalar import Scalar, ScalarService
from logic.coord import Coord, EuclideanDistanceException, CoordValidator
from logic.system.worker import Worker
from logic.vector import Vector, VectorValidator


class EuclideanDistanceFinder(Worker):
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Compute the Euclidean distance between two either two coords or vectors..
        
    Attributes:
        
    Properties:
        -   def compute(
                    u: Coord,
                    v: Coord,
                    coord_validator: CoordValidator,
            ) -> ComputationResult[int]
    
    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            u: Union[Coord|Vector],
            v: Union[Coord|Vector],
            coord_validator: CoordValidator = CoordValidator(),
            vector_validator: VectorValidator = VectorValidator(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ComputationResult[int]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                -   The coord does not pass a validation check.
                -   The scalar does not pass a validation check.
                -   Their product does not satisfy the constraints of the Coord.
            2.  Otherwise, send the success result.
        Args:
            u: Union[Coord|Vector]
            v: Union[Coord|Vector]
            coord_validator: CoordValidator
            vector_validator: VectorValidator
            number_validator: NumberValidator
        Returns:
            ComputationResult[int]
        Raises:
            EuclideanDistanceException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, the either coord does not pass a validation check.
        for coord in (u, v):
            coord_validation_result =coord_validator.validator.validate(coord)
            if coord_validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    EuclideanDistanceException(
                        mthd=method,
                        title=cls.__name__,
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
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _distance_helper(
            cls,
            u: Union[Coord | Vector],
            v: Union[Coord | Vector],
            coord_validator: CoordValidator,
            vector_validator: VectorValidator,
            number_validator: NumberValidator,
    ) -> ComputationResult[int]:
        method = f"{cls.__name__}._distance_helper"
        
        # Handle the case that either operand is null.
        for entity in [u, v]:
            if entity is None:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    EuclideanDistanceException(
                        mthd=method,
                        title=cls.__name__,
                        op=EuclideanDistanceException.OP,
                        msg=EuclideanDistanceException.MSG,
                        err_code=EuclideanDistanceException.ERR_CODE,
                        rslt_type=EuclideanDistanceException.RSLT_TYPE,
                        ex=EuclideanDistanceOperandNullException(
                            msg=EuclideanDistanceException.MSG,
                            err_code=EuclideanDistanceException.ERR_CODE,
                        )
                    )
                )
        # Handle the case that their classes are different.
        if not isinstance(type(u), type(v)):
            # Return exception chain on failure.
            return ComputationResult.failure(
                EuclideanDistanceException(
                    mthd=method,
                    title=cls.__name__,
                    op=EuclideanDistanceException.OP,
                    msg=EuclideanDistanceException.MSG,
                    err_code=EuclideanDistanceException.ERR_CODE,
                    rslt_type=EuclideanDistanceException.RSLT_TYPE,
                    ex=EuclideanDistanceOperandNullException(
                        msg=EuclideanDistanceException.MSG,
                        err_code=EuclideanDistanceException.ERR_CODE,
                    )
                )
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_vector_distance(
            cls,
            u: Vector,
            v: Vector,
            vector_validator: VectorValidator,
            number_validator: NumberValidator,
    ) -> ComputationResult[int]:
        method = f"{cls.__name__}._compute_vector_distance"
        
        # Handle the case that either vector is unsafe.
        for vector in [u, v]:
            validation_result = vector_validator.validate(
                candidate=vector,
                number_validator=number_validator,
            )
            if validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    EuclideanDistanceException(
                        mthd=method,
                        title=cls.__name__,
                        op=EuclideanDistanceException.OP,
                        msg=EuclideanDistanceException.MSG,
                        err_code=EuclideanDistanceException.ERR_CODE,
                        rslt_type=EuclideanDistanceException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # ---Forward the work product. ---#
        return cls._compute_distance(u=u, v=v)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_coord_distance(
            cls,
            a: Coord,
            b: Coord,
            coord_validator: CoordValidator,
            number_validator: NumberValidator,
    ) -> ComputationResult[int]:
        method = f"{cls.__name__}._compute_coord_distance"
        
        # Handle the case that either coord is unsafe.
        for coord in [a, b]:
            validation_result = coord_validator.validate(
                candidate=coord,
                number_validator=number_validator,
            )
            if validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    EuclideanDistanceException(
                        mthd=method,
                        title=cls.__name__,
                        op=EuclideanDistanceException.OP,
                        msg=EuclideanDistanceException.MSG,
                        err_code=EuclideanDistanceException.ERR_CODE,
                        rslt_type=EuclideanDistanceException.RSLT_TYPE,
                        ex=validation_result.exception
                    )
                )
        # ---Forward the work product. ---#
        return cls._compute_distance(
            u=Vector(x=a.column, y=a.row),
            v=Vector(x=b.column, y=b.row)
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _compute_distance(
            cls,
            u: Vector,
            v: Vector,
    ) -> ComputationResult[int]:
        method = f"{cls.__name__}._compute_distance"
        distance = sqrt(pow(base=(u.y - v.y), exp=2) + pow(base=(u.x - v.x), exp=2))
        return ComputationResult.success(distance)
