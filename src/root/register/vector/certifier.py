# src/certifier/register/carrier/validator.py

"""
Module: certifier.register.carrier.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List, cast

from blueprint import VectorToggleRegisterBlueprint
from carrier import VectorToggleRegisterCarrier
from err import (
    RegisterEmptyException, RegisterSizeException, VectorToggleRegisterCertifierException,
    VectorToggleRegisterMismatchException
)
from register import VectorToggleRegister
from result import MethodResultType, ValidationResult
from root import RootCertifier
from toggle import VectorToggle
from toolkit import VectorToggleRegisterToolkit
from util import LoggingLevelRouter


class VectorToggleRegisterCertifier(
    RootCertifier[VectorToggleRegister]
):
    """
    Role
        -   Integrity Maintenance
        -   Consistency Assurance


    Responsibilities:
        1.  Ensure a VectorToggleRegisterBlueprint instance is certified safe,
            reliable and consistent before use.

    Attributes:
        toolkit: VectorToggleRegisterToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Certifier
    """
    
    def __init__(
            self,
            toolkit: VectorToggleRegisterToolkit |
                     None = VectorToggleRegisterToolkit()
    ):
        """
        Args:
            toolkit: VectorToggleRegisterToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> VectorToggleRegisterToolkit:
        return cast(VectorToggleRegisterToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult[VectorToggleRegister]:
        """
        Certify a candidate is a VectorToggleRegisterBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The candidate is not a VectorToggleRegisterDtoCarrier.
                    -   The candidate is an empty VectorToggleRegisterDtoCarrier.
                    -   Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a VectorToggleRegister in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            VectorToggleRegisterCertifierException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.model_carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRegisterCertifierException.MSG,
                    err_code=VectorToggleRegisterCertifierException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # Otherwise, get the payload.
        carrier = cast(self.toolkit.carrier_model, carrier_validation.payload)
        
        # --- extract the carrier's blueprint for additional tests. ---#
        blueprint= carrier.extract_blueprint()
        
        # Handle the wrong number of toggles cases.
        if blueprint.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRegisterCertifierException.MSG,
                    err_code=VectorToggleRegisterCertifierException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=RegisterEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RegisterEmptyException.MSG,
                        err_code=RegisterEmptyException.ERR_CODE,
                    )
                )
            )
        if blueprint.is_wrong_size:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRegisterCertifierException.MSG,
                    err_code=VectorToggleRegisterCertifierException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=RegisterSizeException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RegisterSizeException.MSG,
                        err_code=RegisterSizeException.ERR_CODE,
                    )
                )
            )
        if blueprint.toggles_are_different_types:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorToggleRegisterCertifierException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorToggleRegisterCertifierException.MSG,
                    err_code=VectorToggleRegisterCertifierException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=VectorToggleRegisterMismatchException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorToggleRegisterMismatchException.MSG,
                        err_code=VectorToggleRegisterMismatchException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, either slot is not safe.
        toggles: List[VectorToggle] = []
        
        for item in [blueprint.a, blueprint.b]:
            validation = self.toolkit.vector_toggle_validator.execute(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorToggleRegisterCertifierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorToggleRegisterCertifierException.MSG,
                        err_code=VectorToggleRegisterCertifierException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            toggles.append(cast(VectorToggle, validation.payload))
            
        # --- Extract and cast payloads of the validation results. ---#
        u = toggles[0]
        v = toggles[1]
        
        if carrier.is_carrying_model:
            return ValidationResult.success(
                VectorToggleRegisterCarrier(
                    model=VectorToggleRegister(u=u, v=v)
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            VectorToggleRegisterCarrier(
                blueprint=VectorToggleRegisterBlueprint(u=u, v=v)
            )
        )