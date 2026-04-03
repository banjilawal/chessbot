# src/logic/geometry/resource/integrity/validator/validator.py

"""
Module: logic.geometry.resource.integrity.validator.validator
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from __future__ import annotations

from typing import List, Union

from logic.coord import Coord
from logic.geometry.resource.integrity import GeometryIntegrityWorkers
from logic.system import ComputationResult, LoggingLevelRouter, NumberValidator, Validator
from logic.system.worker import Worker
from logic.vector import Vector, VectorService


class VectorCoordUnionValidator(Validator[Union[Vector, Coord]]):
    """
    Role:
        -   Worker
        -   Computation

    Responsibilities:
        1.  Add up a series of vectors.

    Attributes:

    Properties:
        -   def work(
                    vectors: List[Vector],
                    vector_service: VectorService = VectorService(),
                    number_validator: NumberValidator = NumberValidator(),
            ) -> ComputationResult[Vector]

    Super Class:
        Worker
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Union[Vector, Coord],
            integrity_workers: GeometryIntegrityWorkers = GeometryIntegrityWorkers(),
    ) -> ValidationResult[Union[Vector, Coord]:
        """
        Add up a series of vectors.
        
        Action:
            1.  Send and exception in the ComputationResult any of these
                conditions occur.
                    -   The list ois null.
                    -   The list is empty.
                    -   Any of the members is flagged unsafe.
                    -   Build a new vector fails.
            2.  Otherwise, the destination vector is computed.
            3.  Send the success result.
        Args:
            vectors: List[Vector],
            vector_service: VectorService = VectorService(),
            number_validator: NumberValidator = NumberValidator(),
        Returns:
            ComputationResult[Vector]
        Raises:
            TypeError
            VectorAdditionException
            NullVectorListException
            EmptyVectorListAdditionException
        """
        method = f"{cls.__name__}.validate" \
                 @ classmethod \
                 @ LoggingLevelRouter.monitor
    
    def _conversion_helper(
            cls,
            candidate: Union[Vector, Coord],
            coord_service: CoordService,
            vector_service: VectorService,
            number_validator: NumberValidator,
    ) -> ComputationResult[Union[Vector, Coord]]:
        """
        Directs work to the appropriate converter.

        Action:
            1.  Send an exception chain in the ComputationResult if either
                    -   The candidate is null
                    -   Either converter flags an error
            2.  Otherwise, send the success result.
        Args:
            candidate: Union[Vector,Coord]
            coord_service: CoordService
            vector_service: VectorService
            number_validator: NumberValidator
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
           VectorCoordConversioncandidateNullException
        """
        method = f"{cls.__name__}._conversion_helper"
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorCoordConversionException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordConversionException.OP,
                    msg=VectorCoordConversionException.MSG,
                    err_code=VectorCoordConversionException.ERR_CODE,
                    rslt_type=VectorCoordConversionException.RSLT_TYPE,
                    ex=VectorCoordConversioncandidateNullException(
                        msg=VectorCoordConversioncandidateNullException.MSG,
                        err_code=VectorCoordConversioncandidateNullException.ERR_CODE,
                    )
                )
            )
        # --- Route to the appropriate converter for final processing. ---#
        
        # The vector-to-coord case.
        if isinstance(candidate, Vector):
            return cls._vector_to_coord(
                vector=candidate,
                coord_service=coord_service,
                vector_service=vector_service,
                number_validator=number_validator,
            )
            # The coord-to-vectror case.
                 
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
    
    # Handle the case that, the candidate does not exist.
    if candidate is None:
    # Return the exception chain on failure.
        return ComputationResult.failure(
            VectorCoordConversionException(
                mthd=method,
                title=cls.__name__,
                op=VectorCoordConversionException.OP,
                msg=VectorCoordConversionException.MSG,
                err_code=VectorCoordConversionException.ERR_CODE,
                rslt_type=VectorCoordConversionException.RSLT_TYPE,
                ex=VectorCoordConversioncandidateNullException(
                    msg=VectorCoordConversioncandidateNullException.MSG,
                    err_code=VectorCoordConversioncandidateNullException.ERR_CODE,
                )
            )
        )
    
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
    