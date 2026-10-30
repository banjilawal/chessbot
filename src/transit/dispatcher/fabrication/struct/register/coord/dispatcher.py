# src/transit/dispatcher/fabrication/struct/register/coord/dispatcher.py

"""
Module: transit.dispatcher.fabrication.register.coord.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from fabrication import CoordRegisterBuilder
from err import CoordRegisterBuildDispatcherException
from domain.struct.register import CoordRegister
from artifcat import BuildResult
from transit import CoordRegisterCarrier
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import RegisterBuildDispatcher


class CoordRegisterBuildDispatcher(RegisterBuildDispatcher[CoordRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordRegister instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: CoordRegisterBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{CoordRegister]

    Super Class:
        RegisterBuilder
    """
    
    def __init__(
            self,
            builder: CoordRegisterBuilder | None = CoordRegisterBuilder(),
    ):
        super().__init__(builder=builder or CoordRegisterBuilder())
        
    @property
    def builder(self) -> CoordRegisterBuilder:
        return cast(CoordRegisterBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[CoordRegisterCarrier]:
        """
        Verify the object is a CoordRegister that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a CoordRegister and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[CoordRegister]
        Raises:
             CoordRegisterBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CoordRegisterBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterBuildDispatcherException.MSG,
                    err_code=CoordRegisterBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(CoordRegisterCarrier, build.authorization_applicant)
        )