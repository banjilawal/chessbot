# src/transit/dispatcher/fabrication/model/token/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.token.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import TokenBuilder
from artifcat import BuildResult
from domain import Token
from err import TokenBuildDispatcherException
from transit import ModelBuildDispatcher, TokenCarrier
from util import LoggingLevelRouter


class TokenBuildDispatcher(ModelBuildDispatcher[Token]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the TokenBuild workflow.

    Attributes:
        builder: TokenBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: TokenBuilder | None = None,
    ):
        super().__init__(builder=builder or TokenBuilder())
        
    @property
    def builder(self) -> TokenBuilder:
        return cast(TokenBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[TokenCarrier]:
        """
        Forward a job to a TokenBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a TokenCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[TokenCarrier]
        Raises:
             TokenBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildDispatcherException.MSG,
                    err_code=TokenBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(TokenCarrier, build.payload)
        return BuildResult.success(carrier)