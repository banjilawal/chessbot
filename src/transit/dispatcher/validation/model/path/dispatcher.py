# src/transit/dispatcher/validator/model/path/dispatcher.py

"""
Module: transit.dispatcher.validator.model.path.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import PathValidator
from artifcat import ValidationResult
from domain import Path
from err import PathValidationDispatcherException
from transit import ValidationDispatcher, PathCarrier
from util import LoggingLevelRouter


class PathValidationDispatcher(ValidationDispatcher[Path]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Path validation jobs among workers, then forward their results.

    Attributes:
        validator: PathValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[PathValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[PathValidator]
        """
        super().__init__(validator=validator or PathValidator())
        
    @property
    def validator(self) -> PathValidator:
        return cast(PathValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[PathCarrier]:
        """
        Send jobs to a PathValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
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
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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