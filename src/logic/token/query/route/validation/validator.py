# src/logic/token/query/route/validator/validator.py
"""
Module: logic.token.query.route.validator.validator
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from typing import List

from logic.system import LoggingLevelRouter, SearchResult, ValidationResult
from logic.token import (
    Token, TokenContext, TokenContextValidator, TokenDatasetNullException,  TokenQueryValidationException
)


class TokenQueryValidator:
    """
    Role:
        -   API
        -   Search Micro Validation,

    Responsibilities:
        1.  Public facing API for querying square collections.

    Args:
        id: int
        name: str
        router: SearchRouter[T]
        context_validation: IntegrityValidation[Context[T]]

    Provides:
        -   execute(dataset: List[T], query: Context[T]) -> SearchResult[List[T]]

    Super Class:
        Validation
    """
 
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            dataset: List[Token],
            context: TokenContext,
            context_validator: TokenContextValidator = TokenContextValidator(),
    ) -> ValidationResult[int]:
        method = f"{cls.__name__}._validate"
        
        # Handle the case that, the query is incorrect
        validation_result = context_validator.execute(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the dataset does not exist
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    ex=TokenDatasetNullException(
                        msg=TokenDatasetNullException.MSG,
                        err_code=TokenDatasetNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the dataset is the wrong type.
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected List, got {type(dataset).__name__} instead."
                    )
                )
            )
        # Handle the case that, the does not contain tokens.
        if not isinstance(dataset[0], Token):
            # Return the exception chain on failure.
            return SearchResult.failure(
                TokenQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    ex=TypeError(
                        f"List contains {type(dataset).__name__}  instead of tokens."
                    )
                )
            )
        return ValidationResult.success(2)
    
    