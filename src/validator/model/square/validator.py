# src/validator/square/validator.py

"""
Module: validator.square.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from consistency import SquareConsistencyChecker
from err import SquareValidatorException
from model import Square
from operand import SquareEntityOperand
from primary import SquareRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from validator import ModelValidator


class SquareValidator(ModelValidator[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Square instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: SquareRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult
        -   _bootstrapper(candidate: Any) -> ValidationResult
        -   _model_extractor(payload) -> Square

    Super Class:
        ModelValidator
    """
    _consistency_checker: SquareConsistencyChecker
    
    def __init__(
            self,
            root_certifier: SquareRootCertifier | None = SquareRootCertifier(),
            consistency_checker: SquareConsistencyChecker | None = SquareConsistencyChecker(),
    ):
        super().__init__(root_certifier=root_certifier)
        self._consistency_checker = consistency_checker
    
    @property
    def root_certifier(self) -> SquareRootCertifier:
        return cast(SquareRootCertifier, self.root_certifier)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Square that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   The candidate cannot get bootstrapped into a SquareDtoOperand.
                    -   The dto_operand cannot is not certified as safe.
            2.  Otherwise, extract the Square from the dto_operand then, send it in the
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Square]
        Raises:
             SquareValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the bootstrap does not produce a SquareDtoOperand
        bootstrap = self._bootstrapper(candidate=candidate)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # Handle the case that, SquareDtoOperand is not certified as safe.
        certification = self.root_certifier.execute(
            dto_operand=cast(
                self.root_certifier.toolkit.operand_model,
                bootstrap.payload,
            )
        )
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # Extract the square from certification payload
        model = self._model_extractor(certification.payload)
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def _bootstrapper(self, candidate: Any) -> ValidationResult:
        """
        Put a safe Square in a DtoOperand.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null or not a square.
            2.  Otherwise, encapsulate in a SquareDtoOperand then, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareDtoOperand]
        Raises:
             SquareValidatorException
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
                SquareValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidatorException.MSG,
                    err_code=SquareValidatorException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        dto_operand = SquareEntityOperand(
            model=cast(
                self.root_certifier.toolkit.model,
                bootstrap.payload,
            )
        )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(dto_operand)
    
    @LoggingLevelRouter.monitor
    def _model_extractor(self, payload) -> Square:
        """
        Extract the Square in a DtoOperand

        Action:
            1.  Cast the payload into a SquareDtoOperand.
            2.  Extract and cast its content into a Square.
            3.  Return the Square.
        Args:
            payload
        Returns:
            ValidationResult[SquareDtoOperand]
        Raises:
             SquareValidatorException
        """
        operand = cast(
            self.root_certifier.toolkit.operand_model,
            payload
        )
        return cast(self.root_certifier.toolkit.model, operand.entity)