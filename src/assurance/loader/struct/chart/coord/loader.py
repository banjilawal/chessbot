# src/assurance/load/struct/chart/coord/loader.py

"""
Module: assurance.load.struct.chart.coord.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ChartLoader, CoordChartValidatorToolkit
from domain import CoordChart, CoordChartPrimeExtract
from err import (
    CoordChartCarrierEmptyException, CoordChartLoaderException,
    CoordChartValidationRequestNullException
)
from exchange import CoordChartValidationRequest
from transit import CoordChartCarrier

from util import LoggingLevelRouter


class CoordChartLoader(ChartLoader[CoordChart]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   CoordChartValidationRequest
            -   CoordChartCarrier
            -   CoordChartBlueprint

    Attributes:
        toolkit: CoordChartValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[CoordChartPrimeExtract[T]

    Super Class:
        ChartLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[CoordChartValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[CoordChartValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or CoordChartValidatorToolkit())
    
    @property
    def toolkit(self) -> CoordChartValidatorToolkit:
        return cast(CoordChartValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[CoordChartPrimeExtract]:
        """
        Extract the CoordChartBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a CoordChartValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a CoordChartCarrier
                        -   An empty CoordChartCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a CoordChartPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[CoordChartPrimeExtract]
        Raises:
            CoordChartLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=CoordChartValidationRequest,
            null_exception=CoordChartValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartLoaderException.MSG,
                    err_code=CoordChartLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[CoordChartValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartLoaderException.MSG,
                    err_code=CoordChartLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(CoordChartCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartLoaderException.MSG,
                    err_code=CoordChartLoaderException.ERR_CODE,
                    ex=CoordChartCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordChartCarrierEmptyException.MSG,
                        err_code=CoordChartCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = CoordChartPrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)