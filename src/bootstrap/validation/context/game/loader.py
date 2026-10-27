# src/bootstrap/validation/context/game/loader.py

"""
Module: bootstrap.validation.context.game.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, GameLayerToolkit
from domain import Game, GameContextPrimeExtract
from err import (
    GameCarrierEmptyException, GameContextValidationLoaderException, GameContextValidationRequestNullException
)
from exchange import GameContextValidationRequest
from transit import GameCarrier

from util import LoggingLevelRouter


class GameContextValidationLoader(ContextValidationLoader[GameContext]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   GameContextValidationRequest
            -   GameCarrier
            -   GameBlueprint

    Attributes:
        toolkit: GameLayerToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[GameContextPrimeExtract[T]

    Super Class:
        ContextValidationLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[GameLayerToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[GameLayerToolkit]
        """
        super().__init__(toolkit=toolkit or GameLayerToolkit())
    
    @property
    def toolkit(self) -> GameLayerToolkit:
        return cast(GameLayerToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[GameContextPrimeExtract]:
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
            2.  Otherwise, pack the original carrier and the blueprint in a GameContextPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[GameContextPrimeExtract]
        Raises:
            GameLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=GameContextValidationRequest,
            null_exception=GameContextValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationLoaderException.MSG,
                    err_code=GameContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[GameContextValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationLoaderException.MSG,
                    err_code=GameContextValidationLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(GameContextCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationLoaderException.MSG,
                    err_code=GameContextValidationLoaderException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = GameContextPrimeExtract(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)