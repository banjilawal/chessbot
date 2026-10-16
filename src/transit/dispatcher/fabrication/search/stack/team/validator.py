# src/transit/dispatcher/fabrication/search/stack/team/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.stack.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from fabrication import StackContextBuilder, TeamContextBuilder
from domain import TeamSearchContext
from err import TeamContextBuilderException
from util import LoggingLevelRouter


class TeamContextBuilder(StackContextBuilder[TeamSearchContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamContext instance is safe before use.

    Attributes:
        builder: TeamContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[TeamContext]

    Super Class:
        ContextBuilder
    """
    
    def __init__(self, builder: TeamContextBuilder):
        """
        Args:
            builder: TeamContextChecker
        """
        super().__init__(builder=builder)
    
    @property
    def builder(self) -> TeamContextBuilder:
        return cast(TeamContextBuilder, super().builder)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[TeamSearchContext]:
        """
        Certify a candidate is a TeamContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if builder
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[TeamContext]
        Raises:
            TeamContextBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that builder flags the candidate.
        build = self.builder.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamContextBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamContextBuilderException.MSG,
                    err_code=TeamContextBuilderException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(TeamSearchContext, build.payload)
        return BuildResult.success(context)

