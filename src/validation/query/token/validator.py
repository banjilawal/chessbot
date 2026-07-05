# src/validation/query/token/validator.py

"""
Module: validation.query.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, List, cast

from err import (
    TokenQueryNullException, TokenQueryStackEmptyException, TokenQueryValidationException,
    TokenStackNullException
)
from model import Token, TokenQuery
from result import MethodResultType, ValidationResult
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import TokenContextValidator, PrimingValidator, Validator


class TokenQueryValidator(Validator[TokenQuery]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TokenQuery instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   validate(
                    rank: Any
                    context_validator: TokenContextValidator,
            ) -> ValidationResult[int]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            priming_validator: PrimingValidator | None = None,
            context_validator: TokenContextValidator | None = None,
    ) -> ValidationResult[TokenQuery]:
        """
        Certify a rank is a TokenQuery that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                conditions occur:
                    -   The rank is null
                    -   The rank is not a TokenQuery
                    -   The context fails a safety check.
                    -   The schema is null.
                    -   The schema's type is not ist[Token]
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            context_validator: TokenContextValidator
        Returns:
            ValidationResult[int]
        Raises:
            TypeError
            TokenStackNullException
            TokenQueryValidationException
            TokenQueryStackEmptyException
        """
        method = f"{cls.__name__}._validate"
        
        if priming_validator is None:
            priming_validator = PrimingValidator()
        if context_validator is None:
            context_validator = TokenContextValidator()
        
        validator_priming_result = priming_validator.validate(
            candidate=candidate,
            target_model=TokenQuery,
            null_exception=TokenQueryNullException(),
        )
        # Handle the nonexistence case.
        if validator_priming_result.failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into TokenQuery for additional tests. ---#
        query = cast(TokenQuery, candidate)
        
        # Handle the case that, the context is not safe to use.
        context_validation_result = context_validator.validate(query.context)
        if context_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=context_validation_result.exception
                )
            )
        stack_validation_result = validator_priming_result = priming_validator.validate(
            candidate=query.stack,
            target_model=TokenStackService,
            null_exception=TokenStackNullException(),
        )
        if stack_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=stack_validation_result.exception,
                )
            )
        # Handle the case that, list is empty.
        if query.stack.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=TokenQueryStackEmptyException(
                        msg=TokenQueryStackEmptyException.MSG,
                        err_code=TokenQueryStackEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
