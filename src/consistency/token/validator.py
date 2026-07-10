# src/consistency/token/consistency.py

"""
Module: consistency.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import TokenConsistencyException
from model import Token, TokenEntityRegister
from primary import TokenRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from consistency import ConsistencyChecker


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

    Provides:
        -   def validate(
                candidate: Any, toolkit: TokenToolkit) -> ValidationResult[Token]:

    Super Class:
        Consistency
    """
    
    def __init__(self, root_certifier: TokenRootCertifier | None = TokenRootCertifier()):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> TokenRootCertifier:
        return cast(TokenRootCertifier, self.root_certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
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
            candidate: Any
            toolkit: TokenToolkit
            blueprint_consistency: TokenCertifier
        Returns:
            ValidationResult[Token]
        Raises:
             TokenConsistencyException
        """
        method = f"{self.__class__.__name__}.execute"
        
        entity_test = self.root_certifier.toolkit.priming_consistency.execute(
            target_model=self.root_certifier.toolkit.model,
            null_exception=self.root_certifier.toolkit.null_exception,
        )
        if entity_test.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyException.MSG,
                    err_code=TokenConsistencyException.ERR_CODE,
                    ex=entity_test.exception,
                )
            )
        entity_register = TokenEntityRegister(
            model=cast(Token, candidate),
            null_exception=self.root_certifier.toolkit.null_exception
        )

        # Handle the case that, bootstrap is not successful.
        bootstrap_result = self.root_certifier.execute(candidate=entity_register)
        if bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenConsistencyException.MSG,
                    err_code=TokenConsistencyException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return bootstrap_result