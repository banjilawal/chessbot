# src/logic/token/service/operation/computation/addition/computation.py

"""
Module: logic.token.service.operation.computation.addition.computation
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from logic.system import ComputationResult
from logic.vector import Vector, VectorService
from logic.coord import Coord, CoordAdditionException, CoordService

class CoordVectorAddition:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Add a Vector to a Coord.
        
    Attributes:
        
    Properties:
        -   compute(
                    coord: Coord,
                    vector: Vector,
                    coord_service: CoordService,
                    vector_service: VectorService,
            ) -> ComputationResult[[Coord]]
    
    Super Class:
    """
    
    @classmethod
    def compute(
            cls,
            coord: Coord,
            vector: Vector,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Coord]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                    -   The coord does not pass a validation check.
                    -   The vector does not pass a validation check.
                    -   Their sum does not satisfy the constraints of the Coord.
            2.  Otherwise, send the success result.
        Args:
            coord: Coord
            vector: Vector
            coord_service: CoordService
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordAdditionException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result =coord_service.validation.execute(coord)
        if coord_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordAdditionException.OP,
                    msg=CoordAdditionException.MSG,
                    err_code=CoordAdditionException.ERR_CODE,
                    rslt_type=CoordAdditionException.RSLT_TYPE,
                    ex=coord_validation_result.exception,
                )
            )
        # Handle the case that, the vector does not pass a validation check.
        vector_validation_result = vector_service.validation.execute(candidate=vector)
        if vector_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordAdditionException.OP,
                    msg=CoordAdditionException.MSG,
                    err_code=CoordAdditionException.ERR_CODE,
                    rslt_type=CoordAdditionException.RSLT_TYPE,
                    ex=vector_validation_result.exception,
                )
            )
        # --- Create the product. ---#
        addition_result = coord_service.build.execute(
            row=coord.row + vector.y,
            column=coord.column * vector.x
        )
        # Handle the case that, the product does not satisfy integrity requirements
        if addition_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordAdditionException.OP,
                    msg=CoordAdditionException.MSG,
                    err_code=CoordAdditionException.ERR_CODE,
                    rslt_type=CoordAdditionException.RSLT_TYPE,
                    ex=addition_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        ComputationResult.success(addition_result.payload)
    
