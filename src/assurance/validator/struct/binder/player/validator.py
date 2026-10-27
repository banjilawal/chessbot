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
from assurance import BinderValidator, PlayerBinderLoader, PlayerBinderLayerToolkit
from domain import (
    Archetype, Player, PlayerBinder, PlayerBinderBlueprint,
    PlayerBinderPrimeExtract
)
from err import PlayerBinderCarrierEmptyException, PlayerBinderValidatorException
from exchange import PlayerValidationRequest
from transit import PlayerBinderCarrier, PlayerCarrier
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
    def toolkit(self) -> PlayerBinderLayerToolkit:
        return self.loader.toolkit
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PlayerBinderCarrier]:
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
        loader = self.loader.execute(candidate)
        if loader.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidatorException.MSG,
                    err_code=PlayerBinderValidatorException.ERR_CODE,
                    ex=loader.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(PlayerBinderPrimeExtract, loader.payload)
        carrier = prime_extract.reference
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidatorException.MSG,
                    err_code=PlayerBinderValidatorException.ERR_CODE,
                    ex=PlayerBinderCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerBinderCarrierEmptyException.MSG,
                        err_code=PlayerBinderCarrierEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        entry: Dict[Archetype, Player] = {}
        for key in blueprint.bindings:
            player_validation = self.toolkit.dependency.player.extract_model(
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
            entry[key] = player
        
        # --- FORWARD_THE_APPROPRIATE_WORK_PRODUCT_TO_THE_CALLER. ---#
        
        # The client wants a safe PlayerBinder.
        if prime_extract.recipient_wants_model:
            model = PlayerBinder(
                white_player=entry[Archetype.WHITE],
                black_player=entry[Archetype.BLACK],
            )
            payload = PlayerBinderCarrier(model=model)
            return ValidationResult.success(payload)
        # Otherwise, the client is a PlayerBinderBuilder that needs a Blueprint.
        payload = PlayerBinderCarrier(
            blueprint=PlayerBinderBlueprint(
                white_player=entry[Archetype.WHITE],
                black_player=entry[Archetype.BLACK],
            )
        )
        return ValidationResult.success(payload)

    
    
