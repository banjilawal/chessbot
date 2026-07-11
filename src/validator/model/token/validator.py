# src/validator/token/validator.py

"""
Module: validator.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from consistency import TokenConsistencyChecker
from err import TokenValidatorException
from model import HomeSquare, KingToken, PawnToken, Square, Token
from operand import TokenDtoOperand
from primary import TokenRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from validator import ModelValidator


class TokenValidator(ModelValidator[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Token instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: TokenRootCertifier

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    _consistency_checker: TokenConsistencyChecker
    
    def __init__(
            self,
            root_certifier: TokenRootCertifier | None = TokenRootCertifier(),
            consistency_checker: TokenConsistencyChecker | None = TokenConsistencyChecker(),
    ):
        super().__init__(root_certifier=root_certifier)
        self._consistency_checker = consistency_checker
        
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
            blueprint_validator: TokenCertifier
        Returns:
            ValidationResult[Token]
        Raises:
             TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        bootstrap = self._bootstrapper(candidate=candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # Handle the case that, bootstrap is not successful.
        certification = self.root_certifier.execute(
            dto_operand=cast(TokenDtoOperand, bootstrap.payload)
        )
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(self.root_certifier.toolkit.model, certification.payload)
        )
    
    @LoggingLevelRouter.monitor
    def _bootstrapper(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null or not a token.
            2.  Otherwise, encapsulate in a TokenDtoOperand then, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenDtoOperand]
        Raises:
             TokenValidatorException
        """
        method = f"{self.__class__.__name__}._bootstrapper"
        
        bootstrap = self.root_certifier.toolkit.priming_validator.execute(
            target_model=self.root_certifier.toolkit.model,
            null_exception=self.root_certifier.toolkit.null_exception,
        )
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(self.root_certifier.toolkit.model, bootstrap.payload)
        )
    
    @LoggingLevelRouter.monitor
    def _token_caster(self, dto: TokenDtoOperand) -> Token:
        """
        Verify the object is a Token that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null or not a token.
            2.  Otherwise, encapsulate in a TokenDtoOperand then, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenDtoOperand]
        Raises:
             TokenValidatorException
        """
        method = f"{self.__class__.__name__}._finalizer"
        
        if isinstance(dto.operand, KingToken):
            return cast(KingToken, dto.operand)
        if isinstance(dto.operand, PawnToken):
            return cast(PawnToken, dto.operand)
        return cast(Token, dto.operand)