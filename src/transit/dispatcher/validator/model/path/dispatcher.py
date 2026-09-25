# src/transit/dispatcher/validator/model/path/validator.py

"""
Module: transit.dispatcher.validator.model.path.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import PathValidator
from artifcat import ValidationResult
from domain import Path
from err import PathValidationDispatcherException
from transit import ModelValidationDispatcher, PathCarrier
from util import LoggingLevelRouter


class PathValidationDispatcher(ModelValidationDispatcher[Path]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the PathValidation workflow.

    Attributes:
        validator: PathValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: PathValidator | None = None,
    ):
        super().__init__(validator=validator or PathValidator())
        
    @property
    def validator(self) -> PathValidator:
        return cast(PathValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[PathCarrier]:
        """
        Forward a job to a PathValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a PathCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[PathCarrier]
        Raises:
             PathValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PathValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathValidationDispatcherException.MSG,
                    err_code=PathValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(PathCarrier, validation.payload)
        return ValidationResult.success(carrier)