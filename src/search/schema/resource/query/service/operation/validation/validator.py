# src/logic/schema/database/search/context/service/operation/validation/validator.py

"""
Module: logic.schema.database.search.context.service.operation.validation.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from typing import Any, cast

from system import LoggingLevelRouter, ValidationResult, Validator
from model.catalog import (
    SchemaQuery, SchemaQueryIntegrityWorkers, SchemaQueryNullException, SchemaQueryValidationException
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
                rank: Any
                workers: SchemaQueryIntegrityWorkers
            ) -> ValidationResult[SchemaQuery]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            workers: SchemaQueryIntegrityWorkers = SchemaQueryIntegrityWorkers(),
    ) -> ValidationResult[SchemaQuery]:
        """
        Certify a rank is a SchemaQuery that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if either:
                    -   The rank is null.
                    -   The rank is not a SchemaQuery.
                    -   Any integrity worker raises a failed test.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            workers: SchemaQueryIntegrityWorkers
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
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaQueryValidationException.MTHD_RSLT,
                    ex=SchemaQueryNullException(
                        SchemaQueryNullException.MSG,
                        SchemaQueryNullException.ERR_CODE,
                    ),
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SchemaQuery):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaQueryValidationException.MTHD_RSLT,
                    ex=TypeError(
                        f"Expected SchemaQuery, got {type(candidate).__name__} instead."
                    ),
                )
            )
        # --- Cast the candidate into SchemaQuery for additional tests. ---#
        query = cast(SchemaQuery, candidate)
        
        # Handle the case that, the context is not safe to use.
        context_validation_result = workers.context_validator.build(query.context)
        if context_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaQueryValidationException.MTHD_RSLT,
                    ex=context_validation_result.exception,
                )
            )
        # Handle the case that, the schema is not safe to use.
        schema_validation_result = workers.schema_validator.build(query.catalog)
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=SchemaQueryValidationException.OP,
                    msg=SchemaQueryValidationException.MSG,
                    err_code=SchemaQueryValidationException.ERR_CODE,
                    mthd_rslt_type=SchemaQueryValidationException.MTHD_RSLT,
                    ex=schema_validation_result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
