# src/transit/dispatcher/validator/model/board/validator.py

"""
Module: transit.dispatcher.validator.model.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import BoardValidator
from artifcat import ValidationResult
from domain import Board
from err import BoardValidationDispatcherException
from transit import ModelValidationDispatcher, BoardCarrier
from util import LoggingLevelRouter


class BoardValidationDispatcher(ModelValidationDispatcher[Board]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the BoardValidation workflow.

    Attributes:
        validator: BoardValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: BoardValidator | None = None,
    ):
        super().__init__(validator=validator or BoardValidator())
        
    @property
    def validator(self) -> BoardValidator:
        return cast(BoardValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[BoardCarrier]:
        """
        Forward a job to a BoardValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a BoardCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[BoardCarrier]
        Raises:
             BoardValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationDispatcherException.MSG,
                    err_code=BoardValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(BoardCarrier, validation.payload)
        return ValidationResult.success(carrier)