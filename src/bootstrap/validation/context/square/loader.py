# src/bootstrap/validation/context/square/loader.py

"""
Module: bootstrap.validation.context.square.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, SquareValidatorToolkit
from domain import Square, SquareContextPrimeExtract
from err import (
    SquareCarrierEmptyException, SquareContextValidationLoaderException, SquareContextValidationRequestNullException
)
from exchange import SquareContextValidationRequest
from transit import SquareCarrier

from util import LoggingLevelRouter


class SquareContextValidationLoader(ContextValidationLoader[SquareContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   SquareContextValidationRequest
            -   SquareCarrier
            -   SquareBlueprint

    Attributes:
        toolkit: SquareValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[SquareContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[SquareValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[SquareValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or SquareValidatorToolkit())
    
    @property
    def toolkit(self) -> SquareValidatorToolkit:
        return cast(SquareValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[SquareContextPrimeExtract]:
        """
        Extract the SquareBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a SquareValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a SquareCarrier
                        -   An empty SquareCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a SquareContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareContextPrimeExtract]
        Raises:
            SquareLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=SquareContextValidationRequest,
            null_exception=SquareContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationLoaderException.MSG,
                    err_code=SquareContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[SquareContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationLoaderException.MSG,
                    err_code=SquareContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(SquareContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationLoaderException.MSG,
                    err_code=SquareContextValidationLoaderException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = SquareContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)