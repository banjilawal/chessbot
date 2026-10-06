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
from domain import SquareRegister, SquareRegisterPrimeExtract
from err import (
    EmptySquareRegisterCarrierException, SquareRegisterLoaderException,
    SquareRegisterValidationRequestNullException
)
from exchange import SquareRegisterValidationRequest
from transit import SquareRegisterCarrier

from util import LoggingLevelRouter


class SquareRegisterLoader(RegisterLoader[SquareRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   SquareRegisterValidationRequest
            -   SquareRegisterCarrier
            -   SquareRegisterBlueprint

    Attributes:
        toolkit: SquareRegisterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[SquareRegisterPrimeExtract[T]

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
    def execute(self, candidate: Any) -> ValidationResult[SquareRegisterPrimeExtract]:
        """
        Extract the SquareRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a SquareRegisterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a SquareRegisterCarrier
                        -   An empty SquareRegisterCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a SquareRegisterPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareRegisterPrimeExtract]
        Raises:
            SquareRegisterLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=SquareRegisterValidationRequest,
            null_exception=SquareRegisterValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterLoaderException.MSG,
                    err_code=SquareRegisterLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[SquareRegisterValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterLoaderException.MSG,
                    err_code=SquareRegisterLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(SquareRegisterCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterLoaderException.MSG,
                    err_code=SquareRegisterLoaderException.ERR_CODE,
                    ex=EmptySquareRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptySquareRegisterCarrierException.MSG,
                        err_code=EmptySquareRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = SquareRegisterPrimeExtract(reference=carrier, safe_blueprint=blueprint)
        return ValidationResult.success(extract)