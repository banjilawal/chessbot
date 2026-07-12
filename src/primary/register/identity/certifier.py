# src/certifier/register/carrier/validator.py

"""
Module: certifier.register.carrier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import IdentityRegisterCertifierException
from model import IdentityRegister
from primary import RootCertifier
from result import ValidationResult
from toolkit import IdentityRegisterToolkit
from util import LoggingLevelRouter



class IdentityRegisterRootCertifier(RootCertifier[IdentityRegister]):
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
        toolkit: IdentityRegisterToolkit   
    Properties:
        -   execute(candidate: Any,) -> ValidationResult

    Super Class:
        Certifier
    """
    def __init__(
            self, 
            toolkit: IdentityRegisterToolkit | None = IdentityRegisterToolkit()
    ):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> IdentityRegisterToolkit:
        return cast(IdentityRegisterToolkit, self.toolkit)
    
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
            IdentityRegisterCertifierException
            IdentityRegisterMismatchException
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
                IdentityRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityRegisterCertifierException.MSG,
                    err_code=IdentityRegisterCertifierException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast candidate to a VectorRegister for additional tests. ---#
        blueprint = cast(self.toolkit.blueprint_model, candidate)
        
        # Handle the case that, the id is not safe.
        id_validation_result = self.toolkit.number_validator.execute(blueprint.id)
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                IdentityRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityRegisterCertifierException.MSG,
                    err_code=IdentityRegisterCertifierException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the name is not safe.
        name_validation_result = self.toolkit.name_validator.execute(blueprint.id)
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                IdentityRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityRegisterCertifierException.MSG,
                    err_code=IdentityRegisterCertifierException.ERR_CODE,
                    ex=name_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)
            