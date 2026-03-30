# src/logic/token/service/operation/arithmetic/multiplication/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.multiplication.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from logic.system import ComputationResult
from logic.scalar import Scalar, ScalarService
from logic.zone import Zone, ZoneMultiplicationException, ZoneService

class MultiplyZoneTransaction:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Compute the product of a Zone and a Scalar.
        
    Attributes:
        
    Properties:
        -   compute(
                    zone: Zone,
                    scalar: Scalar,
                    zone_service: ZoneService,
                    scalar_service: ScalarService,
            ) -> ComputationResult[[Zone]]
    
    Super Class:
    """
    
    @classmethod
    def execute(
            cls,
            zone: Zone,
            scalar: Scalar,
            zone_service: ZoneService = ZoneService(),
            scalar_service: ScalarService = ScalarService(),
    ) -> ComputationResult[Zone]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                -   The zone does not pass a validation check.
                -   The scalar does not pass a validation check.
                -   Their product does not satisfy the constraints of the Zone.
            2.  Otherwise, send the success result.
        Args:
            zone: Zone
            scalar: Scalar
            zone_service: ZoneService
            scalar_service: ScalarService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneMultiplicationException
        """
        method = f"{cls.__name__}.execute"
        
        # Handle the case that, the zone does not pass a validation check.
        zone_validation_result =zone_service.validation.execute(zone)
        if zone_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ZoneMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneMultiplicationException.OP,
                    msg=ZoneMultiplicationException.MSG,
                    err_code=ZoneMultiplicationException.ERR_CODE,
                    rslt_type=ZoneMultiplicationException.RSLT_TYPE,
                    ex=zone_validation_result.exception,
                )
            )
        # Handle the case that, the scalar does not pass a validation check.
        scalar_validation_result = scalar_service.validation.execute(candidate=scalar)
        if scalar_validation_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ZoneMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneMultiplicationException.OP,
                    msg=ZoneMultiplicationException.MSG,
                    err_code=ZoneMultiplicationException.ERR_CODE,
                    rslt_type=ZoneMultiplicationException.RSLT_TYPE,
                    ex=scalar_validation_result.exception,
                )
            )
        # --- Create the product. ---#
        product_build_result = zone_service.build.execute(
            row=zone.row * scalar.value,
            column=zone.column * scalar.value
        )
        # Handle the case that, the product does not satisfy integrity requirements
        if product_build_result.is_failure:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ZoneMultiplicationException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneMultiplicationException.OP,
                    msg=ZoneMultiplicationException.MSG,
                    err_code=ZoneMultiplicationException.ERR_CODE,
                    rslt_type=ZoneMultiplicationException.RSLT_TYPE,
                    ex=product_build_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        ComputationResult.success(product_build_result.payload)
    
