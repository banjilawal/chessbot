# src/validator/model/state/edge/validator.py

"""
Module: validator.model.state.edge.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import EdgeValidatorException
from model import Edge
from root import EdgeRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from validator import ModelValidator


class EdgeValidator(ModelValidator[Edge]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Edge instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: EdgeRootCertifier

    Provides:
        -   execute(candidate: Any) -> ValidationResult

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            root_certifier: EdgeRootCertifier | None = EdgeRootCertifier(),
    ):
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> EdgeRootCertifier:
        return cast(EdgeRootCertifier, self.root_certifier)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the object is a Edge that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                root_certifier test..
            2.  Otherwise, cast the payload into a Edge and send in the success result.
                success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Edge]
        Raises:
             EdgeValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the candidate is not safe.
        certification = self.root_certifier.execute(candidate)
        if certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EdgeValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EdgeValidatorException.MSG,
                    err_code=EdgeValidatorException.ERR_CODE,
                    ex=certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(
                self.root_certifier.toolkit.model,
                certification.payload
            )
        )