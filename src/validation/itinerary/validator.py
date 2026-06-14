# src/validation/itinerary/validator.py

"""
Module: validation.itinerary.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import ItinerarySourceEqualsDestinationException, ItineraryValidationException
from model import Itinerary
from result import ValidationResult
from toolkit import ItineraryToolkit
from util import LoggingLevelRouter
from validation import ItineraryConsistencyValidator, Validator


class ItineraryValidator(Validator[Itinerary]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure an Itinerary instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    itinerary: Itinerary,
                    toolkit: ItineraryToolkit,
                    consistency_validator: ItineraryConsistencyValidator,
            ) -> ValidationResult[Token]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "itinerary_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: ItineraryToolkit | None = None,
            consistency_validator: ItineraryConsistencyValidator | None = None,
    ) -> ValidationResult[Itinerary]:
        """
        Verify the object is an Itinerary that is safe to use.
        Action:
            1.  Send an exception chan in the validation result if any of the following occur:
                    -   The candidate is null or the wrong type.
                    -   Either the token, source or destination are not valid.
                    -   The source and destination are the same.
                    -   The itinerary has an inconsistency.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: ItineraryToolkit
            consistency_validator: ItineraryConsistencyValidator
        Returns:
            ValidationResult[Itinerary]
        Raises:
            ItineraryValidationException
            ItinerarySourceEqualsDestinationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ItineraryToolkit()
        if consistency_validator is None:
            consistency_validator = ItineraryConsistencyValidator()
        
        # Use the validation primer for existence and type checking.
        validation_priming_result = toolkit.validation_primer.validate(
            candidate=candidate,
            target_model=toolkit.model_type,
            context_null_exception=toolkit.null_exception,
        )
        # Handle the case that, the base checks are not passed.
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast the candidate into an Itinerary for additional tests ---#
        itinerary = cast(Itinerary, candidate)
        
        # Handle the case that, either the source or destination fail a validation check.
        for square in [itinerary.source, itinerary.destination]:
            square_validation_result = toolkit.square_validator.validate(square)
            if square_validation_result.is_failure:
                if validation_priming_result.is_failure:
                    # Send the exception chain on failure.
                    return ValidationResult.failure(
                        ItineraryValidationException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=ItineraryValidationException.MSG,
                            err_code=ItineraryValidationException.ERR_CODE,
                            ex=square_validation_result.exception,
                        )
                    )
        # Handle the case, that the source and destination are the same.
        if itinerary.source == itinerary.destination:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=ItinerarySourceEqualsDestinationException(
                        msg=ItinerarySourceEqualsDestinationException.MSG,
                        err_code=ItinerarySourceEqualsDestinationException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token fails a validation check.
        token_validation_result = toolkit.token_validator.validate(itinerary.token)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that, the itinerary has an inconsistency.
        consistency_validation_result = consistency_validator.validate(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        if consistency_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=consistency_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)