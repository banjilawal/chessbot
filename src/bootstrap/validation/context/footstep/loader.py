# src/bootstrap/validation/context/footstep/loader.py

"""
Module: bootstrap.validation.context.footstep.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, FootstepValidatorToolkit
from domain import Footstep, FootstepContextPrimeExtract
from err import (
    FootstepCarrierEmptyException, FootstepContextValidationLoaderException,
    FootstepContextValidationRequestNullException
)
from exchange import FootstepContextValidationRequest
from transit import FootstepCarrier

from util import LoggingLevelRouter


class FootstepContextValidationLoader(ContextValidationLoader[FootstepContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   FootstepContextValidationRequest
            -   FootstepCarrier
            -   FootstepBlueprint

    Attributes:
        toolkit: FootstepValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[FootstepContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[FootstepValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[FootstepValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or FootstepValidatorToolkit())
    
    @property
    def toolkit(self) -> FootstepValidatorToolkit:
        return cast(FootstepValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[FootstepContextPrimeExtract]:
        """
        Extract the FootstepBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a FootstepValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a FootstepCarrier
                        -   An empty FootstepCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a FootstepContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[FootstepContextPrimeExtract]
        Raises:
            FootstepLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=FootstepContextValidationRequest,
            null_exception=FootstepContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationLoaderException.MSG,
                    err_code=FootstepContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[FootstepContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationLoaderException.MSG,
                    err_code=FootstepContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(FootstepContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationLoaderException.MSG,
                    err_code=FootstepContextValidationLoaderException.ERR_CODE,
                    ex=FootstepCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepCarrierEmptyException.MSG,
                        err_code=FootstepCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = FootstepContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)