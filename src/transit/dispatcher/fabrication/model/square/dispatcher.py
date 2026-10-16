# src/transit/dispatcher/fabrication/model/square/validator.py

"""
Module: transit.dispatcher.fabrication.model.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import SquareValidator
from artifcat import BuildResult
from domain import Square
from err import SquareBuildDispatcherException
from transit import ModelBuildDispatcher, SquareCarrier
from util import LoggingLevelRouter


class SquareBuildDispatcher(ModelBuildDispatcher[Square]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the SquareBuild workflow.

    Attributes:
        validator: SquareValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: SquareValidator | None = None,
    ):
        super().__init__(validator=validator or SquareValidator())
        
    @property
    def validator(self) -> SquareValidator:
        return cast(SquareValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[SquareCarrier]:
        """
        Forward a job to a SquareValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a SquareCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[SquareCarrier]
        Raises:
             SquareBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildDispatcherException.MSG,
                    err_code=SquareBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(SquareCarrier, build.payload)
        return BuildResult.success(carrier)