# src/exchange/wrapper/validation/model/player/wrapper.py

"""
Module: exchange.wrapper.validation.model.player.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PlayerValidationResponse, ValidationResult
from domain import Player, PlayerBlueprint
from err import PlayerValidationResponderException, PlayerValidationResponseWrapperException, EmptyPlayerCarrierException
from exchange import (
    PlayerValidationResponder, ModelValidationResponseWrapper, PlayerValidationRequest
)
from util import LoggingLevelRouter


class PlayerValidationResponseWrapper(
    ModelValidationResponseWrapper[Player]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Player
                _   PlayerBlueprint
            products from PlayerValidationResponder.

    Attributes:
        responder: PlayerValidationResponder
        
    Provides:
        -   def extract_model(
                    request: PlayerValidationRequest
            ) -> ValidationResult[Player]
            
        -   def extract_blueprint(
                    request: PlayerValidationRequest
            ) -> ValidationResult[PlayerBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[PlayerValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[PlayerValidationResponder]
        """
        super().__init__(responder=responder or PlayerValidationResponder())
    
    @property
    def responder(self) -> PlayerValidationResponder:
        return cast(PlayerValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: PlayerValidationRequest,
    ) -> ValidationResult[Player]:
        """
        Extract a Player safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Player from the success response then send it 
                to the client.
        Args:
            request: PlayerValidationRequest
        Result:
            ValidationResult[Player]
        Raises:
            PlayerValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationResponseWrapperException.MSG,
                    err_code=PlayerValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationResponderException.MSG,
                    err_code=PlayerValidationResponderException.ERR_CODE,
                    ex=EmptyPlayerCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyPlayerCarrierException.MSG,
                        err_code=EmptyPlayerCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Player, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PlayerValidationRequest,
    ) -> ValidationResult[PlayerBlueprint]:
        """
        Extract a PlayerBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the PlayerBluprint from the success response
                then send it to the client.
        Args:
            request: PlayerValidationRequest
        Result:
            ValidationResult[PlayerBlueprint]
        Raises:
            PlayerValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationResponseWrapperException.MSG,
                    err_code=PlayerValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerValidationResponse, result)
        if not response.valid_player:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationResponderException.MSG,
                    err_code=PlayerValidationResponderException.ERR_CODE,
                    ex=EmptyPlayerCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyPlayerCarrierException.MSG,
                        err_code=EmptyPlayerCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(PlayerBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)