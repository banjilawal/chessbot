# src/assurance/primitive/binder/game/validator.py

"""
Module: assurance.primitive.binder.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, cast


from artifcat import ValidationResult
from assurance import GameValidator, PlayerValidator, PrimingValidator
from config import GameColor
from domain import (
    Game, GamePlayerColorBinder, GameValidationRequest, Player, PlayerValidationRequest
)
from err import (
    DuplicatePlayerException, EmptyGameCarrierException, EmptyItemException,
    EmptyPlayerCarrierException, GameColorNullException,
    GamePlayerColorBinderOverCapacityException, GamePlayerColorBinderValidatorException
)
from microservice import IdentityService
from transit import GameCarrier, PlayerCarrier
from util import IdFactory, LoggingLevelRouter


class GamePlayerColorBinderValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a GamePlayerColorBinder is safe to use.

    Attributes:

    Provides:
        - def validate(
                    candidate: Any,
                    floor: int = 0,
                    ceiling: int = BOARD_DIMENSION,
            ) -> ValidationResult[int]:

    Super Class:
    """
    _game_validator: GameValidator
    _identity_service: IdentityService
    _player_validator: PlayerValidator
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            game_validator: Optional[GameValidator] | None = None,
            identity_service: Optional[IdentityService] | None = None,
            player_validator: Optional[PlayerValidator] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            game_validator: Optional[GameValidator]
            identity_service: Optional[IdentityService]
            player_validator: Optional[PlayerValidator]
            priming_validator: Optional[PrimingValidator]
        """
        self._game_validator = game_validator or GameValidator()
        self._identity_service = identity_service or IdentityService()
        self._player_validator = player_validator or PlayerValidator()
        self._priming_validator = priming_validator or PrimingValidator()

    
    @LoggingLevelRouter.monitor
    def execute(self, candidate) -> ValidationResult[GamePlayerColorBinder]:
        """
        Make sure a GamePlayerBinder is safe before use.

        Action:
            1.  Send an exception in the Validation result if any of these conditions occur
                    - Not null
                    - int between floor and ceiling
        Args:
            candidate: Any
        Returns:
            ValidationResult[GamePlayerColorBinder]
        Raises:
            GamePlayerColorBinderValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the validator is not primed.
        priming_result = self._priming_validator.execute(
            candidate=candidate,
            target_model=GamePlayerColorBinder,
            null_exception=GamePlayerColorBinderNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        target = cast(GamePlayerColorBinder, priming_result.payload)
        
        id_validation = self._identity_service.validate_id(candidate=target.id)
        if id_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=id_validation.exception,
                )
            )
        game_validation = self._game_validator.execute(
            candidate=GameValidationRequest(
                item=GameCarrier(model=target.primary),
                id=IdFactory.next_id(class_name="GameValidationRequest"),
            )
        )
        if game_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=game_validation.exception,
                )
            )
        game_carrier = cast(GameCarrier, game_validation.payload)
        if not game_carrier.is_carrying_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=EmptyGameCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyGameCarrierException.MSG,
                        err_code=EmptyGameCarrierException.ERR_CODE,
                    ),
                )
            )
        if target.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=EmptyItemException(),
                )
            )
        if target.is_over_capacity:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=GamePlayerColorBinderOverCapacityException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GamePlayerColorBinderOverCapacityException.MSG,
                        err_code=GamePlayerColorBinderOverCapacityException.ERR_CODE,
                    ),
                )
            )
        color_dict = Dict[str, GameColor]
        for key in target.to_dict:
            key_validation = self._priming_validator.execute(
                candidate=key,
                target_model=GameColor,
                null_exception=GameColorNullException(),
            )
            color = cast(GameColor, key_validation.payload)
            if color == GameColor.WHITE:
                color_dict["white"] = color
            elif color == GameColor.BLACK:
                color_dict["black"] = color
            else:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    GamePlayerColorBinderValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GamePlayerColorBinderValidatorException.MSG,
                        err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                        ex=CapacityException(),
                    )
                )
        
        player_dict: dict[str, Player]
        for key in target.to_dict:
            player_validation = self._player_validator.execute(
                candidate=PlayerValidationRequest(
                    item=PlayerCarrier(model=target.to_dict[key]),
                    id=IdFactory.next_id("PlayerValidationRequest"),
                )
            )
            if player_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    GamePlayerColorBinderValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GamePlayerColorBinderValidatorException.MSG,
                        err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                        ex=player_validation.exception,
                    )
                )
            player_carrier = cast(PlayerCarrier, player_validation.payload)
            if not player_carrier.is_carrying_model:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    GamePlayerColorBinderValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GamePlayerColorBinderValidatorException.MSG,
                        err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                        ex=EmptyPlayerCarrierException(
                            cls_mthd=method,
                            cls_name=self.__class__.__name__,
                            msg=EmptyPlayerCarrierException.MSG,
                            err_code=EmptyPlayerCarrierException.ERR_CODE,
                        ),
                    )
                )
            player = cast(Player, player_carrier.entity)
            if key == GameColor.WHITE:
                player_dict["white"] = player
            player_dict["black"] = player
        if player_dict["white"] == player_dict["black"]:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GamePlayerColorBinderValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GamePlayerColorBinderValidatorException.MSG,
                    err_code=GamePlayerColorBinderValidatorException.ERR_CODE,
                    ex=DuplicatePlayerException(),
                )
            )
        id = cast(int, id_validation.payload)
        game = cast(Game, game_carrier.entity)
        binder = GamePlayerColorBinder(
            id=id,
            primary=game,
            white_player=player_dict["white"],
            black_player=player_dict["black"],
        )
        return ValidationResult.success(binder)
        