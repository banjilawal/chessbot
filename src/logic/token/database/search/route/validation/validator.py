# src/logic/token/database/search/route/validator/validator.py
"""
Module: logic.token.database.search.route.validator.validator
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.system import LoggingLevelRouter,  ValidationResult
from logic.token import (
    Token, TokenContext, TokenContextValidator, TokenDatasetNullException, TokenQueryParamsValidationException
)


class TokenQueryParamsValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Process Runner

    Responsibilities:
        1.  Validate inputs passed to a TokenSearchRouter.

    Attributes:

    Provides:
        -   validate(
                    dataset: List[Token],
                    context: TokenContext,
                    context_validator: TokenContextValidator,
            ) -> ValidationResult[int]

    Super Class:
    """
 
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            dataset: List[Token],
            context: TokenContext,
            context_validator: TokenContextValidator = TokenContextValidator(),
    ) -> ValidationResult[int]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                conditions occur:
                    -   The context fails a safety check.
                    -   The dataset is null.
                    -   The dataset's type is not ist[Token]
            2.  Otherwise, send the success result.
        Args:
            dataset: List[Token]
            context: TokenContext
            context_validator: TokenContextValidator
        Returns:
            ValidationResult[int]
        Raises:
            TypeError
            TokenDatasetNullException
            TokenQueryParamsValidationException
        """
        method = f"{cls.__name__}._validate"
        
        # Handle the case that, the context is not certified as safe.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryParamsValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryParamsValidationException.MSG,
                    err_code=TokenQueryParamsValidationException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the dataset does not exist
        if dataset is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryParamsValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryParamsValidationException.MSG,
                    err_code=TokenQueryParamsValidationException.ERR_CODE,
                    ex=TokenDatasetNullException(
                        msg=TokenDatasetNullException.MSG,
                        err_code=TokenDatasetNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the dataset is the wrong type.
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryParamsValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryParamsValidationException.MSG,
                    err_code=TokenQueryParamsValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected List, got {type(dataset).__name__} instead."
                    )
                )
            )
        # Handle the case that, the does not contain tokens.
        if not isinstance(dataset[0], Token):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryParamsValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryParamsValidationException.MSG,
                    err_code=TokenQueryParamsValidationException.ERR_CODE,
                    ex=TypeError(
                        f"List contains {type(dataset).__name__}  instead of tokens."
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(2)
    
    