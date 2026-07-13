# src/consistency/token/consistency.py

"""
Module: consistency.token.checker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from consistency import ConsistencyChecker
from err import TokenConsistencyCheckerException
from model import Token
from chooser import TokenCarrier
from result import ValidationResult
from setting.board.dimension.config import board_size
from toolkit import TokenToolkit
from util import LoggingLevelRouter


class TokenConsistencyChecker(ConsistencyChecker[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:
        priming_validator: PrimingValidator
    Provides:
        -    execute(dto_operand: TokenDtoOperand) -> ValidationResult

    Super Class:
        Consistency
    """
    _toolkit: TokenToolkit
    
    def __init__(self, toolkit: TokenToolkit | None = TokenToolkit()):
        super().__init__()
        self._toolkit = toolkit
    

    @LoggingLevelRouter.monitor
    def execute(self, dto_operand: TokenCarrier) -> ValidationResult:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not a number.
                    _   A Team check fails
                    -   A Rank check fails
                    -   Identity check fails
            2.  Otherwise, send the success result.
        Args:
            dto_operand: TokenDtoOperand
        Returns:
            ValidationResult[TokenDtoOperand]
        Raises:
             TokenConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        priming_test = self._toolkit.priming_validator.execute(
            target_model=self._toolkit.operand_model,
            null_exception=self._toolkit.operand_null_exception,
        )
        if priming_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=priming_test.exception,
                )
            )
        dto = cast(TokenCarrier, priming_test.payload)
        if not dto.is_model_carrier:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyCheckerException.MSG,
                    err_code=TokenConsistencyCheckerException.ERR_CODE,
                    ex=priming_test.exception,
                )
            )

        
        # --- Forward the work product to the caller. ---#
        return priming_test