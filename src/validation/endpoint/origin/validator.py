# src/validation/endpoint/origin/validator.py

"""
Module: validation.endpoint.origin.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from err import TokenOriginRelationNullException, TokenOriginRelationValidatorException
from model import Square, Token
from report import RelationReport
from result import ValidationResult
from toolkit import TokenEndpointRelationToolkit
from util import LoggingLevelRouter


class TokenOriginCertifier:
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
        -   def validate(
                    token: Token,
                    origin: Square,
                    toolkit: TokenEndpointRelationToolkit,
            ) -> ValidationResult[Square]:

    Super Class:
    """
    OPERATION_NAME = "token_origin_relation_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            token: Token,
            origin: Square,
            toolkit: TokenEndpointRelationToolkit | None = None,
    ) -> ValidationResult[Square]:
        """
        Makes sure a Maneuver's origin contains the right token.

        Action:
            1.  Send an exception chan in the validation result if any of the following occur.:
                    -   The relation analysis is not completed.
                    -   The relationship between the token and origin is not fully bidirectional.
            2.  Otherwise, send the success result.
        Args:
            token: Token
            origin: Square
            toolkit: TokenEndpointRelationToolkit
        Returns:
            ValidationResult
        Raises:
            TokenOriginRelationValidatorException
            TokenOriginRelationNullException
        """
        method = f"{cls.__name__}.validator"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenEndpointRelationToolkit
        
        # --- Run the relation analyzer. ---#
        relation_analysis_result = toolkit.relation_analyzer.analyze(
            candidate_primary=origin,
            candidate_satellite=token,
            token_validator=toolkit.token_validator,
            square_validator=toolkit.square_validator,
        )
        # Handle the case that, the relation_analysis is not completed.
        if relation_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenOriginRelationValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenOriginRelationValidatorException.MSG,
                    err_code=TokenOriginRelationValidatorException.ERR_CODE,
                    ex=relation_analysis_result.exception,
                )
            )
        # --- Extract the relation report for additional tests. ---#
        relation = cast(RelationReport, relation_analysis_result.payload)
        
        # Handle the case that, the token and the origin aren't fully bidirectional.
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