# src/logic/vector/validator.py

"""
Module: logic.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Union

from logic.coord import Coord, CoordService
from logic.system.worker import Worker
from logic.vector import Vector, VectorService
from logic.system import (
    ComputationResult, LoggingLevelRouter, NumberValidator
)
from logic.vector.service.operation.arithmetic import (
    VectorCoordConversionException,
    VectorCoordConversionOperandNullException
)


class VectorCoordConverter(Worker):
    """
    Role:
        -   Worker
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
    
    -   def work(
                operand: Union[Vector,Coord],
                coord_service: CoordService,
                vector_service: VectorService,
                number_validator: NumberValidator,
        ) -> ComputationResult[Union[Vector, Coord]]:
    
    -   def _conversion_helper(
                operand: Union[Vector,Coord],
                coord_service: CoordService,
                vector_service: VectorService,
                number_validator: NumberValidator,
        ) -> ComputationResult[Union[Vector, Coord]]:
    
    -   def _vector_to_coord(
                vector: Vector,
                coord_service: CoordService,
                vector_service: VectorService,
                number_validator: NumberValidator,
        ) -> ComputationResult[Coord]:
 
    -   def _coord_to_vector(
            coord: Coord,
            coord_service: CoordService,
            vector_service: VectorService,
            number_validator: NumberValidator,
        ) -> ComputationResult[Vector]:

    Super Class:
        Worker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            operand: Union[Vector,Coord],
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
            number_validator: NumberValidator = NumberValidator(),
    ) -> ComputationResult[Union[Vector, Coord]]:
        """
        Convert a vector to a coord and vice versa.
        
        Action:
            1.  Send an exception chain in the ComputationResult if any of
                these conditions occur
                    -   The operand is null
                    -   The operand is flagged unsafe.
                    -   Building the other type fails.
            2.  Otherwise, send the success result.
        Args:
            operand: Union[Vector,Coord]
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.work"
        
        conversion_result = cls._conversion_helper(
            operand=operand,
            coord_service=coord_service,
            vector_service=vector_service,
            number_validator=number_validator,
        )
        # Handle the case that, the conversion was unsuccessful
        if conversion_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=conversion_result.exception,
                )
            )
        # --- Forward the work product. ---#
        return conversion_result
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _conversion_helper(
            cls,
            operand: Union[Vector, Coord],
            coord_service: CoordService,
            vector_service: VectorService,
            number_validator: NumberValidator,
    ) -> ComputationResult[Union[Vector, Coord]]:
        """
        Directs work to the appropriate converter.

        Action:
            1.  Send an exception chain in the ComputationResult if either
                    -   The operand is null
                    -   Either converter flags an error
            2.  Otherwise, send the success result.
        Args:
            operand: Union[Vector,Coord]
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
           VectorCoordConversionOperandNullException
        """
        method = f"{cls.__name__}._conversion_helper"
        
        # Handle the case that, the operand does not exist.
        if operand is None:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=VectorCoordConversionOperandNullException(
                        msg=VectorCoordConversionOperandNullException.MSG,
                        err_code=VectorCoordConversionOperandNullException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate converter for final processing. ---#
        
        # The vector-to-coord case.
        if isinstance(operand, Vector):
            return cls._vector_to_coord(
                vector=operand,
                coord_service=coord_service,
                vector_service=vector_service,
                number_validator=number_validator,
            )
        # The coord-to-vectror case.
        return cls._coord_to_vector(
            coord=operand,
            coord_service=coord_service,
            vector_service=vector_service,
            number_validator=number_validator,
        )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _vector_to_coord(
            cls,
            vector: Vector,
            coord_service: CoordService,
            vector_service: VectorService,
            number_validator: NumberValidator,
    ) -> ComputationResult[Coord]:
        """
        Converts a vector to a coord.

        Action:
            1.  Send an exception chain in the ComputationResult if either
                    -   vector is flagged unsafe.
                    -   The coord_builder throws an error
            2.  Otherwise, wrap the payload in a ComputationResult.
            3.  Send the success result.
        Args:
            vector: Vector
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        Result:
            ComputationResult[Coord]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}._vector_to__coord"
        
        # Handle the case that, vector is unsafe.
        vector_validation_result = vector_service.validate(vector)
        if vector_validation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=vector_validation_result.exception,
                )
            )
        # --- Do the conversion work. ---#
        conversion_result = coord_service.builder.build(
            row=vector.x,
            col=vector.y,
            number_validator=number_validator,
        )
        
        # Handle the case that, the conversion was unsuccessful.
        if conversion_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=conversion_result.exception,
                )
            )
        # --- Forward the work product. ---#
        return ComputationResult.success(conversion_result.payload)
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _coord_to_vector(
            cls,
            coord: Coord,
            coord_service: CoordService,
            vector_service: VectorService,
            number_validator: NumberValidator,
    ) -> ComputationResult[Vector]:
        """
        Converts a coord to a vector.

        Action:
            1.  Send an exception chain in the ComputationResult if either
                    -   coord is flagged unsafe.
                    -   The vector_builder throws an error
            2.  Otherwise, wrap the payload in a ComputationResult.
            3.  Send the success result.
        Args:
            coord: Coord
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        Result:
            ComputationResult[Vector]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}._coord_to_vector"
        
        # Handle the case that, coord is unsafe.
        coord_validation_result = coord_service.validate(coord)
        if coord_validation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=coord_validation_result.exception,
                )
            )
        # --- Do the conversion work. ---#
        conversion_result = vector_service.builder.build(
            x=coord.column,
            y=coord.row,
            number_validator=number_validator,
        )
        # Handle the case that, the conversion was unsuccessful.
        if conversion_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=conversion_result.exception,
                )
            )
        # --- Forward the work product. ---#
        return ComputationResult.success(conversion_result.payload)