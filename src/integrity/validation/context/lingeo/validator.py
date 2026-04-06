# src/integrity/validation/context/linegeo/validator.py

"""
Module: integrity.validation.context.linegeo.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from integrity import Validator
from model import LinGeoContext, Vector
from result import ValidationResult
from system import LoggingLevelRouter
from tool import LinGeoContextToolSet
from err import (
    ExcessLinGeoContextFlagsException, LinGeoContextNullException, LinGeoContextValidationException,
    ZeroLinGeoContextFlagsException
)



class LinGeoContextValidator(Validator[LinGeoContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a LinGeoContext instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    tool_set: LinGeoContextToolSe,
            ) -> ValidationResult[LinGeoContext]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet(),
    ) -> ValidationResult[LinGeoContext]:
        """
        Verify the candidate is a safe LinGeoContext.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a LinGeoContext.
                    -   The linGeoContext's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            tool_set: LinGeoContextToolSet
        Returns:
            ValidationResult[LinGeoContext]
        Raises:
            TypeError
            LinGeoContextNullException
            ZeroLinGeoContextFlagsException
            LinGeoContextValidationException
            ExcessLinGeoContextFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                LinGeoContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextValidationException.MSG,
                    err_code=LinGeoContextValidationException.ERR_CODE,
                    ex=LinGeoContextNullException(
                        msg=LinGeoContextNullException.MSG,
                        err_code=LinGeoContextNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is wrong type.
        if not isinstance(candidate, LinGeoContext):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                LinGeoContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextValidationException.MSG,
                    err_code=LinGeoContextValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected LinGeo type, got ({candidate}.__name__) instead."
                    )
                )
            )
        # --- Cast candidate to a LinGeoContext for additional tests. ---#
        context = cast(LinGeoContext, candidate)
        
        # Handle the case that neither option is enabled.
        if len(context.to_dict) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                LinGeoContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextValidationException.MSG,
                    err_code=LinGeoContextValidationException.ERR_CODE,
                    ex=ZeroLinGeoContextFlagsException(
                        msg=ZeroLinGeoContextFlagsException.MSG,
                        err_code=ZeroLinGeoContextFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if len(context.to_dict) > 1:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                LinGeoContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextValidationException.MSG,
                    err_code=LinGeoContextValidationException.ERR_CODE,
                    ex=ExcessLinGeoContextFlagsException(
                        msg=ExcessLinGeoContextFlagsException.MSG,
                        err_code=ExcessLinGeoContextFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Assign to the correct service for the final step. ---#
        validation_result = None
        if isinstance(context.vector, Vector):
            validation_result = tool_set.vector_service.validator.validate(context.vector)
        else:
            validation_result = tool_set.coord_service.validator.validate(context.to_dict)
            
        # Handle the case that context was flagged.
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                LinGeoContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoContextValidationException.MSG,
                    err_code=LinGeoContextValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(context)

            