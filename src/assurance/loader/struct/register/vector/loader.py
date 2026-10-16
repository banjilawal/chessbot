# src/assurance/load/struct/register/vector/loader.py

"""
Module: assurance.load.struct.register.vector.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import RegisterValidationLoader, VectorRegisterValidatorToolkit
from domain import VectorRegister
from err import (
    VectorRegisterConsistencyException, VectorRegisterEmptyException, VectorRegisterLoaderException,
    VectorRegisterValidationRequestNullException
)
from exchange import VectorRegisterValidationRequest

from util import LoggingLevelRouter


class VectorRegisterLoader(RegisterValidationLoader[VectorRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   VectorRegisterValidationRequest
            -   VectorRegister
            -   VectorRegisterBlueprint

    Attributes:
        toolkit: VectorRegisterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[VectorRegister[T]

    Super Class:
        RegisterLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[VectorRegisterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[VectorRegisterValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or VectorRegisterValidatorToolkit())
    
    @property
    def toolkit(self) -> VectorRegisterValidatorToolkit:
        return cast(VectorRegisterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[VectorRegister]:
        """
        Model the VectorRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a VectorRegisterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a VectorRegister
                        -   An empty VectorRegister.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a VectorRegister
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorRegister]
        Raises:
            VectorRegisterLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=VectorRegisterValidationRequest,
            null_exception=VectorRegisterValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterLoaderException.MSG,
                    err_code=VectorRegisterLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[VectorRegisterValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterLoaderException.MSG,
                    err_code=VectorRegisterLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        model = cast(VectorRegister, model_validation.payload)
        # --- Send the work product. ---#
        return ValidationResult.success(model)