# src/assurance/validator/model/game/validator.py

"""
Module: assurance.validator.model.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelValidator, GameValidatorToolkit
from domain import Game, GameBlueprint, GameValidationRequest
from err import (
    GameCarrierEmptyException, GameValidationRequestNullException, GameValidatorException
)
from transit import GameCarrier
from util import LoggingLevelRouter


class GameValidator(ModelValidator[Game]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a GameCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: GameValidationToolkit

    Provides:
        - def execute(request: GameValidationRequest) ->ValidationResult[GameCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[GameValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[GameValidationToolkit]
        """
        super().__init__(toolkit=toolkit or GameValidatorToolkit())
    
    @property
    def toolkit(self) -> GameValidatorToolkit:
        return cast(
            GameValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: GameValidationRequest) -> ValidationResult[GameCarrier]:
        """
        Certify a candidate is a GameCarrier whose payload is either a Game
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a GameCarrier or its null.
                    - The candidate is an empty GameCarrier.
                    - Any Game attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[GameCarrier]
        Raises:
            GameValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=GameValidationRequest,
            null_exception=GameValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidatorException.MSG,
                    err_code=GameValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(GameValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
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
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(
            Type[self.toolkit.metadata.types.carrier],
            carrier_validation.payload,
        )
        # --- Extract the blueprint to verify the attributes. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that there is no blueprint.
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
        
        # Handle the case that any game component in the blueprint is flagged.
        numbers = []
        for number in [blueprint.x, blueprint.y]:
            validation = self.toolkit.helper.number_validator.execute(number)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    GameValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameValidatorException.MSG,
                        err_code=GameValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
            numbers.append(cast(int, validation.payload))
        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case
        if carrier.is_carrying_model:
            return ValidationResult.success(
                GameCarrier(
                    model=Game(
                        x=numbers[0],
                        y=numbers[1],
                    )
                )
            )
        # The blueprint case
        return ValidationResult.success(
            GameCarrier(
                blueprint=GameBlueprint(
                    x=numbers[0],
                    y=numbers[1],
                )
            )
        )
