# src/exchange/wrapper/validation/model/game/wrapper.py

"""
Module: exchange.wrapper.validation.model.game.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import GameValidationResponse, ValidationResult
from domain import Game, GameBlueprint
from err import GameValidationResponderException, GameValidationResponseWrapperException, EmptyGameCarrierException
from exchange import (
    GameValidationResponder, ModelValidationResponseWrapper, GameValidationRequest
)
from util import LoggingLevelRouter


class GameValidationResponseWrapper(
    ModelValidationResponseWrapper[Game]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Game
                _   GameBlueprint
            products from GameValidationResponder.

    Attributes:
        responder: GameValidationResponder
        
    Provides:
        -   def extract_model(
                    request: GameValidationRequest
            ) -> ValidationResult[Game]
            
        -   def extract_blueprint(
                    request: GameValidationRequest
            ) -> ValidationResult[GameBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[GameValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[GameValidationResponder]
        """
        super().__init__(responder=responder or GameValidationResponder())
    
    @property
    def responder(self) -> GameValidationResponder:
        return cast(GameValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: GameValidationRequest,
    ) -> ValidationResult[Game]:
        """
        Extract a Game safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Game from the success response then send it 
                to the client.
        Args:
            request: GameValidationRequest
        Result:
            ValidationResult[Game]
        Raises:
            GameValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationResponseWrapperException.MSG,
                    err_code=GameValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(GameValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationResponderException.MSG,
                    err_code=GameValidationResponderException.ERR_CODE,
                    ex=EmptyGameCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyGameCarrierException.MSG,
                        err_code=EmptyGameCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Game, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: GameValidationRequest,
    ) -> ValidationResult[GameBlueprint]:
        """
        Extract a GameBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the GameBluprint from the success response
                then send it to the client.
        Args:
            request: GameValidationRequest
        Result:
            ValidationResult[GameBlueprint]
        Raises:
            GameValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationResponseWrapperException.MSG,
                    err_code=GameValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(GameValidationResponse, result)
        if not response.valid_game:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationResponderException.MSG,
                    err_code=GameValidationResponderException.ERR_CODE,
                    ex=EmptyGameCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyGameCarrierException.MSG,
                        err_code=EmptyGameCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(GameBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)