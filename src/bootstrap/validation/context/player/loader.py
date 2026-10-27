# src/bootstrap/validation/context/player/loader.py

"""
Module: bootstrap.validation.context.player.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, PlayerLayerToolkit
from domain import Player, PlayerContextPrimeExtract
from err import (
    PlayerCarrierEmptyException, PlayerContextValidationLoaderException, PlayerContextValidationRequestNullException
)
from exchange import PlayerContextValidationRequest
from transit import PlayerCarrier

from util import LoggingLevelRouter


class PlayerContextValidationLoader(ContextValidationLoader[PlayerContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   PlayerContextValidationRequest
            -   PlayerCarrier
            -   PlayerBlueprint

    Attributes:
        toolkit: PlayerLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[PlayerContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[PlayerLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerLayerToolkit]
        """
        super().__init__(toolkit=toolkit or PlayerLayerToolkit())
    
    @property
    def toolkit(self) -> PlayerLayerToolkit:
        return cast(PlayerLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PlayerContextPrimeExtract]:
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
            2.  Otherwise, pack the original carrier and the blueprint in a PlayerContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PlayerContextPrimeExtract]
        Raises:
            PlayerLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=PlayerContextValidationRequest,
            null_exception=PlayerContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationLoaderException.MSG,
                    err_code=PlayerContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[PlayerContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationLoaderException.MSG,
                    err_code=PlayerContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(PlayerContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationLoaderException.MSG,
                    err_code=PlayerContextValidationLoaderException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = PlayerContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)