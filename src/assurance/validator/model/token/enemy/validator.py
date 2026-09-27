# src/assurance/validator/model/token/enemy/validator.py

"""
Module: assurance.validator.model.token.enemy.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Token
from err import TokenEnemyValidatorException
from exchange import TokenValidationRequest, TokenValidationResponseWrapper
from util import LoggingLevelRouter


class TokenEnemyValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenBlueprint enemy and previous_enemys fields
            are safe to use.

    Attributes:
        response_wrapper: TokenValidationResponseWrapper

    Provides:
        -   def execute(
                    request: TokenValidationRequest
            ) -> ValidationResult[Token]:

    Super Class:
    """
    _response_wrapper: TokenValidationResponseWrapper
    
    def __init__(
            self,
            response_wrapper: Optional[TokenValidationResponseWrapper]
                              | None = None,
    ):
        """
        Args:
            response_wrapper: Optional[TokenValidationResponseWrapper]
        """
        self._response_wrapper = (
                response_wrapper or TokenValidationResponseWrapper()
        )

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TokenValidationRequest,
    ) -> ValidationResult[Token]:
        """
        Run a safety check on an enemy.

        Action:
            1.  Send an exception chain in the ValidationResult if
                the responder fails.
            2.  Otherwise, send the validated enemy in the
                success result.
        Args:
            request: TokenValidationRequest
        Returns:
            ValidationResult[Token]
        Raises:
            TokenEnemyValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the response is an unsafe Toke.
        result = self._response_wrapper.extract_model(
            request=request,
        )
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenEnemyValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenEnemyValidatorException.MSG,
                    err_code=TokenEnemyValidatorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product. ---#
        token = cast(Token, result.payload)
        return ValidationResult.success(token)
    