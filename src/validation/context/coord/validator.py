# src/validation/context/coord/operation.py

"""
Module: validation.context.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import CoordContextValidationException
from model import CoordContext
from result import ValidationResult
from setting import BoardProperty
from toolkit import CoordContextToolkit
from util import LoggingLevelRouter
from validation import Validator


class CoordContextValidator(Validator[CoordContext]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a CoordContext instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: CoordContextToolkit,
            ) -> ValidationResult[CoordContext]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: CoordContextToolkit | None = None,
    ) -> ValidationResult[CoordContext]:
        """
        Certify a candidate is a CoordContext that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            toolkit: CoordContextToolkit,
        Returns:
            ValidationResult[CoordContext]
        Raises:
            CoordContextValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = CoordContextToolkit()
        
        # handle the case that, priming the validator fails.
        priming_result = toolkit.context_validation_primer.validate(
            candidate=candidate,
            context_model=toolkit.context_model_type,
            null_exception=toolkit.null_context_exception,
            validator_bootstrapper=toolkit.coord_toolkit.validation_primer
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=CoordContextValidationException.MSG,
                    err_code=CoordContextValidationException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareContext for routing attribute testing. ---#
        context = cast(CoordContext, candidate)
        
        # Certification whichever attribute is enabled.
        for attribute in [context.row, context.column]:
            validation_result = toolkit.coord_toolkit.number_validator.validate(
                candidate=attribute,
                ceiling=BoardProperty.MAX_COLUMN_INDEX.value,
                floor=0,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CoordContextValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CoordContextValidationException.MSG,
                        err_code=CoordContextValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(context)

        



