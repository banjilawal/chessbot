# src/validator/model/game/validator.py

"""
Module: validator.model.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from assurance import GameValidatorToolkit, ModelValidator
from domain import (
    Game, GameBlueprint, GameValidationRequest
)
from err import (
    GameCarrierEmptyException, GameValidationRequestNullException,
    GameValidatorException
)

from artifcat import ValidationResult
from transit import GameCarrier, PathCarrier, TokenCarrier
from util import IdFactory, LoggingLevelRouter


class GameValidator(ModelValidator[Game]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a GameCarrier is safe to use.

    Attributes:
        toolkit: GameValidatorToolkit

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[GameCarrier]:

    Super Class:
        ModelValidator
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
    def execute(self, candidate: Any) -> ValidationResult[GameCarrier]:
        """
        Certify a GameCarrier's payload is either a Game or a Blueprint 
        that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The request is either null or not a GameValidatorRequest.
                    -   The request's payload is either,
                            null
                            not a GameCarrier
                            an empty GameCarrier.
                    -   Either the id, token, or owner attributes are flagged unsafe.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[GameCarrier]
        Raises:
            GameValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.wrapper.priming_validator.execute(
            candidate=candidate,
            target_model=GameValidationRequest,
            null_exception=GameValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        request = cast(GameValidationRequest, priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.wrapper.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to into carrier to extract the blueprint. ---#
        carrier = cast(GameCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that any id in the blueprint is flagged.
        id_validation = self.toolkit.wrapper.identity_service.validate_blueprint_id(
            owner_blueprint=Type[self.toolkit.metadata.types.blueprint]
        )
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        # --- Extract validation payloads. ---#
        id = cast(int, id_validation.payload)
        arena = blueprint.arena
        white_player = blueprint.white_player
        black_player = blueprint.black_player
        binder_id = blueprint.binder_id
        
        # --- Forward the appropriate work product to the caller. ---#
        # The model case
        if carrier.has_model:
            payload = Game(
                id=id,
                arena=arena,
                white_player=white_player,
                black_player=black_player,
                binder_id=binder_id,
            )
            return ValidationResult.success(GameCarrier(model=payload))
        # The blueprint case
        payload = GameBlueprint(
            id=id,
            arena=arena,
            white_player=white_player,
            black_player=black_player,
            binder_id=binder_id,
        )
        return ValidationResult.success(GameCarrier(blueprint=payload))
        
        
