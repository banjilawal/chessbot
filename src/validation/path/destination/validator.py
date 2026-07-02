# src/validation/itinerary/consistency/destination/validator.py

"""
Module: validation.itinerary.consistency.destination.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import SquareTokenRelationAnalyzer
from err import (
    ItineraryConsistencyException, PartialTokenDestinationBindingException,
    TokenAlreadyAtDestinationException
)
from model import Square, Token
from report import RelationReport
from result import ValidationResult
from util import LoggingLevelRouter


class DestinationRelationValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure an itinerary's token and destination do not have a relationship before its used.

    Attributes:

    Provides:
        -   def execute(
                    itinerary: Itinerary,
                    relation_analyzer: SquareTokenRelationAnalyzer,
            ) -> ValidationResult[Token]:

    Super Class:
    """
    OPERATION_NAME = "itinerary_destination_consistency_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            destination: Square,
            relation_analyzer: SquareTokenRelationAnalyzer | None = None,
    ) -> ValidationResult[Square]:
        """
        Verify there is no relationship between the itinerary's token and destination.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   There is a partial binding between the token and destination.
                    -   The token and destination have a bidirectional relationship.
            2.  Otherwise, send the success result.
        Args:
            itinerary: Itinerary
            relation_analyzer: SquareTokenRelationAnalyzer
        Returns:
            ValidationResult[Itinerary]
        Raises:
            ItineraryConsistencyException
            TokenAlreadyAtDestinationException
            PartialTokenDestinationBindingException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if relation_analyzer is None:
            relation_analyzer = SquareTokenRelationAnalyzer()
        
        # --- Test the has no relation with the destination. ---#
        relation_result = relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=relation_result.exception,
                )
            )
        # Handle the case that the token has an unexpected partial binding to the destination.
        relation = cast(RelationReport, relation_result.payload)
        if (
                relation.stale_link_exists or
                relation.registration_missing
        ):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=PartialTokenDestinationBindingException(
                        msg=PartialTokenDestinationBindingException.MSG,
                        err_code=PartialTokenDestinationBindingException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token has an unexpected full binding with the destination.
        if relation.fully_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=TokenAlreadyAtDestinationException(
                        msg=TokenAlreadyAtDestinationException.MSG,
                        err_code=TokenAlreadyAtDestinationException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(destination)