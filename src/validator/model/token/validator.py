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
from model import Token
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
        -   execute(candidate: Any) -> ValidationResult
        -   _bootstrapper(candidate: Any) -> ValidationResult
        -   _model_extractor(payload) -> Token

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
                    -   The candidate cannot get bootstrapped into a TokenDtoOperand.
                    -   The dto_operand cannot is not certified as safe.
            2.  Otherwise, extract the Token from the dto_operand then, send it in the
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Token]
        Raises:
             TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the bootstrap does not produce a TokenDtoOperand
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
        # Handle the case that, TokenDtoOperand is not certified as safe.
        certification = self.root_certifier.execute(
            dto_operand=cast(
                self.root_certifier.toolkit.operand_model,
                bootstrap.payload,
            )
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
        # Extract the token from certification payload
        model = self._model_extractor(certification.payload)

        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def _bootstrapper(self, candidate: Any) -> ValidationResult:
        """
        Put a safe Token in a DtoOperand.

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
            candidate=candidate,
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
        dto_operand = TokenDtoOperand(
            model=cast(
                self.root_certifier.toolkit.model,
                bootstrap.payload,
            )
        )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(dto_operand)
    
    @LoggingLevelRouter.monitor
    def _model_extractor(self, payload) -> Token:
        """
        Extract the Token in a DtoOperand

        Action:
            1.  Cast the payload into a TokenDtoOperand.
            2.  Extract and cast its content into a Token.
            3.  Return the Token.
        Args:
            payload
        Returns:
            ValidationResult[TokenDtoOperand]
        Raises:
             TokenValidatorException
        """
        operand = cast(
            self.root_certifier.toolkit.operand_model,
            payload
        )
        return cast(self.root_certifier.toolkit.model, operand.entity)