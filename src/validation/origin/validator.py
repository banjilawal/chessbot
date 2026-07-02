# src/validation/origin/validator.py

"""
Module: validation.origin.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from analyzer import SquareTokenRelationAnalyzer
from err import TokenOriginRelationNullException, TokenOriginRelationValidatorException
from model import Square, Token
from report import RelationReport
from result import ValidationResult
from util import LoggingLevelRouter
from validation import SquareValidator, TokenValidator


class TokenOriginRelationValidator:
    """
    Role
        -   Validation Worker
        -   Integrity Maintenance
        -   Consistency Assurance

    Responsibilities:
        1.  Verify a Token has a fully bidirectional relation with the Square it wants
            to travel from

    Attributes:

    Provides:
        -   def execute(
                    token: Token,
                    origin: Square,
                    token_validator: TokenValidator | None = None,
                    square_validator: SquareValidator | None = None,
                    relation_analyzer: SquareTokenRelationAnalyzer | None = None,
            ) -> ValidationResult[Square]:

    Super Class:
    """
    OPERATION_NAME = "token_origin_relation_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            origin: Square,
            token_validator: TokenValidator | None = None,
            square_validator: SquareValidator | None = None,
            relation_analyzer: SquareTokenRelationAnalyzer | None = None,
    ) -> ValidationResult[Square]:
        """
        Makes sure a Token is not already in a Square it wants to visit.

        Action:
            1.  Send an exception chan in the validation result if either:
                    -   The relation analysis is not completed.
                    -   There is a partial binding between the token and origin.
                    -   The token and origin have a bidirectional relationship.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            origin: Square
            token_validator: TokenValidator
            square_validator: SquareValidator
            relation_analyzer: SquareTokenRelationAnalyzer
        Returns:
            ValidationResult
        Raises:
            TokenOriginRelationValidatorException
            TokenAlreadyAtOriginException
            PartialTokenOriginRelationException
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
            candidate_primary=origin,
            candidate_satellite=token,
            token_validator=token_validator,
            square_validator=square_validator,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_analysis.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenOriginRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginRelationValidatorException.MSG,
                    err_code=TokenOriginRelationValidatorException.ERR_CODE,
                    ex=relation_analysis.exception,
                )
            )
        # Handle the case that, the token and the origin aren't fully bidirectional.
        relation = cast(RelationReport, relation_analysis.payload)
        if not relation.fully_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenOriginRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginRelationValidatorException.MSG,
                    err_code=TokenOriginRelationValidatorException.ERR_CODE,
                    ex=TokenOriginRelationNullException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenOriginRelationNullException.MSG,
                        err_code=TokenOriginRelationNullException.ERR_CODE,
                    ),
                )
            )
        # --- The token is at the origin. Forward the work product to the caller. ---#
        return ValidationResult.success(origin)