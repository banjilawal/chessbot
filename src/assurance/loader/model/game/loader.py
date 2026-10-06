# src/assurance/load/model/game/loader.py

"""
Module: assurance.load.model.game.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, GameValidatorToolkit
from domain import Game, GamePrimeExtract
from err import (
    GameCarrierEmptyException, GameLoaderException, GameValidationRequestNullException
)
from exchange import GameValidationRequest
from transit import GameCarrier

from util import LoggingLevelRouter


class GameLoader(ModelLoader[Game]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   GameValidationRequest
            -   GameCarrier
            -   GameBlueprint

    Attributes:
        toolkit: GameValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[GamePrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[GameValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[GameValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or GameValidatorToolkit())
    
    @property
    def toolkit(self) -> GameValidatorToolkit:
        return cast(GameValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[GamePrimeExtract]:
        """
        Extract the GameBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a GameValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a GameCarrier
                        -   An empty GameCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a GamePrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[GamePrimeExtract]
        Raises:
            GameLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=GameValidationRequest,
            null_exception=GameValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameLoaderException.MSG,
                    err_code=GameLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[GameValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameLoaderException.MSG,
                    err_code=GameLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(GameCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameLoaderException.MSG,
                    err_code=GameLoaderException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = GamePrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)