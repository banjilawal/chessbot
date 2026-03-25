# src/logic/token/service/operation/computation/process.py

"""
Module: logic.token.service.operation.computation.process
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations
n
from logic.scalar import Scalar, ScalarService
from logic.system import ComputationResult
from logic.coord import Coord, CoordMultiplicationException, CoordValidationProcess

class CoordScalarProduct:
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Coord microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Coord state by providing single entry and exit points to Coord
        lifecycle.

    Super Class:
        *   IntegrityService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.
    """
    
    @classmethod
    def compute(
            cls,
            coord: Coord,
            scalar: Scalar,
            scalar_service: ScalarService = ScalarService(),
            coord_validator: CoordValidationProcess = CoordValidationProcess(),
    ) -> ComputationResult[[Coord]]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                -   The coord does not pass a validation check.
                -   The scalar does not pass a validation check.
                -   Their product does not satisfy the constraints of the Coord.
            2.  Otherwise, send the success resul.
        Args:
            coord: Coord
            scalar: Scalar
            scalar_service: ScalarService
            coord_validator: CoordValidationProcess
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, the coord does not pass a validation check.
        coord_validation_result = coord_validator.execute(candidate=coord)
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
        scalar_validation_result = scalar_service.validation.execute(candidate=scalar)
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
        # --- Forward the work product to the caller. ---#
        product = Coord(
                row=coord.row * scalar.value,
            column=coord.column * scalar.value
        )
        # Handle the case that, the product does not satisfy integrity requirements
        product_validation_result = coord_validator.execute(product)
        if product_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordMultiplicationException.OP,
                    msg=CoordMultiplicationException.MSG,
                    err_code=CoordMultiplicationException.ERR_CODE,
                    rslt_type=CoordMultiplicationException.RSLT_TYPE,
                    ex=product_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
    
