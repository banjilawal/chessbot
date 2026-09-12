# src/assurance/validator/model/player/validator.py

"""
Module: assurance.validator.model.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    MachinePlayerValidator, HumanPlayerValidator, ModelValidator, PawnPlayerValidator,
    PlayerValidatorToolkit
)
from domain import Player, PlayerValidationRequest
from err import PlayerValidationRequestNullException, PlayerValidatorException
from transit import MachineCarrier, HumanPlayerCarrier, PawnPlayerCarrier, PlayerCarrier
from util import LoggingLevelRouter


class PlayerValidator(ModelValidator[Player]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: PlayerValidationToolkit

    Provides:
        - def execute(request: PlayerValidationRequest) ->ValidationResult[PlayerCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[PlayerValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerValidationToolkit]
        """
        super().__init__(toolkit=toolkit or PlayerValidatorToolkit())
    
    @property
    def toolkit(self) -> PlayerValidatorToolkit:
        return cast(
            PlayerValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PlayerValidationRequest) -> ValidationResult[PlayerCarrier]:
        """
        Certify a candidate is a PlayerCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a PlayerCarrier or its null.
                    - The candidate is an empty PlayerCarrier.
                    - Any Player attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[PlayerCarrier]
        Raises:
            PlayerValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=PlayerValidationRequest,
            null_exception=PlayerValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(PlayerValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(PlayerCarrier, carrier_validation.payload)
        
        # --- Extract the blueprint to verify the attributes. ---#

        if carrier.is_human_player_carrier:
            validated_carrier = cast(HumanPlayerCarrier, carrier)
            helper = HumanPlayerValidator()
            return helper.execute(validated_carrier)
        validated_carrier = cast(MachineCarrier, carrier)
        helper = MachinePlayerValidator()
        return helper.execute(validated_carrier)

    
    