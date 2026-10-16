# src/transit/dispatcher/fabrication/search/stack/coord/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.stack.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import BuildResult
from fabrication import StackContextBuilder, CoordContextBuilder
from domain import CoordSearchContext
from err import CoordContextBuilderException
from util import LoggingLevelRouter


class CoordContextBuilder(StackContextBuilder[CoordSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordContext instance is safe before use.

    Attributes:
        builder: CoordContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[CoordContext]

    Super Class:
        ContextBuilder
    """
    
    def __init__(self, builder: Optional[CoordContextBuilder] | None = None):
        """
        Args:
            builder: Optional[CoordContextChecker]
        """
        super().__init__(builder=builder or CoordContextBuilder)
    
    
    @property
    def builder(self) -> CoordContextBuilder:
        return cast(CoordContextBuilder, super().builder)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[CoordSearchContext]:
        """
        Certify a candidate is a CoordContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if builder
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[CoordContext]
        Raises:
            CoordContextBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that builder flags the candidate.
        build = self.builder.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CoordContextBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextBuilderException.MSG,
                    err_code=CoordContextBuilderException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(CoordSearchContext, build.payload)
        return BuildResult.success(context)

        



