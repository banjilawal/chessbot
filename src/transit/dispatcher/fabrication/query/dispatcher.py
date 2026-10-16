# src/transit/dispatcher/fabrication/query/token/validator.py

"""
Module: transit.dispatcher.fabrication.query.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from domain.metadata.blueprint import QueryBuildBlueprint
from err import QueryValidatorException
from domain.model import CatalogQuery, Query, StackQuery
from artifcat import BuildResult
from util import LoggingLevelRouter
from transit import BuildDispatcher


class QueryBuildDispatcher(BuildDispatcher[Query]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Ensure a Query instance is certified safe, reliable, and consistent before use.

    Attributes:

    Provides:
        - validate(
                    rank: Any
                    context_validator: TokenContextValidator,
            ) -> BuildResult[int]

    Super Class:
    """
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            job: Any,
            blueprint: QueryBuildBlueprint,
    ) -> BuildResult[Query]:
        """
        Certify a rank is a Query that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                conditions occur:
                    - The rank is null
                    - The rank is not a Query
                    - The context fails a safety check.
                    - The schema is null.
                    - The schema's type is not ist[Token]
            2.  Otherwise, send the success result.
        Args:
            job: Any
            blueprint: QueryBuildBlueprint
        Returns:
            BuildResult[Query]
        Raises:
            QueryValidatorException
            ListEmptyException
        """
        method = f"{self.__class__.__name__}._validate"
        
        priming_result = blueprint.priming_validator.execute(
            job=job,
            target_model=blueprint.query_model_type,
            model_null_exception=blueprint.query_null_exception,
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QueryValidatorException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidatorException.MSG,
                    err_code=QueryValidatorException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into Query for additional tests. ---#
        query = cast(blueprint.query_model_type, job)
        
        # Handle the case that the
        datasource_build_result = cls._datasource_validator(
            query=query,
            blueprint=blueprint
        )
        if datasource_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QueryValidatorException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidatorException.MSG,
                    err_code=QueryValidatorException.ERR_CODE,
                    ex=datasource_build_result.exception,
                )
            )
        # Handle the case that the context is flagged.
        context_build_result = blueprint.context_validator.execute(query.context)
        if context_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QueryValidatorException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidatorException.MSG,
                    err_code=QueryValidatorException.ERR_CODE,
                    ex=context_build_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult.success(query)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _datasource_validator(
            cls,
            query: Query,
            blueprint: QueryBuildBlueprint
    ) -> BuildResult[Query]:
        method = f"{self.__class__.__name__}._datasource_validator"
        
        if isinstance(query, StackQuery):
            stack_query = cast(blueprint.query_model_type, query)
            return cls._stack_query_validator(query=stack_query, blueprint=blueprint)
        
        catalog_query = cast(blueprint.query_model_type, query)
        return cls._catalog_query_validator(query=catalog_query, blueprint=blueprint)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _stack_query_validator(
            cls,
            query: StackQuery,
            blueprint: QueryBuildBlueprint
    ) -> BuildResult[StackQuery]:
        method = f"{self.__class__.__name__}._stack_query_validator"
        
        # Handle the case that the stack is flagged.
        stack_build_result = blueprint.priming_validator.execute(
            job=query.stack,
            target_model=blueprint.stack_model_type,
            model_null_exception=blueprint.stack_null_exception,
        )
        if stack_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QueryValidatorException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidatorException.MSG,
                    err_code=QueryValidatorException.ERR_CODE,
                    ex=stack_build_result.exception
                )
            )
        # Handle the case that stack is empty.
        if query.stack.is_empty:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QueryValidatorException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidatorException.MSG,
                    err_code=QueryValidatorException.ERR_CODE,
                    ex=blueprint.empty_stack_exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult.success(query)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _catalog_query_validator(
            cls,
            query: CatalogQuery,
            blueprint: QueryBuildBlueprint
    ) -> BuildResult[CatalogQuery]:
        method = f"{self.__class__.__name__}._stack_query_validator"
        
        catalog_build_result = blueprint.priming_validator.execute(
            job=query.catalog,
            target_model=blueprint.stack_model_type,
            model_null_exception=blueprint.stack_null_exception,
        )
        if catalog_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QueryValidatorException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidatorException.MSG,
                    err_code=QueryValidatorException.ERR_CODE,
                    ex=catalog_build_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult.success(query)
        
    
