# src/transit/dispatcher/fabrication/struct/register/vector/dispatcher.py

"""
Module: transit.dispatcher.fabrication.register.vector.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import VectorRegisterBuildDispatcherException
from domain.struct.register import VectorRegister
from artifcat import BuildResult
from transit import VectorRegisterCarrier
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import RegisterBuildDispatcher


class VectorRegisterBuildDispatcher(RegisterBuildDispatcher[VectorRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a VectorRegister instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: VectorRegisterBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{VectorRegister]

    Super Class:
        RegisterBuilder
    """
    
    def __init__(
            self,
            builder: VectorRegisterBuilder | None = VectorRegisterBuilder(),
    ):
        super().__init__(builder=builder or VectorRegisterBuilder())
        
    @property
    def builder(self) -> VectorRegisterBuilder:
        return cast(VectorRegisterBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[VectorRegisterCarrier]:
        """
        Verify the object is a VectorRegister that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a VectorRegister and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[VectorRegister]
        Raises:
             VectorRegisterBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorRegisterBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterBuildDispatcherException.MSG,
                    err_code=VectorRegisterBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(VectorRegisterCarrier, build.authorization_applicant)
        )