# src/assurance/validator/structure/register/toggle/validator.py

"""
Module: assurance.validator.register.toggle.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from domain.metadata.blueprint import CartesianToggleRegisterBlueprint
from carrier import CartesianToggleRegisterCarrier
from err import (
    RegisterEmptyException, RegisterSizeException, CartesianToggleRegisterValidatorException,
    CartesianToggleRegisterMismatchException
)
from domain.structure.register import CartesianToggleRegister
from artifcat import MethodResultType, ValidationResult
from assurance.validator import Validator
from domain.structure.toggle import CartesianToggle
from operation.toolkit import CartesianToggleRegisterToolkit
from util import LoggingLevelRouter


class CartesianToggleRegisterValidator(
    Validator[CartesianToggleRegister]
):
    """
    Role
        - Integrity Maintenance
        - Consistency Assurance


    Responsibilities:
        1.  Ensure a CartesianToggleRegisterBlueprint instance is certified safe,
            reliable and consistent before use.

    Attributes:
        toolkit: Optional[CartesianToggleRegisterToolkit]

    Provides:
        - execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        Validator
    """
    
    def __init__(
            self,
            toolkit: Optional[CartesianToggleRegisterToolkit] |None = CartesianToggleRegisterToolkit()
    ):
        """
        Args:
            toolkit: Optional[CartesianToggleRegisterToolkit]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> CartesianToggleRegisterToolkit:
        return cast(CartesianToggleRegisterToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate, Any) -> ValidationResult[CartesianToggleRegister]:
        """
        Certify a candidate is a CartesianToggleRegisterBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a CartesianToggleRegisterCarrier.
                    - The candidate is an empty CartesianToggleRegisterCarrier.
                    - Either the board, team, formation, rank or id get flagged unsafe.
            2.  For a model_carrier send a CartesianToggleRegister in the success result. Otherwise, send a TokeBlueprint.
        Args:
            candidate, Any
        Returns:
            ValidationResult
        Raises:
            CartesianToggleRegisterValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        carrier_validation = self.carrier_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.carrier_model,
            model_null_exception=self.toolkit.carrier_null_exception,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRegisterValidatorException.MSG,
                    err_code=CartesianToggleRegisterValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # Otherwise, get the payload.
        carrier = cast(self.toolkit.carrier_model, carrier_validation.payload)
        
        # --- extract the carrier's blueprint for additional tests. ---#
        blueprint= carrier.extract_blueprint()
        
        # Handle the wrong number of toggles cases.
        if blueprint.is_blank:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRegisterValidatorException.MSG,
                    err_code=CartesianToggleRegisterValidatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=RegisterEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RegisterEmptyException.MSG,
                        err_code=RegisterEmptyException.ERR_CODE,
                    )
                )
            )
        if blueprint.is_half_full:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianToggleRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRegisterValidatorException.MSG,
                    err_code=CartesianToggleRegisterValidatorException.ERR_CODE,
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
                CartesianToggleRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianToggleRegisterValidatorException.MSG,
                    err_code=CartesianToggleRegisterValidatorException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.VALIDATION_RESULT,
                    ex=CartesianToggleRegisterMismatchException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CartesianToggleRegisterMismatchException.MSG,
                        err_code=CartesianToggleRegisterMismatchException.ERR_CODE,
                    )
                )
            )
        # Handle the case that either slot is not safe.
        toggles: List[CartesianToggle] = []
        
        for item in [blueprint.a, blueprint.b]:
            validation = self.toolkit.vector_toggle_validator.execute(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CartesianToggleRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CartesianToggleRegisterValidatorException.MSG,
                        err_code=CartesianToggleRegisterValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            toggles.append(cast(CartesianToggle, validation.payload))
            
        # --- Extract and cast payloads of the validation results. ---#
        u = toggles[0]
        v = toggles[1]
        
        if carrier.is_carrying_model:
            return ValidationResult.success(
                CartesianToggleRegisterCarrier(
                    model=CartesianToggleRegister(u=u, v=v)
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            CartesianToggleRegisterCarrier(
                blueprint=CartesianToggleRegisterBlueprint(u=u, v=v)
            )
        )