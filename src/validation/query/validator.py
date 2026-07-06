# src/validation/query/token/validator.py

"""
Module: validation.query.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from blueprint import QueryValidationBlueprint
from err import QueryValidationException
from model import CatalogQuery, Query, StackQuery
from result import ValidationResult
from util import LoggingLevelRouter
from validation import Validator


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
    def execute(
            cls,
            candidate: Any,
            blueprint: QueryValidationBlueprint,
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
            candidate: Any
            blueprint: QueryValidationBlueprint
        Returns:
            ValidationResult[Query]
        Raises:
            QueryValidationException
            ListEmptyException
        """
        method = f"{cls.__name__}._validate"
        
        priming_result = blueprint.priming_validator.execute(
            candidate=candidate,
            context_model=blueprint.query_model_type,
            null_exception=blueprint.query_null_exception,
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into Query for additional tests. ---#
        query = cast(blueprint.query_model_type, candidate)
        
        # Handle the case that, the
        datasource_validation_result = cls._datasource_validator(
            query=query,
            blueprint=blueprint
        )
        if datasource_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=datasource_validation_result.exception,
                )
            )
        # Handle the case that, the context is flagged.
        context_validation_result = blueprint.context_validator.execute(query.context)
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
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _datasource_validator(
            cls,
            query: Query,
            blueprint: QueryValidationBlueprint
    ) -> ValidationResult[Query]:
        method = f"{cls.__name__}._datasource_validator"
        
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
            blueprint: QueryValidationBlueprint
    ) -> ValidationResult[StackQuery]:
        method = f"{cls.__name__}._stack_query_validator"
        
        # Handle the case that, the stack is flagged.
        stack_validation_result = blueprint.priming_validator.execute(
            candidate=query.stack,
            context_model=blueprint.stack_model_type,
            null_exception=blueprint.stack_null_exception,
        )
        if stack_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=stack_validation_result.exception
                )
            )
        # Handle the case that, stack is empty.
        if query.stack.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=blueprint.empty_stack_exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _catalog_query_validator(
            cls,
            query: CatalogQuery,
            blueprint: QueryValidationBlueprint
    ) -> ValidationResult[CatalogQuery]:
        method = f"{cls.__name__}._stack_query_validator"
        
        catalog_validation_result = blueprint.priming_validator.execute(
            candidate=query.catalog,
            context_model=blueprint.stack_model_type,
            null_exception=blueprint.stack_null_exception,
        )
        if catalog_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueryValidationException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=QueryValidationException.MSG,
                    err_code=QueryValidationException.ERR_CODE,
                    ex=catalog_validation_result.exception
                )
            )
        # --- Forward the work product to the client. ---#
        return ValidationResult.success(query)
        
    
