# src/integrity/validation/context/vector/validator.py

"""
Module: integrity.validation.context.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from integrity import Validator
from model import Coord, VectorContext, Vector
from result import ValidationResult
from system import LoggingLevelRouter
from toolkit  import VectorContextToolkit
from err import (
    ExcessVectorContextFlagsException, VectorContextNullException, VectorContextValidationException,
    ZeroVectorContextFlagsException
)



class VectorContextValidator(Validator[VectorContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorContext instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : VectorContextToolSe,
            ) -> ValidationResult[VectorContext]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: VectorContextToolkit = None,
    ) -> ValidationResult[VectorContext]:
        """
        Verify the candidate is a safe VectorContext.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorContext.
                    -   The vectorContext's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit : VectorContextToolkit
        Returns:
            ValidationResult[VectorContext]
        Raises:
            TypeError
            VectorContextNullException
            ZeroVectorContextFlagsException
            VectorContextValidationException
            ExcessVectorContextFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = VectorContextToolkit()
            
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextValidationException.MSG,
                    err_code=VectorContextValidationException.ERR_CODE,
                    ex=VectorContextNullException(
                        msg=VectorContextNullException.MSG,
                        err_code=VectorContextNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is wrong type.
        if not isinstance(candidate, VectorContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextValidationException.MSG,
                    err_code=VectorContextValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected Vector type, got ({candidate}.__name__) instead."
                    )
                )
            )
        # --- Cast candidate to a VectorContext for additional tests. ---#
        context = cast(VectorContext, candidate)
        
        # Handle the case that neither option is enabled.
        if len(context.to_dict) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextValidationException.MSG,
                    err_code=VectorContextValidationException.ERR_CODE,
                    ex=ZeroVectorContextFlagsException(
                        msg=ZeroVectorContextFlagsException.MSG,
                        err_code=ZeroVectorContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if len(context.to_dict) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextValidationException.MSG,
                    err_code=VectorContextValidationException.ERR_CODE,
                    ex=ExcessVectorContextFlagsException(
                        msg=ExcessVectorContextFlagsException.MSG,
                        err_code=ExcessVectorContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Assign to the correct service for the final step. ---#
        validation_result = None
        if isinstance(context.vector, Vector):
            validation_result = toolkit.vector_service.validator.validate(context.vector)
        if isinstance(context.coord, Coord):
            validation_result = toolkit.coord_service.validator.validate(context.to_dict)
            
        # Handle the case that context was flagged.
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorContextValidationException.MSG,
                    err_code=VectorContextValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(context)

            