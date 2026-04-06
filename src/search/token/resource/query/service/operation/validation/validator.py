# src/logic/token/database/search/context/service/operation/validation/validator.py

"""
Module: logic.token.database.search.context.service.operation.validation.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, List, cast

from system import LoggingLevelRouter, ValidationResult, Validator
from model.token import (
    Token, TokenContextValidator, TokenQueryNullException, TokenQueryStackEmptyException,
    TokenStackNullException, TokenQuery, TokenQueryValidationException
)


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
            context_validator: TokenContextValidator = TokenContextValidator(),
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
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=TokenQueryNullException(
                        TokenQueryNullException.MSG,
                        TokenQueryNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, TokenQuery):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected TokenQuery, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the rank to TokenQuery for additional tests. ---#
        query = cast(TokenQuery, candidate)
        
        # Handle the case that, the context is not safe to use.
        validation_result = context_validator.validate(query.context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the schema does not exist
        if query.stack is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=TokenStackNullException(
                        msg=TokenStackNullException.MSG,
                        err_code=TokenStackNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the schema is the wrong type.
        if not isinstance(query.stack, List):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected List, got {type(query.stack).__name__} instead."
                    )
                )
            )
        # Handle the case that, list is empty.
        if len(query.stack) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=TokenQueryStackEmptyException(
                        msg=TokenQueryStackEmptyException.MSG,
                        err_code=TokenQueryStackEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, list contains something different from tokens.
        if not isinstance(query.stack[0], Token):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=TokenQueryValidationException.OP,
                    msg=TokenQueryValidationException.MSG,
                    err_code=TokenQueryValidationException.ERR_CODE,
                    rslt_type=TokenQueryValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"List contains {type(query.stack).__name__}  instead of tokens."
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
