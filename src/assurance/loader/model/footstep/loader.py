# src/assurance/load/model/footstep/loader.py

"""
Module: assurance.load.model.footstep.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, FootstepValidatorToolkit
from domain import Footstep, FootstepPrimeExtract
from err import (
    FootstepCarrierEmptyException, FootstepLoaderException,
    FootstepValidationRequestNullException
)
from exchange import FootstepValidationRequest
from transit import FootstepCarrier

from util import LoggingLevelRouter


class FootstepLoader(ModelLoader[Footstep]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   FootstepValidationRequest
            -   FootstepCarrier
            -   FootstepBlueprint

    Attributes:
        toolkit: FootstepValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[FootstepPrimeExtract[T]

    Super Class:
        ModelLoader
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
    def execute(self, candidate: Any) -> ValidationResult[FootstepPrimeExtract]:
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
            2.  Otherwise, pack the original carrier and the blueprint in a FootstepPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[FootstepPrimeExtract]
        Raises:
            FootstepLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=FootstepValidationRequest,
            null_exception=FootstepValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepLoaderException.MSG,
                    err_code=FootstepLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[FootstepValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepLoaderException.MSG,
                    err_code=FootstepLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(FootstepCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepLoaderException.MSG,
                    err_code=FootstepLoaderException.ERR_CODE,
                    ex=FootstepCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepCarrierEmptyException.MSG,
                        err_code=FootstepCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = FootstepPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)