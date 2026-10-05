# src/assurance/load/model/maneuver/loader.py

"""
Module: assurance.load.model.maneuver.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, ManeuverValidatorToolkit
from domain import Maneuver, ManeuverPrimeExtract
from err import (
    ManeuverCarrierEmptyException, ManeuverLoaderException, ManeuverValidationRequestNullException
)
from exchange import ManeuverValidationRequest
from transit import ManeuverCarrier

from util import LoggingLevelRouter


class ManeuverLoader(ModelLoader[Maneuver]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ManeuverValidationRequest
            -   ManeuverCarrier
            -   ManeuverBlueprint

    Attributes:
        toolkit: ManeuverValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ManeuverPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ManeuverValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ManeuverValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ManeuverValidatorToolkit())
    
    @property
    def toolkit(self) -> ManeuverValidatorToolkit:
        return cast(ManeuverValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ManeuverPrimeExtract]:
        """
        Extract the ManeuverBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a ManeuverValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a ManeuverCarrier
                        -   An empty ManeuverCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a ManeuverPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ManeuverPrimeExtract]
        Raises:
            ManeuverLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=ManeuverValidationRequest,
            null_exception=ManeuverValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverLoaderException.MSG,
                    err_code=ManeuverLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[ManeuverValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverLoaderException.MSG,
                    err_code=ManeuverLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(ManeuverCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverLoaderException.MSG,
                    err_code=ManeuverLoaderException.ERR_CODE,
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ManeuverPrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)