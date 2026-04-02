# src/logic/schema/database/search/query/service/operation/build/builder.py

"""
Module: logic.schema.database.search.query.service.operation.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import List


from logic.system import BuildResult, Builder, LoggingLevelRouter, ValidationResult
from logic.schema import (
    Schema, SchemaContext, SchemaContextValidator, SchemaQueryBuildException, SchemaStackNullException, SchemaQuery,
)


class SchemaQueryBuilder(Builder[SchemaQuery]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Process Runner

    Responsibilities:
        1.  Validate inputs passed to a SchemaSearchRouter.

    Attributes:

    Provides:
        -   validate(
                    stack: List[Schema],
                    context: SchemaContext,
                    context_validator: SchemaContextValidator,
            ) -> ValidationResult[int]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            stack: List[Schema],
            context: SchemaContext,
            context_validator: SchemaContextValidator = SchemaContextValidator(),
    ) -> BuildResult[SchemaQuery]:
        """
        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                conditions occur:
                    -   The context fails a safety check.
                    -   The stack is null.
                    -   The stack's type is not ist[Schema]
            2.  Otherwise, send the success result.
        Args:
            stack: List[Schema]
            context: SchemaContext
            context_validator: SchemaContextValidator
        Returns:
            ValidationResult[int]
        Raises:
            TypeError
            SchemaStackNullException
            SchemaQueryBuildException
        """
        method = f"{cls.__name__}._validate"
        
        # Handle the case that, the context is not certified as safe.
        validation_result = context_validator.validate(context)
        if validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=SchemaQueryBuildException.MSG,
                    err_code=SchemaQueryBuildException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # Handle the case that, the stack does not exist
        if stack is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=SchemaQueryBuildException.MSG,
                    err_code=SchemaQueryBuildException.ERR_CODE,
                    ex=SchemaStackNullException(
                        msg=SchemaStackNullException.MSG,
                        err_code=SchemaStackNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the stack is the wrong type.
        if not isinstance(stack, List):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=SchemaQueryBuildException.MSG,
                    err_code=SchemaQueryBuildException.ERR_CODE,
                    ex=TypeError(
                        f"Expected List, got {type(stack).__name__} instead."
                    )
                )
            )
        # Handle the case that, the does not contain schemas.
        if not isinstance(stack[0], Schema):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SchemaQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    msg=SchemaQueryBuildException.MSG,
                    err_code=SchemaQueryBuildException.ERR_CODE,
                    ex=TypeError(
                        f"List contains {type(stack).__name__}  instead of schemas."
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult(SchemaQuery(stack=stack, context=context))