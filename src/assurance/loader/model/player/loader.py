# src/assurance/load/model/player/loader.py

"""
Module: assurance.load.model.player.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, PlayerValidatorToolkit
from domain import Player, PlayerPrimeExtract
from err import (
    PlayerCarrierEmptyException, PlayerLoaderException, PlayerValidationRequestNullException
)
from exchange import PlayerValidationRequest
from transit import PlayerCarrier

from util import LoggingLevelRouter


class PlayerLoader(ModelLoader[Player]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   PlayerValidationRequest
            -   PlayerCarrier
            -   PlayerBlueprint

    Attributes:
        toolkit: PlayerValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[PlayerPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[PlayerValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or PlayerValidatorToolkit())
    
    @property
    def toolkit(self) -> PlayerValidatorToolkit:
        return cast(PlayerValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PlayerPrimeExtract]:
        """
        Extract the PlayerBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a PlayerValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a PlayerCarrier
                        -   An empty PlayerCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a PlayerPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PlayerPrimeExtract]
        Raises:
            PlayerLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=PlayerValidationRequest,
            null_exception=PlayerValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerLoaderException.MSG,
                    err_code=PlayerLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[PlayerValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerLoaderException.MSG,
                    err_code=PlayerLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(PlayerCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerLoaderException.MSG,
                    err_code=PlayerLoaderException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = PlayerPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)