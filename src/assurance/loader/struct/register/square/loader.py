# src/assurance/load/struct/register/square/loader.py

"""
Module: assurance.load.struct.register.square.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import RegisterLoader, SquareRegisterValidatorToolkit
from domain import SquareRegister
from err import (
    SquareRegisterConsistencyException, SquareRegisterEmptyException, SquareRegisterLoaderException,
    SquareRegisterValidationRequestNullException
)
from exchange import SquareRegisterValidationRequest

from util import LoggingLevelRouter


class SquareRegisterLoader(RegisterLoader[SquareRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   SquareRegisterValidationRequest
            -   SquareRegister
            -   SquareRegisterBlueprint

    Attributes:
        toolkit: SquareRegisterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[SquareRegister[T]

    Super Class:
        RegisterLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[SquareRegisterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareRegisterValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or SquareRegisterValidatorToolkit())
    
    @property
    def toolkit(self) -> SquareRegisterValidatorToolkit:
        return cast(SquareRegisterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareRegister]:
        """
        Model the SquareRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a SquareRegisterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a SquareRegister
                        -   An empty SquareRegister.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a SquareRegister
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareRegister]
        Raises:
            SquareRegisterLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=SquareRegisterValidationRequest,
            null_exception=SquareRegisterValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterLoaderException.MSG,
                    err_code=SquareRegisterLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[SquareRegisterValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterLoaderException.MSG,
                    err_code=SquareRegisterLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        model = cast(SquareRegister, model_validation.payload)
        # --- Send the work product. ---#
        return ValidationResult.success(model)