# src/logic/schema/database/search/query/service/operation/validation/validator.py

"""
Module: logic.schema.database.search.query.service.operation.validation.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, List, cast

from logic.system import LoggingLevelRouter, ValidationResult, Validator
from logic.schema import (
    Schema, SchemaContextValidator, SchemaQueryNullException, SchemaQueryStackEmptyException,
    SchemaStackNullException, SchemaQuery, SchemaQueryValidationException
)


class SchemaQueryValidator(Validator[SchemaQuery]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SchemaQuery instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   validate(
                    candidate: Any
                    context_validator: SchemaContextValidator,
            ) -> ValidationResult[int]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            context_validator: SchemaContextValidator = SchemaContextValidator(),
    ) -> ValidationResult[SchemaQuery]:
        """
        Certify a candidate is a SchemaQuery that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                conditions occur:
                    -   The candidate is null
                    -   The candidate is not a SchemaQuery
                    -   The context fails a safety check.
                    -   The stack is null.
                    -   The stack's type is not ist[Schema]
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            context_validator: SchemaContextValidator
        Returns:
            ValidationResult[int]
        Raises:
            TypeError
            SchemaStackNullException
            SchemaQueryValidationException
            SchemaQueryStackEmptyException
        """
        method = f"{cls.__name__}._validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=SchemaQueryNullException(
                        SchemaQueryNullException.MSG,
                        SchemaQueryNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SchemaQuery):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected SchemaQuery, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to SchemaQuery for additional tests. ---#
        query = cast(SchemaQuery, candidate)
        
        # Handle the case that, the context is not certified as safe.
        validation_result = context_validator.validate(query.context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the stack does not exist
        if query.stack is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=SchemaStackNullException(
                        msg=SchemaStackNullException.MSG,
                        err_code=SchemaStackNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the stack is the wrong type.
        if not isinstance(query.stack, List):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected List, got {type(query.stack).__name__} instead."
                    )
                )
            )
        # Handle the case that, list is empty.
        if len(query.stack) == 0:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=SchemaQueryStackEmptyException(
                        msg=SchemaQueryStackEmptyException.MSG,
                        err_code=SchemaQueryStackEmptyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, list contains something different from schemas.
        if not isinstance(query.stack[0], Schema):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"List contains {type(query.stack).__name__}  instead of schemas."
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
