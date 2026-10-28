# src/bootstrap/validation/model/maneuver/loader.py

"""
Module: bootstrap.validation.context.maneuver.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ManeuverLayerToolkit
from bootstrap import ModelValidationLoader
from domain import Maneuver, ManeuverPrimeExtract
from err import (
    ManeuverCarrierEmptyException, ManeuverValidationLoaderException, ManeuverValidationRequestNullException
)
from exchange import ManeuverValidationRequest
from transit import ManeuverCarrier

from util import LoggingLevelRouter


class ManeuverValidationLoader(ModelValidationLoader[Maneuver]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ManeuverValidationRequest
            -   ManeuverCarrier
            -   ManeuverBlueprint

    Attributes:
        toolkit: ManeuverLayerToolkit

    Provides:
        -   def execute(item: Any) -> ValidationResult[ManeuverPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ManeuverLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ManeuverLayerToolkit]
        """
        super().__init__(toolkit=toolkit or ManeuverLayerToolkit())
    
    @property
    def toolkit(self) -> ManeuverLayerToolkit:
        return cast(ManeuverLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[ManeuverPrimeExtract]:
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
            item: Any
        Returns:
            ValidationResult[ManeuverPrimeExtract]
        Raises:
            ManeuverLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=item,
            target_model=ManeuverValidationRequest,
            null_exception=ManeuverValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationLoaderException.MSG,
                    err_code=ManeuverValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[ManeuverValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationLoaderException.MSG,
                    err_code=ManeuverValidationLoaderException.ERR_CODE,
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
                ManeuverValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationLoaderException.MSG,
                    err_code=ManeuverValidationLoaderException.ERR_CODE,
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ManeuverPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)