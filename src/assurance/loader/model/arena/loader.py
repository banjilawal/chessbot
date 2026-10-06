# src/assurance/load/model/arena/loader.py

"""
Module: assurance.load.model.arena.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, ArenaValidatorToolkit
from domain import Arena, ArenaPrimeExtract
from err import (
    EmptyArenaCarrierException, ArenaLoaderException, ArenaValidationRequestNullException
)
from exchange import ArenaValidationRequest
from transit import ArenaCarrier

from util import LoggingLevelRouter


class ArenaLoader(ModelLoader[Arena]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ArenaValidationRequest
            -   ArenaCarrier
            -   ArenaBlueprint

    Attributes:
        toolkit: ArenaValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ArenaPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[ArenaValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[ArenaValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or ArenaValidatorToolkit())
    
    @property
    def toolkit(self) -> ArenaValidatorToolkit:
        return cast(ArenaValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ArenaPrimeExtract]:
        """
        Extract the ArenaBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a ArenaValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a ArenaCarrier
                        -   An empty ArenaCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a ArenaPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ArenaPrimeExtract]
        Raises:
            ArenaLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=ArenaValidationRequest,
            null_exception=ArenaValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaLoaderException.MSG,
                    err_code=ArenaLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[ArenaValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaLoaderException.MSG,
                    err_code=ArenaLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(ArenaCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaLoaderException.MSG,
                    err_code=ArenaLoaderException.ERR_CODE,
                    ex=EmptyArenaCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyArenaCarrierException.MSG,
                        err_code=EmptyArenaCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = ArenaPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)