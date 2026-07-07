# src/validator/itinerary/consistency/sourcey/validator.py

"""
Module: validator.itinerary.consistency.source.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from err import BidirectionalSourceTokenRelationException, ItineraryConsistencyException
from model import Itinerary
from report import RelationReport
from result import ValidationResult
from toolkit import ItineraryToolkit
from util import LoggingLevelRouter
from validator import Validator


class ItinerarySourceConsistencyValidator(Validator[Itinerary]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure an itinerary's token and source have a bidirectional relation before its used.

    Attributes:

    Provides:
        -   def validate(
                    itinerary: Itinerary,
                    toolkit: ItineraryToolkit,
            ) -> ValidationResult[Token]:

    Super Class:
    """
    OPERATION_NAME = "itinerary_source_consistency_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            itinerary: Itinerary,
            toolkit: ItineraryToolkit | None = None,
    ) -> ValidationResult[Itinerary]:
        """
        Verify there the itinerary's token and source have a bidirectional relationship.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The square-token relation analysis is not completed.
                    -   There relation between the token and its source is not fully bidirectional.
            2.  Otherwise, send the success result.
        Args:
            itinerary: Itinerary
            toolkit: ItineraryToolkit
        Returns:
            ValidationResult[Itinerary]
        Raises:
            ItineraryConsistencyException
            NoSourceTokenRelationException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ItineraryToolkit()
        
        relation_result = toolkit.square_token_relation_analyzer.execute(
            candidate_primary=itinerary.source,
            candidate_satellite=itinerary.token,
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
        # Handle the case that, the token does not have a bidirectional relation with its source.
        relation = cast(RelationReport, relation_result.payload)
        if not relation.fully_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryConsistencyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryConsistencyException.MSG,
                    err_code=ItineraryConsistencyException.ERR_CODE,
                    ex=BidirectionalSourceTokenRelationException(
                        msg=BidirectionalSourceTokenRelationException.MSG,
                        err_code=BidirectionalSourceTokenRelationException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)