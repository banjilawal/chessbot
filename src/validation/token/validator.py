# src/validation/token/validator.py

"""
Module: validation.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from blueprint import TokenBlueprint
from err import TokenValidatorException
from model import Token
from result import ValidationResult
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validation import TokenBlueprintValidator, Validator


class TokenValidator(Validator[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                candidate: Any, toolkit: TokenToolkit) -> ValidationResult[Token]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "token_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: TokenToolkit | None = None,
            blueprint_validator: TokenBlueprintValidator | None = None,
    ) -> ValidationResult[Token]:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not a number.
                    _   A Team check fails
                    -   A Rank check fails
                    -   Identity check fails
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: TokenToolkit
            blueprint_validator: TokenBlueprintValidator
        Returns:
            ValidationResult[Token]
        Raises:
             TokenValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenToolkit()
        if blueprint_validator is None:
            blueprint_validator = TokenBlueprintValidator()
        
        # Handle the case that, the candidate fails an initial check.
        priming_validation_result = toolkit.priming_validator.validate(
            candidate=candidate,
            target_model=toolkit.model,
            null_exception=toolkit.null_exception,
        )
        if priming_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=priming_validation_result.exception,
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        token = cast(Token, candidate)
        blueprint = TokenBlueprint(
            id=token.id,
            team=token.team,
            rank=token.rank,
            formation=token.formation,
            home_square=token.home_square,
            null_exception=toolkit.null_exception,
        )
        
        blueprint_validation_result = blueprint_validator.validate(
            candidate=blueprint,
            toolkit=toolkit,
        )
        # Handle the case that the, blueprint is flagged.
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        ## Since the blueprint is valid by the transitive property the token is valid.

        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(token)