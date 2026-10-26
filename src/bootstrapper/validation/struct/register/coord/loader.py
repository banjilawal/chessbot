# src/bootstrap/validation/struct/register/coord/loader.py

"""
Module: bootstrap.validation.struct.register.coord.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import RegisterValidationLoader, CoordRegisterValidatorToolkit
from domain import CoordRegister
from err import (
    CoordRegisterConsistencyException, CoordRegisterEmptyException, CoordRegisterLoaderException,
    CoordRegisterValidationRequestNullException
)
from exchange import CoordRegisterValidationRequest

from util import LoggingLevelRouter


class CoordRegisterLoader(RegisterValidationLoader[CoordRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   CoordRegisterValidationRequest
            -   CoordRegister
            -   CoordRegisterBlueprint

    Attributes:
        toolkit: CoordRegisterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[CoordRegister[T]

    Super Class:
        RegisterLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[CoordRegisterValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[CoordRegisterValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or CoordRegisterValidatorToolkit())
    
    @property
    def toolkit(self) -> CoordRegisterValidatorToolkit:
        return cast(CoordRegisterValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordRegister]:
        """
        Model the CoordRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a CoordRegisterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a CoordRegister
                        -   An empty CoordRegister.
                -   A blueprint cannot be modeled from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a CoordRegister
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordRegister]
        Raises:
            CoordRegisterLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=CoordRegisterValidationRequest,
            null_exception=CoordRegisterValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterLoaderException.MSG,
                    err_code=CoordRegisterLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[CoordRegisterValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        model_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.model,
            null_exception=self.toolkit.nulls.model,
        )
        if model_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterLoaderException.MSG,
                    err_code=CoordRegisterLoaderException.ERR_CODE,
                    ex=model_validation.exception,
                )
            )
        # --- Cast model_validation payload to carrier then model blueprint. ---#
        model = cast(CoordRegister, model_validation.payload)
        # --- Send the work product. ---#
        return ValidationResult.success(model)