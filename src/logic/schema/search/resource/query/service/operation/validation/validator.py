# src/logic/schema/database/search/context/service/operation/validation/validator.py

"""
Module: logic.schema.database.search.context.service.operation.validation.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, List, cast

from logic.system import LoggingLevelRouter, ValidationResult, Validator
from logic.schema import (
    Schema, SchemaContextValidator, SchemaQueryValidator, SchemaQueryNullException, SchemaQueryStackEmptyException,
    SchemaStackNullException, SchemaQuery, SchemaQueryValidationException, SchemaValidator
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
        -   def validate(
                    candidate: Any,
                    schema_validator: SchemaValidator,
                    context_validator: SchemaContextValidator,
            ) -> ValidationResult[SchemaQuery]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            schema_validator: SchemaValidator = SchemaValidator(),
            context_validator: SchemaContextValidator = SchemaQueryValidator(),
    ) -> ValidationResult[SchemaQuery]:
        """
        Certify a candidate is a SchemaQuery that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if either:
                    -   The schema
                    -   The context
                fail a validation check.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            schema_validator: SchemaValidator
            context_validator: SchemaContextValidator
        Returns:
            ValidationResult[SchemaQuery]
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
                    ),
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
                    ),
                )
            )
        # --- Cast the candidate to SchemaQuery for additional tests. ---#
        query = cast(SchemaQuery, candidate)
        
        # Handle the case that, the context is not certified as safe.
        context_validation_result = context_validator.validate(query.context)
        if context_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=context_validation_result.exception,
                )
            )
        # Handle the case that, the schema is not certified as safe.
        schema_validation_result = schema_validator.validate(query.catalog)
        if schema_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    rslt_type=SchemaQueryValidationException.RSLT_TYPE,
                    ex=schema_validation_result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
