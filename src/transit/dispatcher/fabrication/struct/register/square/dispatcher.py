# src/transit/dispatcher/fabrication/struct/register/square/dispatcher.py

"""
Module: transit.dispatcher.fabrication.register.square.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from fabrication import SquareRegisterBuilder
from err import SquareRegisterBuildDispatcherException
from domain.struct.register import SquareRegister
from artifcat import BuildResult
from transit import SquareRegisterCarrier
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import RegisterBuildDispatcher


class SquareRegisterBuildDispatcher(RegisterBuildDispatcher[SquareRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a SquareRegister instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: SquareRegisterBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{SquareRegister]

    Super Class:
        RegisterBuilder
    """
    
    def __init__(
            self,
            builder: SquareRegisterBuilder | None = SquareRegisterBuilder(),
    ):
        super().__init__(builder=builder or SquareRegisterBuilder())
        
    @property
    def builder(self) -> SquareRegisterBuilder:
        return cast(SquareRegisterBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[SquareRegisterCarrier]:
        """
        Verify the object is a SquareRegister that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a SquareRegister and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[SquareRegister]
        Raises:
             SquareRegisterBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareRegisterBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterBuildDispatcherException.MSG,
                    err_code=SquareRegisterBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(SquareRegisterCarrier, build.authorization_applicant)
        )