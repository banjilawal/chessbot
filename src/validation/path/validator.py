# src/validation/itinerary/consistency/validator.py

"""
Module: validation.itinerary.consistency.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Square, Token
from util import LoggingLevelRouter


class TokenPathValidator:
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
                    origin_relation_analyzer: OriginRelationValidator,
                    destination_relation_analyzer: DestinationTokenRelationAnalyzer,
            ) -> ValidationResult[Token]:

    Super Class:
    """
    OPERATION_NAME = "itinerary_consistency_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validator(
            cls,
            candidate
            token: Token,
            origin: Square,
            destination: Square,
            origin_relation_validator: OriginRelationValidator | None = None,
            destination_analyzer: DestinationTokenRelationAnalyzer | None = None,
    ) -> ValidationResult[int]:
        """
        Verify there is consistency between the itinerary's elements.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   There is a token-source inconsistency.
                    -   There is token-destination inconsistency.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            origin: Square
            destination: Square
            origin_relation_validator: OriginRelationValidator
            destination_analyzer: DestinationTokenRelationAnalyzer
        Returns:
            ValidationResult[int]
        Raises:
            ItineraryConsistencyException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if origin_relation_validator is None:
            origin_relation_validator = OriginRelationValidator()
        if destination_analyzer is None:
            destination_analyzer = DestinationTokenRelationAnalyzer()
        
        # Handle the case that, the token has an inconsistency with the source.
        origin_relation_analysis = origin_relation_validator.execute(
            token=token,
            origin=origin,
        )
        if origin_relation_analysis.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=origin_relation_analysis.exception,
                )
            )

        # Handle the case that, the token has an inconsistency with the destination.
        destination_result = destination_analyzer.validate(
            token=token,
            destination=destination,
        )
        if destination_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=destination_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(2)
        
        
