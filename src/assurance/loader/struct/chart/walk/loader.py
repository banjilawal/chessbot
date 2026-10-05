# src/assurance/load/struct/chart/walk/loader.py

"""
Module: assurance.load.struct.chart.walk.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ChartLoader, WalkValidatorToolkit
from domain import Walk, WalkPrimeExtract
from err import (
    WalkCarrierEmptyException, WalkoaderException, WalkValidationRequestNullException
)
from exchange import WalkValidationRequest
from transit import WalkCarrier

from util import LoggingLevelRouter


class WalkLoader(ChartLoader[Walk]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   WalkValidationRequest
            -   WalkCarrier
            -   WalkBlueprint

    Attributes:
        toolkit: WalkValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[WalkPrimeExtract[T]

    Super Class:
        ChartLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[WalkValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[WalkValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or WalkValidatorToolkit())
    
    @property
    def toolkit(self) -> WalkValidatorToolkit:
        return cast(WalkValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[WalkPrimeExtract]:
        """
        Extract the WalkBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a WalkValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a WalkCarrier
                        -   An empty WalkCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a WalkPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[WalkPrimeExtract]
        Raises:
            WalkLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=WalkValidationRequest,
            null_exception=WalkValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkoaderException.MSG,
                    err_code=WalkoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[WalkValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkoaderException.MSG,
                    err_code=WalkoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(WalkCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkoaderException.MSG,
                    err_code=WalkoaderException.ERR_CODE,
                    ex=WalkCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=WalkCarrierEmptyException.MSG,
                        err_code=WalkCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = WalkPrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)