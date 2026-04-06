# src/logic/geometry/resource/integrity/validator/validator.py

"""
Module: logic.geometry.resource.integrity.validator.validator
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from __future__ import annotations

from typing import Union, cast

from logic.coord import Coord
from model.geometry.vector import Vector
from system import LoggingLevelRouter, ValidationResult
from math.geometry import (
    GeometryIntegrityWorkers, VectorCoordUnionNullException, VectorCoordUnionValidatorException
)




class VectorCoordUnionValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Coord instance is certified safe, reliable and consistent before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Union[Vector, Coord],
                    workers: GeometryIntegrityWorkers = GeometryIntegrityWorkers(),
            ) -> ValidationResult[Union[Vector, Coord]]:

    Super Class:
        Worker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Union[Vector, Coord],
            workers: GeometryIntegrityWorkers = GeometryIntegrityWorkers(),
    ) -> ValidationResult[Union[Vector, Coord]]:
        """
        Verify that the Union[Vector, Coord] is safe to use.
        
        Action:
            1.  Send and exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a Union.
                    -   The union's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Union[Vector, Coord],
            workers: GeometryIntegrityWorkers = GeometryIntegrityWorkers(),
        Returns:
            ValidationResult[Union[Vector, Coord]
        Raises:
            TypeError
            NullAlgebraAContextException
            AlgebraContextValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorCoordUnionValidatorException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordUnionValidatorException.OP,
                    msg=VectorCoordUnionValidatorException.MSG,
                    err_code=VectorCoordUnionValidatorException.ERR_CODE,
                    rslt_type=VectorCoordUnionValidatorException.RSLT_TYPE,
                    ex=VectorCoordUnionNullException(
                        msg=VectorCoordUnionNullException.MSG,
                        err_code=VectorCoordUnionNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is neither a Vector or Coord.
        if not isinstance(candidate, (Vector, Coord)):
            return ValidationResult.failure(
                VectorCoordUnionValidatorException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordUnionValidatorException.OP,
                    msg=VectorCoordUnionValidatorException.MSG,
                    err_code=VectorCoordUnionValidatorException.ERR_CODE,
                    rslt_type=VectorCoordUnionValidatorException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected either (Vector, Coord), got "
                        f"type({candidate}.__name__) instead."
                    )
                )
            )
        # --- Proceed with validating either a vector or coord. ---#

        if isinstance(candidate, Vector):
            # --- Cast to vector. ---#
            vector = cast(Vector, candidate)
            
            # Handle the case that, the vector is unsafe.
            vector_validation_result = workers.vector_service.validate(
                candidate=vector,
                number_validator=workers.number_validator,
            )
            if vector_validation_result.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    VectorCoordUnionValidatorException(
                        mthd=method,
                        title=cls.__name__,
                        op=VectorCoordUnionValidatorException.OP,
                        msg=VectorCoordUnionValidatorException.MSG,
                        err_code=VectorCoordUnionValidatorException.ERR_CODE,
                        rslt_type=VectorCoordUnionValidatorException.RSLT_TYPE,
                        ex=vector_validation_result.exception,
                    )
                )
            # --- Forward the work product to the caller ---#
            return ValidationResult.success(vector)
        
        # --- Process alternate case. ---#
        coord = cast(Coord, candidate)
        
        # Handle the case that, the coord is unsafe.
        coord_validation_result = workers.coord_service.validate(
            candidate=coord,
            number_validator=workers.number_validator,
        )
        if coord_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorCoordUnionValidatorException(
                    mthd=method,
                    title=cls.__name__,
                    op=VectorCoordUnionValidatorException.OP,
                    msg=VectorCoordUnionValidatorException.MSG,
                    err_code=VectorCoordUnionValidatorException.ERR_CODE,
                    rslt_type=VectorCoordUnionValidatorException.RSLT_TYPE,
                    ex=coord_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(coord)
        
            