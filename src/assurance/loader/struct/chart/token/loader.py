# src/assurance/load/struct/chart/token/loader.py

"""
Module: assurance.load.struct.chart.token.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ChartLoader, TokenChartValidatorToolkit
from domain import TokenChart, TokenChartPrimeExtract
from err import (
    TokenChartCarrierEmptyException, TokenChartLoaderException,
    TokenChartValidationRequestNullException
)
from exchange import TokenChartValidationRequest
from transit import TokenChartCarrier

from util import LoggingLevelRouter


class TokenChartLoader(ChartLoader[TokenChart]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TokenChartValidationRequest
            -   TokenChartCarrier
            -   TokenChartBlueprint

    Attributes:
        toolkit: TokenChartValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[TokenChartPrimeExtract[T]

    Super Class:
        ChartLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenChartValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenChartValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TokenChartValidatorToolkit())
    
    @property
    def toolkit(self) -> TokenChartValidatorToolkit:
        return cast(TokenChartValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TokenChartPrimeExtract]:
        """
        Extract the TokenChartBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a TokenChartValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a TokenChartCarrier
                        -   An empty TokenChartCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a TokenChartPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenChartPrimeExtract]
        Raises:
            TokenChartLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=TokenChartValidationRequest,
            null_exception=TokenChartValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartLoaderException.MSG,
                    err_code=TokenChartLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[TokenChartValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartLoaderException.MSG,
                    err_code=TokenChartLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(TokenChartCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartLoaderException.MSG,
                    err_code=TokenChartLoaderException.ERR_CODE,
                    ex=TokenChartCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenChartCarrierEmptyException.MSG,
                        err_code=TokenChartCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = TokenChartPrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)