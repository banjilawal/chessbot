# src/logic/token/service/operation/arithmetic/convert/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.convert.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from system import ComputationResult
from model.math.vector import Vector, VectorService
from logic.coord import ConvertVectorException, Coord, CoordService


class ConvertVectorToCoordTransaction:
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
    def execute(
            cls,
            vector: Vector,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Coord]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                    -   The vector does not pass a validation check.
                    -   Build a Coord from the vectors components is unsuccessful.
            2.  Otherwise, send the success result.
        Args:
            vector: Vector
            coord_service: CoordService
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            VectorCoordConversionException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the vector does not pass a validation check.
        vector_validation_result = vector_service.validator.validate(vector)
        if vector_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ConvertVectorException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=ConvertVectorException.OP,
                    msg=ConvertVectorException.MSG,
                    err_code=ConvertVectorException.ERR_CODE,
                    mthd_rslt=ConvertVectorException.MTHD_RSLT,
                    ex=vector_validation_result.exception,
                )
            )
        # --- Create the Coord. ---#
        conversion_result = coord_service.builder.build(
            row=vector.y,
            column=vector.x
        )
        # Handle the case that, the product does not satisfy integrity requirements
        if conversion_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ConvertVectorException(
                    cls_mthd=method,
                    cls_name=method.__name__,
                    op=ConvertVectorException.OP,
                    msg=ConvertVectorException.MSG,
                    err_code=ConvertVectorException.ERR_CODE,
                    mthd_rslt=ConvertVectorException.MTHD_RSLT,
                    ex=conversion_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        ComputationResult.success(conversion_result.payload)
    
