# src/certifier/register/carrier/validator.py

"""
Module: certifier.register.carrier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import SquareRegisterCertifierException
from model import SquareRegister
from result import ValidationResult
from toolkit import SquareRegisterToolkit
from util import LoggingLevelRouter
from validator import Certifier


class SquareRegisterRootCertifier(RootCertifier[SquareRegister]):
    """
    Role
        -   Transaction Worker
        -   Operation Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorRegister instance is certified safe, reliable and consistent
            before use in a binary arithmetic operation.

    Attributes:
        toolkit: SquareRegisterToolkit   
    Properties:
        -   execute(candidate: Any,) -> ValidationResult

    Super Class:
        Certifier
    """
    def __init__(
            self, 
            toolkit: SquareRegisterToolkit | None = SquareRegisterToolkit()
    ):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> SquareRegisterToolkit:
        return cast(SquareRegisterToolkit, self.toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verify the candidate is a safe VectorRegister.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   Validator priming fails.
                    -   The vectorRegister's payload is flagged unsafe.
                    -   There is a mismatch between the contexts.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorRegister]
        Raises:
            SquareRegisterCertifierException
            SquareRegisterMismatchException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_blueprint=self.toolkit.blueprint_model,
            model_null_exception=self.toolkit.blueprint_null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterCertifierException.MSG,
                    err_code=SquareRegisterCertifierException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast candidate to a VectorRegister for additional tests. ---#
        blueprint = cast(self.toolkit.blueprint_model, candidate)
        
        # Handle the case that, either slot is not safe.
        for item in [blueprint.origin, blueprint.destination]:
            validation = self.toolkit.square_validator.execute(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareRegisterCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareRegisterCertifierException.MSG,
                        err_code=SquareRegisterCertifierException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)
            