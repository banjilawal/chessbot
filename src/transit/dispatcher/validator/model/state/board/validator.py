# src/transit/dispatcher/validator/model/state/board/validator.py

"""
Module: transit.dispatcher.validator.model.state.board.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import BoardValidatorException
from domain.model import Board
from assurance import BoardIntegrityChecker
from artifcat import ValidationResult
from util import LoggingLevelRouter
from transit.dispatcher.validator import ModelValidationDispatcher


class BoardValidationDispatcher(ModelValidationDispatcher[Board]):
    """
    Role
        -  Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Board instance is certified safe, reliable and consistent before use.

    Attributes:
        integrity_checker: BoardIntegrityChecker

    Provides:
        -  execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            integrity_checker: BoardIntegrityChecker | None = BoardIntegrityChecker(),
    ):
        super().__init__(integrity_checker=integrity_checker)
        
    @property
    def integrity_checker(self) -> BoardIntegrityChecker:
        return cast(BoardIntegrityChecker, super().integrity_checker)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Board that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                integrity_checker test..
            2.  Otherwise, cast the payload into a Board and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Board]
        Raises:
             BoardValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.integrity_checker.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidatorException.MSG,
                    err_code=BoardValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.integrity_checker.bundle.model,
                certification.payload
            )
        )