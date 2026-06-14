# src/validation/itinerary/validator.py

"""
Module: validation.itinerary.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import (
    ItineraryNullException, ItinerarySourceEqualsDestinationException, ItineraryValidationException,
    BidirectionalSourceTokenRelationException, TokenAlreadyAtDestinationException, TokenDestinationPartialBindingException
)
from model import Itinerary
from report import RelationReport
from result import ValidationResult
from toolkit import ItineraryToolkit, Toolkit
from util import LoggingLevelRouter
from validation import Validator


class ItineraryValidator(Validator[Itinerary]):
    """
    Role:Validation, Data Integrity And Reliability Guarantor

    Responsibilities:
    1.  Produce Itinerary instances whose integrity is guaranteed at creation.
    2.  Manage construction of Itinerary instances that can be used safely by the client.
    3.  Ensure params for Itinerary creation have met the application's safety contract.
    4.  Return an exception to the client if a Validation resource does not satisfy integrity requirements.

    Super Class:
        *   Validation

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    OPERATION_NAME = "itinerary_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: ItineraryToolkit | None = None,
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
        # --- Integrity tests are passed. Perform consistency checks. ---#
        
        # Handle the case that, the itinerary has an inconsistency.
        consistency_validation_result = cls._consistency_validator(
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
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _consistency_validator(
        cls,
        itinerary: Itinerary,
        toolkit: ItineraryToolkit,
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
        Returns:
            ValidationResult[Itinerary]
        Raises:
            ItineraryConsistencyException
        """
        method = f"{cls.__name__}._consistency_validator"
        
        # Handle the case that, the token has an inconsistency with the source.
        source_consistency_result = cls._source_consistency_validator(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        if source_consistency_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=source_consistency_result.exception,
                )
            )
        # Handle the case that, the token has an inconsistency with the destination.
        destination_consistency_result = cls._destination_consistency_validator(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        if destination_consistency_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=destination_consistency_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _source_consistency_validator(
            cls,
            itinerary: Itinerary,
            toolkit: ItineraryToolkit,
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
        method = f"{cls.__name__}._source_consistency_validator"
        
        relation_result = toolkit.square_token_relation_analyzer.analyze(
            candidate_primary=itinerary.source,
            candidate_satellite=itinerary.token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=relation_result.exception,
                )
            )
        # Handle the case that, the token does not have a bidirectional relation with its source.
        relation = cast(RelationReport, relation_result.payload)
        if not relation.fully_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=BidirectionalSourceTokenRelationException(
                        msg=BidirectionalSourceTokenRelationException.MSG,
                        err_code=BidirectionalSourceTokenRelationException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _destination_consistency_validator(
            cls,
            itinerary: Itinerary,
            toolkit: ItineraryToolkit,
    ) -> ValidationResult[Itinerary]:
        """
        Verify there is no relationship between the itinerary's token and destination.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   There is a partial binding between the token and destination.
                    -   The token and destination have a bidirectional relationship.
            2.  Otherwise, send the success result.
        Args:
            itinerary: Itinerary
            toolkit: ItineraryToolkit
        Returns:
            ValidationResult[Itinerary]
        Raises:
            ItineraryConsistencyException
            TokenAlreadyAtDestinationException
            TokenDestinationPartialBindingException
        """
        method = f"{cls.__name__}._destination_consistency_validator"

        # --- Test the has no relation with the destination. ---#
        relation_result = toolkit.square_token_relation_analyzer.analyze(
            candidate_primary=itinerary.destination,
            candidate_satellite=itinerary.token,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
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
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=TokenDestinationPartialBindingException(
                        msg=TokenDestinationPartialBindingException.MSG,
                        err_code=TokenDestinationPartialBindingException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token has an unexpected full binding with the destination.
        if relation.fully_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ItineraryValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ItineraryValidationException.MSG,
                    err_code=ItineraryValidationException.ERR_CODE,
                    ex=TokenAlreadyAtDestinationException(
                        msg=TokenAlreadyAtDestinationException.MSG,
                        err_code=TokenAlreadyAtDestinationException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(itinerary)