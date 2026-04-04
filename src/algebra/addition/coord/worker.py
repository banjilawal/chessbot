# src/logic/token/service/operation/arithmetic/addition/validator.py

"""
Module: logic.token.service.operation.arithmetic.addition.transaction
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations

from typing import List, Union

from model.vector import Vector, VectorService
from logic.system import ComputationResult, LoggingLevelRouter
from logic.coord import Coord, CoordAdditionException, CoordAdditionOperandNullException, CoordService

class CoordAdder:
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
            ) -> ComputationResult[Coord]
            
        -   _run_param_checks(
                    cls,
                    coord: Coord,
                    operand: Union[Vector, Coord],
                    coord_service: CoordService = CoordService(),
                    vector_service: VectorService = VectorService(),
            ) -> ComputationResult[Coord]
            
        -   _run_coord_param_checks(
                    cls,
                    coords: List[Coord],
                    coord_service: CoordService,
            ) -> ComputationResult[Coord]
            
        -   _route_addition(
                    cls,
                    coord: Coord,
                    operand: Union[Vector, Coord],
                    coord_service: CoordService,
            ) -> ComputationResult[Coord]
    
    Super Class:
    """
    
    @classmethod
    def execute(
            cls,
            coord: Coord,
            operand: Union[Vector, Coord],
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
            operand: Union[Vector, Coord]
            coord_service: CoordService
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordAdditionException
        """
        method = f"{cls.__name__}.compute"
        
        # Handle the case that, an operand does not pass a validation check.
        validation_result = cls._run_param_checks(
            coord=coord,
            operand=operand,
            coord_service=coord_service,
            vector_service=vector_service,
        )
        if validation_result.is_failure:
            return validation_result
        # --- Compute the sum. ---#
        addition_result =  cls._route_addition(
            coord=coord,
            operand=operand,
            coord_service=coord_service,
        )
        # Handle the case that the sum is not computed.
        if addition_result.is_failure:
            # Return the exception chain on failure.
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
        return addition_result
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_param_checks(
            cls,
            coord: Coord,
            operand: Union[Vector, Coord],
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
    ) -> ComputationResult[Coord]:
        """
        Verify the summation parameters are safe.
        
        Action:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The coord.
                    -   The operand.
                fail their validation check.
            2.  Otherwise, send the success result.
        Args:
            coord: Coord
            operand: Union[Vector, Coord]
            coord_service: CoordService
            vector_service: VectorService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordAdditionException
            CoordAdditionOperandNullException
        """
        method = f"{cls.__name__}._run_param_checks"
        
        # Handle the case that, the operand does not exist.
        if operand is None:
            # Return exception chain on failure.
            return ComputationResult.failure(
                CoordAdditionException(
                    mthd=method,
                    title=cls.__name__,
                    op=CoordAdditionException.OP,
                    msg=CoordAdditionException.MSG,
                    err_code=CoordAdditionException.ERR_CODE,
                    rslt_type=CoordAdditionException.RSLT_TYPE,
                    ex=CoordAdditionOperandNullException(
                        msg=CoordAdditionOperandNullException.MSG,
                        err_code=CoordAdditionOperandNullException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the operand is a vector that fails a validation check.
        if isinstance(operand, Vector):
            vector_validation_result = vector_service.validator.validate(candidate=operand)
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
            # Run the coord param_check results
            return cls._run_coord_param_checks(coords=[coord], coord_service=coord_service)
        # Handle the case that, the coord and operand are the same type.
        return cls._run_coord_param_checks(coords=[coord, operand], coord_service=coord_service)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_coord_param_checks(
            cls,
            coords: List[Coord],
            coord_service: CoordService,
    ) -> ComputationResult[Coord]:
        """
        Verify the summation's coord parameters are safe.

        Action:
            1.  Send an exception chain in the ComputationResult if any Coord
                param fails a safety check.
            2.  Otherwise, send the success result.
        Args:
            coords: List[Coord]
            coord_service: CoordService
        Returns:
            ComputationResult[Coord]
        Raises:
            CoordAdditionException
        """
        method = f"{cls.__name__}._run_coord_param_checks"
        
        # Handle the case that, a coord_param fails a validation check.
        for coord in coords:
            coord_validation_result = coord_service.validator.validate(coord)
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
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(coords[0])
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _route_addition(
            cls,
            coord: Coord,
            operand: Union[Vector, Coord],
            coord_service: CoordService,
    ) -> ComputationResult[Coord]:
        """
         Add the operand to the coord.
         
         Actions:
            1.  Build a new coord by from the component sums.
            2.  If Coord build fails send an exception chain in the ComputationResult.
                Otherwise, send the success result.
                Send an exception chain in the ComputationResult if
         Args:
            coord: Coord
            operand: Union[Vector, Coord]
            coord_service: CoordService
         Returns:
             ComputationResult[Coord]
         Raises:
         """
        method = f"{cls.__name__}._route_addition"
        
        # Build a new coord from a coord and vector.
        if isinstance(operand, Vector):
            return coord_service.builder.build(
                row=coord.row + operand.y,
                column=coord.column * operand.x
            )
        # Build a new coord from two coords.
        return coord_service.builder.build(
            row=coord.row + operand.row,
            column=coord.column + operand.column
        )
