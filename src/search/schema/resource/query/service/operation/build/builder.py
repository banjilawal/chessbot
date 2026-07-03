# src/logic/schema/database/search/context/service/operation/build/builder.py

"""
Module: logic.schema.database.search.context.service.operation.build.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from typing import Type

from system import Builder, LoggingLevelRouter, BuildResult
from model.catalog import (
    Schema, SchemaContext, SchemaQuery, SchemaQueryBuilderException, SchemaQueryIntegrityWorkers
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
            context: SchemaContext,
            schema: Schema = Type[Schema],
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
            SchemaQueryBuilderException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the schema is not safe to use.
        schema_validation_result = workers.schema_validator.execute(schema)
        if schema_validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SchemaQueryBuilderException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=SchemaQueryBuilderException.OP,
                    msg=SchemaQueryBuilderException.MSG,
                    err_code=SchemaQueryBuilderException.ERR_CODE,
                    mthd_rslt_type=SchemaQueryBuilderException.MTHD_RSLT,
                    ex=schema_validation_result.exception,
                )
            )
        
        # Handle the case that, the context is not safe to use.
        context_validation_result = workers.context_validator.execute(context)
        if context_validation_result.is_failure:
            # Send the exception chain on failure.
            # Send the exception chain on failure.
            return BuildResult.failure(
                SchemaQueryBuilderException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    op=SchemaQueryBuilderException.OP,
                    msg=SchemaQueryBuilderException.MSG,
                    err_code=SchemaQueryBuilderException.ERR_CODE,
                    mthd_rslt_type=SchemaQueryBuilderException.MTHD_RSLT,
                    ex=context_validation_result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult(SchemaQuery(catalog=schema, context=context))