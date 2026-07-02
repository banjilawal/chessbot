# src/validation/destination/validator.py

"""
Module: validation.destination.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from analyzer import SquareTokenRelationAnalyzer
from err import (
    TokenDestinationRelationValidatorException, PartialTokenDestinationRelationException,
    TokenAlreadyAtDestinationException
)
from model import Square, Token
from report import RelationReport
from result import ValidationResult
from util import LoggingLevelRouter
from validation import SquareValidator, TokenValidator


class TokenDestinationRelationValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Verify a Token neither has, a partial nor fully bidirectional relation it wants 
            to visit.
        2.  Prevents circular square visits. 

    Attributes:

    Provides:
        -   def execute(
                    token: Token,
                    destination: Square,
                    token_validator: TokenValidator | None = None,
                    square_validator: SquareValidator | None = None,
                    relation_analyzer: SquareTokenRelationAnalyzer | None = None,
            ) -> ValidationResult[Square]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "token_destination_relation_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            destination: Square,
            token_validator: TokenValidator | None = None,
            square_validator: SquareValidator | None = None,
            relation_analyzer: SquareTokenRelationAnalyzer | None = None,
    ) -> ValidationResult[Square]:
        """
        Makes sure a Token is not already in a Square it wants to visit.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The relation analysis is not completed.
                    -   There is a partial binding between the token and destination.
                    -   The token and destination have a bidirectional relationship.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            destination: Square
            token_validator: TokenValidator
            square_validator: SquareValidator
            relation_analyzer: SquareTokenRelationAnalyzer
        Returns:
            ValidationResult
        Raises:
            TokenDestinationRelationValidatorException
            TokenAlreadyAtDestinationException
            PartialTokenDestinationRelationException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if token_validator is None:
            token_validator = TokenValidator()
        if square_validator is None:
            square_validator = SquareValidator()
        if relation_analyzer is None:
            relation_analyzer = SquareTokenRelationAnalyzer()
        
        # --- Run the relation analyzer. ---#
        relation_analysis = relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=token,
            token_validator=token_validator,
            square_validator=square_validator,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_analysis.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDestinationRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenDestinationRelationValidatorException.MSG,
                    err_code=TokenDestinationRelationValidatorException.ERR_CODE,
                    ex=relation_analysis.exception,
                )
            )
        # Handle the case that the token has an unexpected partial binding to the destination.
        relation = cast(RelationReport, relation_analysis.payload)
        if (
                relation.stale_link_exists or
                relation.registration_missing
        ):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDestinationRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenDestinationRelationValidatorException.MSG,
                    err_code=TokenDestinationRelationValidatorException.ERR_CODE,
                    ex=PartialTokenDestinationRelationException(
                        msg=PartialTokenDestinationRelationException.MSG,
                        err_code=PartialTokenDestinationRelationException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the token has an unexpected full binding with the destination.
        if relation.fully_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDestinationRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenDestinationRelationValidatorException.MSG,
                    err_code=TokenDestinationRelationValidatorException.ERR_CODE,
                    ex=TokenAlreadyAtDestinationException(
                        msg=TokenAlreadyAtDestinationException.MSG,
                        err_code=TokenAlreadyAtDestinationException.ERR_CODE,
                    ),
                )
            )
        # --- Token is not at the destination. Forward the work product to the caller. ---#
        return ValidationResult.success(destination)