# src/logic/token/service/operation/arithmetic/addition/transaction.py

"""
Module: logic.token.service.operation.arithmetic.addition.transaction
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from typing import List, Union

from logic.vector import Vector, VectorService
from logic.system import ComputationResult, LoggingLevelRouter
from logic.zone import Zone, ZoneAdditionException, ZoneAdditionOperandNullException, ZoneService

class ZoneAdditionTransaction:
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Add a Vector to a Zone.
        
    Attributes:
        
    Properties:
        -   compute(
                    zone: Zone,
                    vector: Vector,
                    zone_service: ZoneService,
                    vector_service: VectorService,
            ) -> ComputationResult[Zone]
            
        -   _run_param_checks(
                    cls,
                    zone: Zone,
                    operand: Union[Vector, Zone],
                    zone_service: ZoneService = ZoneService(),
                    vector_service: VectorService = VectorService(),
            ) -> ComputationResult[Zone]
            
        -   _run_zone_param_checks(
                    cls,
                    zones: List[Zone],
                    zone_service: ZoneService,
            ) -> ComputationResult[Zone]
            
        -   _route_addition(
                    cls,
                    zone: Zone,
                    operand: Union[Vector, Zone],
                    zone_service: ZoneService,
            ) -> ComputationResult[Zone]
    
    Super Class:
    """
    
    @classmethod
    def execute(
            cls,
            zone: Zone,
            operand: Union[Vector, Zone],
            zone_service: ZoneService = ZoneService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Zone]:
        """
        Action:
            1.  Send an exception chain in the ComputationResult if:
                    -   The zone does not pass a validation check.
                    -   The vector does not pass a validation check.
                    -   Their sum does not satisfy the constraints of the Zone.
            2.  Otherwise, send the success result.
        Args:
            zone: Zone
            operand: Union[Vector, Zone]
            zone_service: ZoneService
            vector_service: VectorService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneAdditionException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, an operand does not pass a validation check.
        validation_result = cls._run_param_checks(
            zone=zone,
            operand=operand,
            zone_service=zone_service,
            vector_service=vector_service,
        )
        if validation_result.is_failure:
            return validation_result
        # --- Compute the sum. ---#
        addition_result =  cls._route_addition(
            zone=zone,
            operand=operand,
            zone_service=zone_service,
        )
        # Handle the case that the sum is not computed.
        if addition_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                ZoneAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneAdditionException.OP,
                    msg=ZoneAdditionException.MSG,
                    err_code=ZoneAdditionException.ERR_CODE,
                    rslt_type=ZoneAdditionException.RSLT_TYPE,
                    ex=addition_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return addition_result
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_param_checks(
            cls,
            zone: Zone,
            operand: Union[Vector, Zone],
            zone_service: ZoneService = ZoneService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Zone]:
        """
        Verify the summation parameters are safe.
        
        Action:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The zone.
                    -   The operand.
                fail their validation check.
            2.  Otherwise, send the success result.
        Args:
            zone: Zone
            operand: Union[Vector, Zone]
            zone_service: ZoneService
            vector_service: VectorService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneAdditionException
            ZoneAdditionOperandNullException
        """
        method = f"{cls.__name__}._run_param_checks"
        
        # Handle the case that, the operand does not exist.
        if operand is None:
            # Return exception chain on failure.
            return ComputationResult.failure(
                ZoneAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=ZoneAdditionException.OP,
                    msg=ZoneAdditionException.MSG,
                    err_code=ZoneAdditionException.ERR_CODE,
                    rslt_type=ZoneAdditionException.RSLT_TYPE,
                    ex=ZoneAdditionOperandNullException(
                        msg=ZoneAdditionOperandNullException.MSG,
                        err_code=ZoneAdditionOperandNullException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the operand is a vector that fails a validation check.
        if isinstance(operand, Vector):
            vector_validation_result = vector_service.validation.execute(candidate=operand)
            if vector_validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    ZoneAdditionException(
                        mthd=method,
                        title=cls.__name__,
                        op=ZoneAdditionException.OP,
                        msg=ZoneAdditionException.MSG,
                        err_code=ZoneAdditionException.ERR_CODE,
                        rslt_type=ZoneAdditionException.RSLT_TYPE,
                        ex=vector_validation_result.exception,
                    )
                )
            # Run the zone param_check results
            return cls._run_zone_param_checks(zones=[zone], zone_service=zone_service)
        # Handle the case that, the zone and operand are the same type.
        return cls._run_zone_param_checks(zones=[zone, operand], zone_service=zone_service)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_zone_param_checks(
            cls,
            zones: List[Zone],
            zone_service: ZoneService,
    ) -> ComputationResult[Zone]:
        """
        Verify the summation's zone parameters are safe.

        Action:
            1.  Send an exception chain in the ComputationResult if any Zone
                param fails a safety check.
            2.  Otherwise, send the success result.
        Args:
            zones: List[Zone]
            zone_service: ZoneService
        Returns:
            ComputationResult[Zone]
        Raises:
            ZoneAdditionException
        """
        method = f"{cls.__name__}._run_zone_param_checks"
        
        # Handle the case that, a zone_param fails a validation check.
        for zone in zones:
            zone_validation_result = zone_service.validation.execute(zone)
            if zone_validation_result.is_failure:
                # Return exception chain on failure.
                return ComputationResult.failure(
                    ZoneAdditionException(
                        mthd=method,
                        title=cls.__name__,
                        op=ZoneAdditionException.OP,
                        msg=ZoneAdditionException.MSG,
                        err_code=ZoneAdditionException.ERR_CODE,
                        rslt_type=ZoneAdditionException.RSLT_TYPE,
                        ex=zone_validation_result.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(zones[0])
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _route_addition(
            cls,
            zone: Zone,
            operand: Union[Vector, Zone],
            zone_service: ZoneService,
    ) -> ComputationResult[Zone]:
        """
         Add the operand to the zone.
         
         Actions:
            1.  Build a new zone by from the component sums.
            2.  If Zone build fails send an exception chain in the ComputationResult.
                Otherwise, send the success result.
                Send an exception chain in the ComputationResult if
         Args:
            zone: Zone
            operand: Union[Vector, Zone]
            zone_service: ZoneService
         Returns:
             ComputationResult[Zone]
         Raises:
         """
        method = f"{cls.__name__}._route_addition"
        
        # Build a new zone from a zone and vector.
        if isinstance(operand, Vector):
            return zone_service.build.execute(
                row=zone.row + operand.y,
                column=zone.column * operand.x
            )
        # Build a new zone from two zones.
        return zone_service.build.execute(
            row=zone.row + operand.row,
            column=zone.column + operand.column
        )
