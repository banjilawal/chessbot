# src/validator/itinerary/consistency/validator.py

"""
Module: validator.itinerary.consistency.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import ItineraryConsistencyException
from model import Itinerary
from result import ValidationResult
from toolkit import ItineraryToolkit
from util import LoggingLevelRouter
from validator import ItineraryDestinationConsistencyValidator, ItinerarySourceConsistencyValidator


class ItineraryConsistencyValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure at point of use, an itinerary's token:
                Has no relationship with its destination.
                Has a bidirectional relationship with its source.

    Attributes:

    Provides:
        -   def validate(
                    itinerary: Itinerary,
                    toolkit: ItineraryToolkit,
                    source_consistency_validator: ItinerarySourceConsistencyValidator,
                    destination_consistency_validator: ItineraryDestinationConsistencyValidator,
            ) -> ValidationResult[Token]:

    Super Class:
    """
    OPERATION_NAME = "itinerary_consistency_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            itinerary: Itinerary,
            toolkit: ItineraryToolkit | None = None,
            source_consistency_validator: ItinerarySourceConsistencyValidator | None = None,
            destination_consistency_validator: ItineraryDestinationConsistencyValidator | None = None,
    ) -> ValidationResult[Itinerary]:
        """
        Verify there is consistency between the itinerary's elements.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   There is a token-source inconsistency.
                    -   There is token-destination inconsistency.
            2.  Otherwise, send the success result.
        Args:
            itinerary: Itinerary
            toolkit: ItineraryToolkit
            source_consistency_validator: ItinerarySourceConsistencyValidator
            destination_consistency_validator: ItineraryDestinationConsistencyValidator
        Returns:
            ValidationResult[Itinerary]
        Raises:
            ItineraryConsistencyException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ItineraryToolkit()
        if source_consistency_validator is None:
            source_consistency_validator = ItinerarySourceConsistencyValidator()
        if destination_consistency_validator is None:
            destination_consistency_validator = ItineraryDestinationConsistencyValidator()
        
        # Handle the case that, the token has an inconsistency with the source.
        source_consistency_result = source_consistency_validator.execute(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        if source_consistency_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=source_consistency_result.exception,
                )
            )
        # Handle the case that, the token has an inconsistency with the destination.
        destination_consistency_result = destination_consistency_validator.validate(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        if destination_consistency_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=destination_consistency_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)
