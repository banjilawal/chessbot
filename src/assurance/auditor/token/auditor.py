# src/assurance/auditor/token/assurance/auditor.py

"""
Module: assurance.auditor.token.checker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from assurance.auditor import Auditor
from err import TokenAuditorException
from model import Token
from result import ValidationResult
from util import LoggingLevelRouter


class TokenAuditor(Auditor[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:
    
    Provides:
        -    execute(item: Token) -> ValidationResult[Token]

    Super Class:
        Consistency
    """
    
    def __init__(self, toolkit):
        super().__init__()
    

    @LoggingLevelRouter.monitor
    def execute(self, item: Token) -> ValidationResult[Token]:
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
            item: Token
        Returns:
            ValidationResult[TokenDtoOperand]
        Raises:
             TokenConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        team = item.team
        game_board = team.board
        
        if item not in team.roster:
            ValidationResult.failure(
                TokenAuditorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAuditorException.MSG,
                    err_code=TokenAuditorException.ERR_CODE,
                )
            )
        token = item
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(token)