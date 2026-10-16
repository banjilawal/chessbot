# src/transit/dispatcher/fabrication/query/token/dispatcher.py

"""
Module: transit.dispatcher.fabrication.query.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import (
    TokenQueryNullException, TokenQueryStackEmptyException, TokenQueryBuilderException,
    TokenStackNullException
)
from domain.model import TokenQuery
from artifcat import MethodResultType, BuildResult
from collection.stack import TokenStackService
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import TokenContextBuilder, PrimingBuilder, BuildDispatcher


class TokenQueryBuildDispatcher(BuildDispatcher[TokenQuery]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Ensure a TokenQuery instance is certified safe, reliable, and consistent before use.

    Attributes:

    Provides:
        - validate(
                    rank: Any
                    context_builder: TokenContextBuilder,
            ) -> BuildResult[int]

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            job: Any,
            priming_builder: PrimingBuilder | None = None,
            context_builder: TokenContextBuilder | None = None,
    ) -> BuildResult[TokenQuery]:
        """
        Certify a rank is a TokenQuery that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                conditions occur:
                    - The rank is null
                    - The rank is not a TokenQuery
                    - The context fails a safety check.
                    - The schema is null.
                    - The schema's type is not ist[Token]
            2.  Otherwise, send the success result.
        Args:
            job: Any
            context_builder: TokenContextBuilder
        Returns:
            BuildResult[int]
        Raises:
            TypeError
            TokenStackNullException
            TokenQueryBuilderException
            TokenQueryStackEmptyException
        """
        method = f"{self.__class__.__name__}._validate"
        
        if priming_builder is None:
            priming_builder = PrimingBuilder()
        if context_builder is None:
            context_builder = TokenContextBuilder()
        
        builder_priming_result = priming_builder.execute(
            candidate=job,
            target_model=TokenQuery,
            null_exception=TokenQueryNullException(),
        )
        # Handle the nonexistence case.
        if builder_priming_result.failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenQueryBuilderException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryBuilderException.MSG,
                    err_code=TokenQueryBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=builder_priming_result.exception,
                )
            )
        # --- Cast the candidate into TokenQuery for additional tests. ---#
        query = cast(TokenQuery, job)
        
        # Handle the case that the context is not safe to use.
        context_build_result = context_builder.execute(query.context)
        if context_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenQueryBuilderException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryBuilderException.MSG,
                    err_code=TokenQueryBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=context_build_result.exception
                )
            )
        stack_build_result = builder_priming_result = priming_builder.execute(
            candidate=query.stack,
            target_model=TokenStackService,
            null_exception=TokenStackNullException(),
        )
        if stack_build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenQueryBuilderException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryBuilderException.MSG,
                    err_code=TokenQueryBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=stack_build_result.exception,
                )
            )
        # Handle the case that list is empty.
        if query.stack.is_empty:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenQueryBuilderException(
                    cls_mthd=method,
                    cls_name=method.__class__.__name__,
                    msg=TokenQueryBuilderException.MSG,
                    err_code=TokenQueryBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=TokenQueryStackEmptyException(
                        msg=TokenQueryStackEmptyException.MSG,
                        err_code=TokenQueryStackEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the client. ---#
        return BuildResult.success(query)
        
    
