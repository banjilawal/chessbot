# src/assurance/load/model/rank/loader.py

"""
Module: assurance.load.model.rank.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, RankValidatorToolkit
from domain import Rank, RankPrimeExtract
from err import (
    EmptyRankCarrierException, RankLoaderException, RankValidationRequestNullException
)
from exchange import RankValidationRequest
from transit import RankCarrier

from util import LoggingLevelRouter


class RankLoader(ModelLoader[Rank]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   RankValidationRequest
            -   RankCarrier
            -   RankBlueprint

    Attributes:
        toolkit: RankValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[RankPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[RankValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[RankValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or RankValidatorToolkit())
    
    @property
    def toolkit(self) -> RankValidatorToolkit:
        return cast(RankValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[RankPrimeExtract]:
        """
        Extract the RankBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a RankValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a RankCarrier
                        -   An empty RankCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a RankPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[RankPrimeExtract]
        Raises:
            RankLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=RankValidationRequest,
            null_exception=RankValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankLoaderException.MSG,
                    err_code=RankLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[RankValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankLoaderException.MSG,
                    err_code=RankLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(RankCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankLoaderException.MSG,
                    err_code=RankLoaderException.ERR_CODE,
                    ex=EmptyRankCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyRankCarrierException.MSG,
                        err_code=EmptyRankCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = RankPrimeExtract(carrier=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)