# src/transit/dispatcher/fabrication/struct/register/square/validator.py

"""
Module: transit.dispatcher.fabrication.register.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import SquareRegisterValidator
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
        validator: SquareRegisterValidator

    Provides:
        -   def execute(candidate: Any) -> BuildResult{SquareRegister]

    Super Class:
        RegisterValidator
    """
    
    def __init__(
            self,
            validator: SquareRegisterValidator | None = SquareRegisterValidator(),
    ):
        super().__init__(validator=validator or SquareRegisterValidator())
        
    @property
    def validator(self) -> SquareRegisterValidator:
        return cast(SquareRegisterValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[SquareRegisterCarrier]:
        """
        Verify the object is a SquareRegister that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                validator test..
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
        build = self.validator.execute(job)
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
            cast(SquareRegisterCarrier, build.payload)
        )