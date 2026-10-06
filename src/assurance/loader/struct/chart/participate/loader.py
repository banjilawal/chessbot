# src/assurance/load/struct/chart/participate/loader.py

"""
Module: assurance.load.struct.chart.participate.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ChartLoader, ParticipationValidatorToolkit
from domain import Participation, ParticipationPrimeExtract
from err import (
    ParticipationCarrierEmptyException, ParticipationLoaderException,
    ParticipationValidationRequestNullException
)
from exchange import WalkValidationRequest
from transit import ParticipationCarrier

from util import LoggingLevelRouter


class ParticipationLoader(ChartLoader[Participation]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ParticipationValidationRequest
            -   ParticipationCarrier
            -   ParticipationBlueprint

    Attributes:
        toolkit: ParticipationValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ParticipationPrimeExtract[T]

    Super Class:
        ChartLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ParticipationValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ParticipationValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ParticipationValidatorToolkit())
    
    @property
    def toolkit(self) -> ParticipationValidatorToolkit:
        return cast(ParticipationValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ParticipationPrimeExtract]:
        """
        Extract the ParticipationBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a ParticipationValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a ParticipationCarrier
                        -   An empty ParticipationCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a ParticipationPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ParticipationPrimeExtract]
        Raises:
            ParticipationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=WalkValidationRequest,
            null_exception=ParticipationValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationLoaderException.MSG,
                    err_code=ParticipationLoaderException.ERR_CODE,
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
                ParticipationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationLoaderException.MSG,
                    err_code=ParticipationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(ParticipationCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationLoaderException.MSG,
                    err_code=ParticipationLoaderException.ERR_CODE,
                    ex=ParticipationCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ParticipationCarrierEmptyException.MSG,
                        err_code=ParticipationCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ParticipationPrimeExtract(
            reference=carrier,
            safe_blueprint=blueprint,
        )
        return ValidationResult.success(extract)