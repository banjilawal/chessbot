# src/logic/token/service/operation/arithmetic/distance/arithmetic.py

"""
Module: logic.token.service.operation.arithmetic.distance.arithmetic
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from math import sqrt

from logic.system import ComputationResult
from logic.scalar import Scalar, ScalarService
from logic.zone import Zone, EuclideanDistanceException, ZoneService

class EuclideanDistance:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Compute the Euclidean distance between two Zones.
        
    Attributes:
        
    Properties:
        -   def compute(
                    u: Zone,
                    v: Zone,
                    zone_service: ZoneService,
            ) -> ComputationResult[int]
    
    Super Class:
    """
    
    @classmethod
    def compute(
            cls,
            u: Zone,
            v: Zone,
            zone_service: ZoneService = ZoneService(),
    ) -> ComputationResult[int]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                -   The zone does not pass a validation check.
                -   The scalar does not pass a validation check.
                -   Their product does not satisfy the constraints of the Zone.
            2.  Otherwise, send the success result.
        Args:
            u: Zone,
            v: Zone,
            zone_service: ZoneService
        Returns:
            ComputationResult[int]
        Raises:
            EuclideanDistanceException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, the either zone does not pass a validation check.
        for zone in (u, v):
            zone_validation_result =zone_service.validation.execute(zone)
            if zone_validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    EuclideanDistanceException(
                        mthd=method,
                        title=cls.__name__,
                        op=EuclideanDistanceException.OP,
                        msg=EuclideanDistanceException.MSG,
                        err_code=EuclideanDistanceException.ERR_CODE,
                        rslt_type=EuclideanDistanceException.RSLT_TYPE,
                        ex=zone_validation_result.exception,
                    )
                )
        # ---Calculate the distance then, forward the work product to the caller. ---#
        distance = sqrt(pow(base=(u.row - v.row), exp=2) + pow(base=(u.column - v.column), exp=2))
        return ComputationResult.success(distance)

    
