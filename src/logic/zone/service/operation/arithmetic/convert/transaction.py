# src/logic/token/service/operation/arithmetic/convert/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.convert.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from logic.system import ComputationResult
from logic.vector import Vector, VectorService
from logic.zone import ConvertVectorException, Zone, ZoneService


class ConvertVectorToZoneTransaction:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Add a Vector to a Zone.
        
    Attributes:
        
    Properties:
        -   compute(
                    vector: Vector,
                    zone_service: ZoneService,
                    vector_service: VectorService,
            ) -> ComputationResult[[Zone]]
    
    Super Class:
    """
    
    @classmethod
    def execute(
            cls,
            vector: Vector,
            zone_service: ZoneService = ZoneService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Zone]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                    -   The vector does not pass a validation check.
                    -   Build a Zone from the vectors components is unsuccessful.
            2.  Otherwise, send the success result.
        Args:
            vector: Vector
            zone_service: ZoneService
            vector_service: VectorService
        Returns:
            ComputationResult[Zone]
        Raises:
            ConvertVectorException
        """
        method = f"{cls.__name__}.execute"
        
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
        # --- Create the Zone. ---#
        conversion_result = zone_service.build.execute(
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
    
