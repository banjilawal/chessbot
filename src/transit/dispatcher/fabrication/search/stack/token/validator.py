# src/transit/dispatcher/fabrication/search/stack/token/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.stack.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from fabrication import StackContextBuilder, TokenContextBuilder
from domain import TokenSearchContext
from err import TokenContextBuilderException
from util import LoggingLevelRouter


class TokenContextBuilder(StackContextBuilder[TokenSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenContext instance is safe before use.

    Attributes:
        builder: TokenContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[TokenContext]

    Super Class:
        ContextBuilder
    """
    
    def __init__(self, builder: TokenContextBuilder):
        """
        Args:
            builder: TokenContextChecker
        """
        super().__init__(builder=builder)
    
    
    @property
    def builder(self) -> TokenContextBuilder:
        return cast(TokenContextBuilder, super().builder)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[TokenSearchContext]:
        """
        Certify a candidate is a TokenContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if builder
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[TokenContext]
        Raises:
            TokenContextBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that builder flags the candidate.
        build = self.builder.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenContextBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextBuilderException.MSG,
                    err_code=TokenContextBuilderException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(TokenSearchContext, build.payload)
        return BuildResult.success(context)

        
    
