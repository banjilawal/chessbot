# src/validation/query/token/validator.py

"""
Module: validation.query.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, List, cast

from err import ListNullException
from model import Query
from system import LoggingLevelRouter, ValidationResult, Validator
from model.token import (
    Token, TokenContextValidator, QueryNullException, ListEmptyException,
    TokenStackNullException, Query, QueryValidationException
)
from validation import ContextValidator, ValidationPrimer


class QueryValidator(Validator[Query]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Query instance is certified safe, reliable and consistent before use.

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
            query_model_type: Query,
            null_exception: QueryNullException,
            context_validator: ContextValidator,
            validation_primer: ValidationPrimer,
    ) -> ValidationResult[Query]:
        """
        Certify a rank is a Query that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                conditions occur:
                    -   The rank is null
                    -   The rank is not a Query
                    -   The context fails a safety check.
                    -   The schema is null.
                    -   The schema's type is not ist[Token]
            2.  Otherwise, send the success result.
        Args:
            query_model_type: Query,
            null_exception: QueryNullException,
            context_validator: ContextValidator,
            validation_primer: ValidationPrimer,
        Returns:
            ValidationResult[Query]
        Raises:
            QueryValidationException
            ListEmptyException
        """
        method = f"{cls.__name__}._validate"
        
        query_validation_result = validation_primer.validate(
            candidate=candidate,
            target_model=query_model_type,
            null_exception=null_exception,
        )
        if query_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=query_validation_result.exception
                )
            )
        # --- Cast the candidate into Query for additional tests. ---#
        query = cast(query_model_type, candidate)
        
        context_validation_result = context_validator.validate(query.context)
        if context_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=context_validation_result.exception
                )
            )
        list_validation_result = validation_primer.validate(
            candidate=query.items,
            target_model=List,
            null_exception=ListNullException(),
        )
        if list_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=list_validation_result.exception
                )
            )
        # Handle the case that, list is empty.
        if len(query.items) == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=QueryValidationException.OP,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=ListEmptyException(
                        msg=ListEmptyException.MSG,
                        err_code=ListEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
