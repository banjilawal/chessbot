# src/certifier/register/operand/validator.py

"""
Module: certifier.register.operand.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import CartesianRegisterCertifierException, CartesianRegisterMismatchException
from model import PointRegister
from primary import RootCertifier
from result import ValidationResult
from toolkit import CartesianRegisterToolkit
from util import LoggingLevelRouter


class CartesianRegisterRootCertifier(RootCertifier[PointRegister]):
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
        toolkit: CartesianRegisterToolkit   
    Properties:
        -   execute(candidate: Any,) -> ValidationResult

    Super Class:
        Certifier
    """
    def __init__(
            self, 
            toolkit: CartesianRegisterToolkit | None = CartesianRegisterToolkit()
    ):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> CartesianRegisterToolkit:
        return cast(CartesianRegisterToolkit, self.toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult:
        """
        Verify the candidate is a safe VectorRegister.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   Validator priming fails.
                    -   The vectorRegisterBlueprint's payload is flagged unsafe.
                    -   There is a mismatch between the contexts.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            CartesianRegisterCertifierException
            CartesianRegisterMismatchException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_blueprint=self.toolkit.blueprint_model,
            null_exception=self.toolkit.blueprint_null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianRegisterCertifierException.MSG,
                    err_code=CartesianRegisterCertifierException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast candidate to a VectorRegister for additional tests. ---#
        blueprint = cast(self.toolkit.blueprint_model, candidate)
        
        # Handle the case that the register has mixed contents.
        if register.is_mismatched_register:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianRegisterCertifierException.MSG,
                    err_code=CartesianRegisterCertifierException.ERR_CODE,
                    ex=CartesianRegisterMismatchException(
                        msg=CartesianRegisterMismatchException.MSG,
                        err_code=CartesianRegisterMismatchException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, either slot does not contain a safe vector_opernad.
        for item in [blueprint.a, blueprint.b]:
            validation = self.toolkit.cartesian_validator.execute(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CartesianRegisterCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CartesianRegisterCertifierException.MSG,
                        err_code=CartesianRegisterCertifierException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)