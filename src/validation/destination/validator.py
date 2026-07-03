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
from toolkit import TokenEndpointRelationToolkit
from util import LoggingLevelRouter


class TokenDestinationRelationValidator:
    """
    Role
        -   Validation Worker
        -   Integrity Maintenance
        -   Consistency Assurance

    Responsibilities:
        1.  Verify a Token neither has, a partial nor fully bidirectional relation it wants 
            to visit.
        2.  Prevents circular square visits. 

    Attributes:

    Provides:
        -   def execute(
                    token: Token,
                    destination: Square,
                    toolkit: TokenEndpointRelationToolkit,
            ) -> ValidationResult[Square]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "token_destination_relation_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            token: Token,
            destination: Square,
            toolkit: TokenEndpointRelationToolkit | None = None,
    ) -> ValidationResult[Square]:
        """
        Makes sure a Token is not already in a Square it wants to visit.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The relation analysis is not completed.
                    -   The token is either fully or partially bound to the destination.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            destination: Square
            toolkit: TokenEndpointRelationToolkit
        Returns:
            ValidationResult
        Raises:
            TokenDestinationRelationValidatorException
            TokenAlreadyAtDestinationException
            PartialTokenDestinationRelationException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenEndpointRelationToolkit
        
        # --- Run the relation analyzer. ---#
        relation_analysis_result = toolkit.relation_analyzer.analyze(
            candidate_primary=destination,
            candidate_satellite=token,
            token_validator=toolkit.token_validator,
            square_validator=toolkit.square_validator,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenDestinationRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenDestinationRelationValidatorException.MSG,
                    err_code=TokenDestinationRelationValidatorException.ERR_CODE,
                    ex=relation_analysis_result.exception,
                )
            )
        # --- Extract the relation report for additional tests. ---#
        relation = cast(RelationReport, relation_analysis_result.payload)
        
        # Handle the case that the token has an unexpected partial binding to the destination.
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
        # Handle the case that, the token is already at the destination.
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
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(destination)