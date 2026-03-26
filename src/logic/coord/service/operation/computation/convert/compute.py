# src/logic/token/service/operation/computation/convert/computation.py

"""
Module: logic.token.service.operation.computation.convert.computation
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from logic.system import ComputationResult
from logic.vector import Vector, VectorService
from logic.coord import ConvertVectorException, Coord, CoordService


class VectorToCoordConversion:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Add a Vector to a Coord.
        
    Attributes:
        
    Properties:
        -   compute(
                    vector: Vector,
                    coord_service: CoordService,
                    vector_service: VectorService,
            ) -> ComputationResult[[Coord]]
    
    Super Class:
    """
    
    @classmethod
    def compute(
            cls,
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
            vector: Vector
            coord_service: CoordService
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            ConvertVectorException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, the vector does not pass a validation check.
        vector_validation_result = vector_service.validation.execute(vector)
        if vector_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ConvertVectorException(
                    mthd=method,
                    title=cls.__name__,
                    op=ConvertVectorException.OP,
                    msg=ConvertVectorException.MSG,
                    err_code=ConvertVectorException.ERR_CODE,
                    rslt_type=ConvertVectorException.RSLT_TYPE,
                    ex=vector_validation_result.exception,
                )
            )
        # --- Create the Coord. ---#
        conversion_result = coord_service.build.execute(
            row=vector.y,
            column=vector.x
        )
        # Handle the case that, the product does not satisfy integrity requirements
        if conversion_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ConvertVectorException(
                    mthd=method,
                    title=cls.__name__,
                    op=ConvertVectorException.OP,
                    msg=ConvertVectorException.MSG,
                    err_code=ConvertVectorException.ERR_CODE,
                    rslt_type=ConvertVectorException.RSLT_TYPE,
                    ex=conversion_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        ComputationResult.success(conversion_result.payload)
    
