# src/assurance/load/struct/register/coord/loader.py

"""
Module: assurance.load.struct.register.coord.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import RegisterLoader, CoordRegisterValidatorToolkit
from domain import CoordRegister, CoordRegisterPrimeExtract
from err import (
    EmptyCoordRegisterCarrierException, CoordRegisterLoaderException,
    CoordRegisterValidationRequestNullException
)
from exchange import CoordRegisterValidationRequest
from transit import CoordRegisterCarrier

from util import LoggingLevelRouter


class CoordRegisterLoader(RegisterLoader[CoordRegister]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   CoordRegisterValidationRequest
            -   CoordRegisterCarrier
            -   CoordRegisterBlueprint

    Attributes:
        toolkit: CoordRegisterValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[CoordRegisterPrimeExtract[T]

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
    def execute(self, candidate: Any) -> ValidationResult[CoordRegisterPrimeExtract]:
        """
        Extract the CoordRegisterBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a CoordRegisterValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a CoordRegisterCarrier
                        -   An empty CoordRegisterCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a CoordRegisterPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordRegisterPrimeExtract]
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
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterLoaderException.MSG,
                    err_code=CoordRegisterLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(CoordRegisterCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterLoaderException.MSG,
                    err_code=CoordRegisterLoaderException.ERR_CODE,
                    ex=EmptyCoordRegisterCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyCoordRegisterCarrierException.MSG,
                        err_code=EmptyCoordRegisterCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = CoordRegisterPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)