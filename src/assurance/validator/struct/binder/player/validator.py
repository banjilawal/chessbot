# src/assurance/validator/struct/binder/player/validator.py

"""
Module: assurance.validator.struct.binder.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, cast

from artifcat import ValidationResult
from assurance import BinderValidator, PlayerBinderLoader, PlayerBinderValidatorToolkit
from domain import Player, PlayerBinder
from err import PlayerBinderConsistencyException, PlayerBinderValidatorException
from exchange import PlayerValidationRequest
from transit import PlayerCarrier
from util import IdFactory, LoggingLevelRouter


class PlayerBinderValidator(BinderValidator[PlayerBinder]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null Entity.
        2.  Run safety checks on structs and blueprints inside an Entity's payload.

    Attributes:
        loader: PlayerBinderLoader

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[PlayerBinder]:

    Super Class:
        BinderValidator
    """
    
    def __init__(
            self,
            loader: Optional[PlayerBinderLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PlayerBinderLoader]
        """
        super().__init__(loader=loader or PlayerBinderLoader())
        
    @property
    def loader(self) -> PlayerBinderLoader:
        return cast(PlayerBinderLoader, super().loader)
    
    @property
    def toolkit(self) -> PlayerBinderValidatorToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PlayerBinder]:
        """
        Certify a PlayerBinder's payload is either a PlayerBinder or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a PlayerBinderValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a PlayerBinder
                            an empty PlayerBinder.
                    -   Either the player, row, or column attributes are flagged unsafe.
            2.  Otherwise, Send a  with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[PlayerBinder]
        Raises:
            PlayerBinderValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
                
        # Handle the case that loader fails.
        load = self.loader.execute(candidate)
        if load.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidatorException.MSG,
                    err_code=PlayerBinderValidatorException.ERR_CODE,
                    ex=load.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        struct = cast(PlayerBinder, load.payload)
        
        if struct.is_not_consistent:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidatorException.MSG,
                    err_code=PlayerBinderValidatorException.ERR_CODE,
                    ex=PlayerBinderConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerBinderConsistencyException.MSG,
                        err_code=PlayerBinderConsistencyException.ERR_CODE,
                    )
                )
            )
        
        entry = struct.to_dict
        endpoints: Dict[str, Player] = {}
        for key in struct.to_dict:
            player_validation = self.toolkit.wrapper.player.extract_model(
                request=PlayerValidationRequest(
                    item=PlayerCarrier(model=entry[key]),
                    id=IdFactory.next_id(class_name="PlayerBinderRequest")
                )
            )
            if player_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    PlayerBinderValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerBinderValidatorException.MSG,
                        err_code=PlayerBinderValidatorException.ERR_CODE,
                        ex=player_validation.exception
                    )
                )
            player = cast(Player, player_validation.payload)
            endpoints[key] = player
            
        # --- Forward the appropriate work product to the caller. ---#
        return ValidationResult.success(
            PlayerBinder(
                origin=endpoints["origin"],
                destination=endpoints["destination"],
            )
        )

    
    
