# src/logic/schema/database/search/context/service/operation/build/builder.py

"""
Module: logic.schema.database.search.context.service.operation.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from logic.system import Builder, LoggingLevelRouter, BuildResult
from logic.schema import (
    Schema, SchemaContext, SchemaContextValidator, SchemaQuery, SchemaQueryBuildException,
    SchemaQueryIntegrityWorkers, SchemaValidator
)


class SchemaQueryBuilder(Builder[SchemaQuery]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  SchemaQuery creation process owner.
        2.  Ensure SchemaQuery build resources meet satisfy contracts.
        3.  Guarantee new instances comply with business logic at birth.

    Attributes:

    Provides:
        -   def build(
                schema: Schema
                context: SchemaContext
                workers: SchemaQueryIntegrityWorkers
            ) -> BuildResult[SchemaContext]:

     Super Class:
         Builder
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            schema: Schema,
            context: SchemaContext,
            workers: SchemaQueryIntegrityWorkers = SchemaQueryIntegrityWorkers(),
    ) -> BuildResult[SchemaQuery]:
        """
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                conditions occur:
                    -   The schema fails a safety check.
                    -   The context fails a safety check
            2.  Otherwise, send the success result.
        Args:
            schema: Schema
            context: SchemaContext
            workers: SchemaQueryIntegrityWorkers
        Returns:
            BuildResult[SchemaQuery]
        Raises:
            TypeError
            SchemaStackNullException
            SchemaQueryBuildException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the schema is not certified as safe.
        schema_validation_result = workers.schema_validator.validate(schema)
        if schema_validation_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryBuildException.OP,
                    msg=SchemaQueryBuildException.MSG,
                    err_code=SchemaQueryBuildException.ERR_CODE,
                    rslt_type=SchemaQueryBuildException.RSLT_TYPE,
                    ex=schema_validation_result.exception,
                )
            )
        
        # Handle the case that, the context is not certified as safe.
        context_validation_result = workers.context_validator.validate(context)
        if context_validation_result.is_failure:
            # Return the exception chain on failure.
            # Return the exception chain on failure.
            return BuildResult.failure(
                SchemaQueryBuildException(
                    mthd=method,
                    title=cls.__class__.__name__,
                    op=SchemaQueryBuildException.OP,
                    msg=SchemaQueryBuildException.MSG,
                    err_code=SchemaQueryBuildException.ERR_CODE,
                    rslt_type=SchemaQueryBuildException.RSLT_TYPE,
                    ex=context_validation_result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult(SchemaQuery(catalog=schema, context=context))