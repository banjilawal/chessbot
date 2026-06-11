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
    NoSourceTokenRelationException, TokenAlreadyAtDestinationException, TokenDestinationPartialRelationException
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
        Action:
            1.  verify itinerary_variety is a not-null ItineraryVariety object.
            2.  Use itinerary_variety to pick which Validation method will create the concrete Itinerary object.
        Args:
            *   rank (int)
            *   token_service (TokenService)
            *   square_validator (SquareService)
            *   identity_service (IdentityService)
        Returns:
            *   ValidationResult[Itinerary] containing either:
                    - On failure: Exception.
                    - On success: Itinerary in the payload.
        Raises:
            *   TypeError
            *   NullItineraryException
            *   KingCannotBeCapturedException
            *   TokenCannotCaptureItselfException
            *   FriendCannotCaptureFriendException
            *   PrisonerCapturedByDifferentEnemyException
            *   UnformedTokenCannotBeVictorException
            *   PrisonerCannotBeActiveCombatantException
            *   ItineraryValidationException
            *   VictorAndPrisonerOnDifferentBoardsException
            *   PrisonerAlreadyHasItineraryException
            *   PrisonerCapturedOnDifferentSquareException
        """
        method = f"ItineraryValidator.validate"
        
        # Handle the case that, the candidate does not exist.
        validation_priming_result = toolkit.validation_primer.validate(
            candidate=candidate,
            target_model=Itinerary,
            context_null_exception=toolkit.null_exception,
        )
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
        # --- Cast the candidate into a Token for additional tests ---#
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
        # --- Test the token's consistency with its source. ---#
        consistency_validation_result = cls._consistency_validator(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        # Handle the case that, the itinerary has an inconsistency.
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
        # --- Candidate has been successfully validated. Return to the caller. ---#
        return ValidationResult.success(itinerary)
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _consistency_validator(
        cls,
        itinerary: Itinerary,
        toolkit: ItineraryToolkit,
    ) -> ValidationResult[Itinerary]:
        method = f"{cls.__name__}._consistency_validator"
        
        source_consistency_result = cls._source_consistency_validator(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        # Handle the case that, the source has an inconsistency with the token.
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
        
        destination_consistency_result = cls._destination_consistency_validator(
            itinerary=itinerary,
            toolkit=toolkit,
        )
        # Handle the case that, the source has an inconsistency with the token.
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
        # --- Candidate has been successfully validated. Return to the caller. ---#
        return ValidationResult.success(itinerary)
        
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _source_consistency_validator(
            cls,
            itinerary: Itinerary,
            toolkit: ItineraryToolkit,
    ) -> ValidationResult[Itinerary]:
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
                    ex=NoSourceTokenRelationException(
                        msg=NoSourceTokenRelationException.MSG,
                        err_code=NoSourceTokenRelationException.ERR_CODE,
                    ),
                )
            )
        # --- Candidate has been successfully validated. Return to the caller. ---#
        return ValidationResult.success(itinerary)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _destination_consistency_validator(
            cls,
            itinerary: Itinerary,
            toolkit: ItineraryToolkit,
    ) -> ValidationResult[Itinerary]:
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
                    ex=TokenDestinationPartialRelationException(
                        msg=TokenDestinationPartialRelationException.MSG,
                        err_code=TokenDestinationPartialRelationException.ERR_CODE,
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
        # --- Candidate has been successfully validated. Return to the caller. ---#
        return ValidationResult.success(itinerary)