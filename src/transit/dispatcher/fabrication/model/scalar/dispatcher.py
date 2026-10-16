# src/transit/dispatcher/fabrication/model/scalar/validator.py

"""
Module: transit.dispatcher.fabrication.model.scalar.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import ScalarValidator
from artifcat import BuildResult
from domain import Scalar
from err import ScalarBuildDispatcherException
from transit import ModelBuildDispatcher, ScalarCarrier
from util import LoggingLevelRouter


class ScalarBuildDispatcher(ModelBuildDispatcher[Scalar]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ScalarBuild workflow.

    Attributes:
        validator: ScalarValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: ScalarValidator | None = None,
    ):
        super().__init__(validator=validator or ScalarValidator())
        
    @property
    def validator(self) -> ScalarValidator:
        return cast(ScalarValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ScalarCarrier]:
        """
        Forward a job to a ScalarValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ScalarCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[ScalarCarrier]
        Raises:
             ScalarBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildDispatcherException.MSG,
                    err_code=ScalarBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ScalarCarrier, build.payload)
        return BuildResult.success(carrier)