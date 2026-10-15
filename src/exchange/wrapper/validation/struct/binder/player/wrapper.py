# src/exchange/wrapper/validation/struct/binder/player/wrapper.py

"""
Module: exchange.wrapper.validation.struct.binder.player.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PlayerBinderValidationResponse, ValidationResult
from domain import Player, PlayerBlueprint, PlayerBinder, PlayerBinderBlueprint
from err import PlayerBinderValidationResponderException, PlayerBinderValidationResponseWrapperException, PlayerCarrierEmptyException
from exchange import (
    PlayerBinderValidationResponder, BinderValidationResponseWrapper, PlayerBinderValidationRequest
)
from util import LoggingLevelRouter


class PlayerBinderValidationResponseWrapper(
    BinderValidationResponseWrapper[PlayerBinder]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Player
                _   PlayerBlueprint
            products from PlayerBinderValidationResponder.

    Attributes:
        responder: PlayerBinderValidationResponder
        
    Provides:
        -   def extract_model(
                    request: PlayerBinderValidationRequest
            ) -> ValidationResult[Player]
            
        -   def extract_blueprint(
                    request: PlayerBinderValidationRequest
            ) -> ValidationResult[PlayerBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[PlayerBinderValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[PlayerBinderValidationResponder]
        """
        super().__init__(responder=responder or PlayerBinderValidationResponder())
    
    @property
    def responder(self) -> PlayerBinderValidationResponder:
        return cast(PlayerBinderValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: PlayerBinderValidationRequest,
    ) -> ValidationResult[PlayerBinder]:
        """
        Extract a Player safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Player from the success response then send it 
                to the client.
        Args:
            request: PlayerBinderValidationRequest
        Result:
            ValidationResult[Player]
        Raises:
            PlayerBinderValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationResponseWrapperException.MSG,
                    err_code=PlayerBinderValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerBinderValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationResponderException.MSG,
                    err_code=PlayerBinderValidationResponderException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        binder = cast(PlayerBinder, response.valid_model)
        return ValidationResult.success(binder)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PlayerBinderValidationRequest,
    ) -> ValidationResult[PlayerBinderBlueprint]:
        """
        Extract a PlayerBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the PlayerBluprint from the success response
                then send it to the client.
        Args:
            request: PlayerBinderValidationRequest
        Result:
            ValidationResult[PlayerBlueprint]
        Raises:
            PlayerBinderValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationResponseWrapperException.MSG,
                    err_code=PlayerBinderValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerBinderValidationResponse, result)
        if not response.valid_player:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationResponderException.MSG,
                    err_code=PlayerBinderValidationResponderException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(PlayerBinderBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)