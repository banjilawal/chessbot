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
from assurance import RegisterLoader, VectorRegisterValidatorToolkit
from domain import VectorRegister, VectorRegisterPrimeExtract
from err import (
    EmptyVectorRegisterCarrierException, VectorRegisterLoaderException,
    VectorRegisterValidationRequestNullException
)
from exchange import VectorRegisterValidationRequest
from transit import VectorRegisterCarrier

from util import LoggingLevelRouter


class VectorRegisterLoader(RegisterLoader[VectorRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   VectorRegisterValidationRequest
            -   VectorRegisterCarrier
            -   VectorRegisterBlueprint

    Attributes:
        toolkit: VectorRegisterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[VectorRegisterPrimeExtract[T]

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
    def execute(self, candidate: Any) -> ValidationResult[VectorRegisterPrimeExtract]:
        """
        Extract the VectorRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a VectorRegisterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a VectorRegisterCarrier
                        -   An empty VectorRegisterCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a VectorRegisterPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[VectorRegisterPrimeExtract]
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
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterLoaderException.MSG,
                    err_code=VectorRegisterLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(VectorRegisterCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterLoaderException.MSG,
                    err_code=VectorRegisterLoaderException.ERR_CODE,
                    ex=EmptyVectorRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyVectorRegisterCarrierException.MSG,
                        err_code=EmptyVectorRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = VectorRegisterPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)