# src/logic/token/database/search/context/service/operation/build/builder.py

"""
Module: logic.token.database.search.context.service.operation.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List


from logic.system import BuildResult, Builder, LoggingLevelRouter, ValidationResult
from model.token import (
    Token, TokenContext, TokenContextValidator, TokenQueryBuildException, TokenStackNullException, TokenQuery,
)


class TokenQueryBuilder(Builder[TokenQuery]):
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
                    schema: List[Token],
                    context: TokenContext,
                    context_validator: TokenContextValidator,
            ) -> ValidationResult[int]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            stack: List[Token],
            context: TokenContext,
            context_validator: TokenContextValidator = TokenContextValidator(),
    ) -> BuildResult[TokenQuery]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                conditions occur:
                    -   The context fails a safety check.
                    -   The schema is null.
                    -   The schema's type is not ist[Token]
            2.  Otherwise, send the success result.
        Args:
            stack: List[Token]
            context: TokenContext
            context_validator: TokenContextValidator
        Returns:
            ValidationResult[int]
        Raises:
            TypeError
            TokenStackNullException
            TokenQueryBuildException
        """
        method = f"{cls.__name__}._validate"
        
        # Handle the case that, the context is not safe to use.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryBuildException.MSG,
                    err_code=TokenQueryBuildException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the schema does not exist
        if stack is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryBuildException.MSG,
                    err_code=TokenQueryBuildException.ERR_CODE,
                    ex=TokenStackNullException(
                        msg=TokenStackNullException.MSG,
                        err_code=TokenStackNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the schema is the wrong type.
        if not isinstance(stack, List):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryBuildException.MSG,
                    err_code=TokenQueryBuildException.ERR_CODE,
                    ex=TypeError(
                        f"Expected List, got {type(stack).__name__} instead."
                    )
                )
            )
        # Handle the case that, the does not contain tokens.
        if not isinstance(stack[0], Token):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=TokenQueryBuildException.MSG,
                    err_code=TokenQueryBuildException.ERR_CODE,
                    ex=TypeError(
                        f"List contains {type(stack).__name__}  instead of tokens."
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult(TokenQuery(stack=stack, context=context))