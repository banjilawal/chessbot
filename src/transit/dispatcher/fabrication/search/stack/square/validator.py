# src/transit/dispatcher/fabrication/search/stack/square/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.stack.square.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from fabrication import StackContextBuilder, SquareContextBuilder
from domain import SquareSearchContext
from err import SquareContextBuilderException
from util import LoggingLevelRouter


class SquareContextBuilder(StackContextBuilder[SquareSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareContext instance is safe before use.

    Attributes:
        builder: SquareContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[SquareContext]

    Super Class:
        ContextBuilder
    """
    
    def __init__(self, builder: SquareContextBuilder):
        """
        Args:
            builder: SquareContextChecker
        """
        super().__init__(builder=builder)
    
    
    @property
    def builder(self) -> SquareContextBuilder:
        return cast(SquareContextBuilder, super().builder)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[SquareSearchContext]:
        """
        Certify a candidate is a SquareContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if builder
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[SquareContext]
        Raises:
            SquareContextBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that builder flags the candidate.
        build = self.builder.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareContextBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextBuilderException.MSG,
                    err_code=SquareContextBuilderException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(SquareSearchContext, build.payload)
        return BuildResult.success(context)

        
    
