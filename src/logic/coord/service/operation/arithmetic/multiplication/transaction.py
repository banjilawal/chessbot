# src/logic/token/service/operation/arithmetic/multiplication/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.multiplication.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from logic.system import ComputationResult
from build.scalar import Scalar, ScalarService
from logic.coord import Coord, CoordMultiplicationException, CoordService

class MultiplyCoordTransaction:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Compute the product of a Coord and a Scalar.
        
    Attributes:
        
    Properties:
        -   compute(
                    coord: Coord,
                    scalar: Scalar,
                    coord_service: CoordService,
                    scalar_service: ScalarService,
            ) -> ComputationResult[[Coord]]
    
    Super Class:
    """
    
    @classmethod
    def execute(
            cls,
            coord: Coord,
            scalar: Scalar,
            coord_service: CoordService = CoordService(),
            scalar_service: ScalarService = ScalarService(),
    ) -> ComputationResult[Coord]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                -   The coord does not pass a validation check.
                -   The scalar does not pass a validation check.
                -   Their product does not satisfy the constraints of the Coord.
            2.  Otherwise, send the success result.
        Args:
            coord: Coord
            scalar: Scalar
            coord_service: CoordService
            scalar_service: ScalarService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordMultiplicationException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result =coord_service.validator.validate(coord)
        if coord_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordMultiplicationException.OP,
                    msg=CoordMultiplicationException.MSG,
                    err_code=CoordMultiplicationException.ERR_CODE,
                    rslt_type=CoordMultiplicationException.RSLT_TYPE,
                    ex=coord_validation_result.exception,
                )
            )
        # Handle the case that, the scalar does not pass a validation check.
        scalar_validation_result = scalar_service.validator.validate(candidate=scalar)
        if scalar_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordMultiplicationException.OP,
                    msg=CoordMultiplicationException.MSG,
                    err_code=CoordMultiplicationException.ERR_CODE,
                    rslt_type=CoordMultiplicationException.RSLT_TYPE,
                    ex=scalar_validation_result.exception,
                )
            )
        # --- Create the product. ---#
        product_build_result = coord_service.builder.build(
            row=coord.row * scalar.value,
            column=coord.column * scalar.value
        )
        # Handle the case that, the product does not satisfy integrity requirements
        if product_build_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordMultiplicationException.OP,
                    msg=CoordMultiplicationException.MSG,
                    err_code=CoordMultiplicationException.ERR_CODE,
                    rslt_type=CoordMultiplicationException.RSLT_TYPE,
                    ex=product_build_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        ComputationResult.success(product_build_result.payload)
    
