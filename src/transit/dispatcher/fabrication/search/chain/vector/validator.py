# src/transit/dispatcher/fabrication/search/chain/vector/dispatcher.py

"""
Module: transit.dispatcher.fabrication.search.chain.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from fabrication import ChainContextBuilder, VectorNodeContextBuilder
from domain import VectorNodeContext
from err import VectorNodeContextBuilderException

from util import LoggingLevelRouter


class VectorNodeContextBuilder(
    ChainContextBuilder[VectorNodeContext]
):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorNodeContext instance is safe before use.

    Attributes:
        builder: VectorNodeContextChecker

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[VectorNodeContext]

    Super Class:
        ContextBuilder
    """
    
    def __init__(self, builder: VectorNodeContextBuilder):
        """
        Args:
            builder: VectorNodeContextChecker
        """
        super().__init__(builder=builder)
    
    
    @property
    def builder(self) -> VectorNodeContextBuilder:
        return cast(VectorNodeContextBuilder, super().builder)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> BuildResult[VectorNodeContext]:
        """
        Certify a candidate is a VectorNodeContext that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if builder
                returns a failure.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            BuildResult[VectorNodeContext]
        Raises:
            VectorNodeContextBuilderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that builder flags the candidate.
        build = self.builder.execute(candidate=candidate)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorNodeContextBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeContextBuilderException.MSG,
                    err_code=VectorNodeContextBuilderException.ERR_CODE,
                    ex=build.exception
                )
            )
        # --- Otherwise, cast and forward the work product to the caller. ---#
        context = cast(VectorNodeContext, build.payload)
        return BuildResult.success(context)

        
    
