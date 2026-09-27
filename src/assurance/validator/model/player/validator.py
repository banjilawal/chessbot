# src/assurance/validator/model/player/validator.py

"""
Module: assurance.validator.model.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    MachinePlayerValidator, HumanPlayerValidator, ModelValidator, PlayerValidatorToolkit
)
from domain import Player, PlayerValidationRequest
from err import PlayerValidationRequestNullException, PlayerValidatorException
from transit import HumanPlayerCarrier, MachinePlayerCarrier, PlayerCarrier
from util import LoggingLevelRouter


class PlayerValidator(ModelValidator[Player]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerCarrier is safe to use.

    Attributes:
        toolkit: PlayerValidatorToolkit

    Provides:
        -   def execute(candidate: PlayerValidationRequest) ->ValidationResult[PlayerCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[PlayerValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[PlayerValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or PlayerValidatorToolkit())
    
    @property
    def toolkit(self) -> PlayerValidatorToolkit:
        return cast(
            PlayerValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[PlayerCarrier]:
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
            candidate: Any
        Returns:
            ValidationResult[PlayerCarrier]
        Raises:
            PlayerValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.wrapper.priming_validator.execute(
            candidate=candidate,
            target_model=PlayerValidationRequest,
            null_exception=PlayerValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorException.MSG,
                    err_code=PlayerValidatorException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result into a request for additional tests. ---#
        request = cast(PlayerValidationRequest, priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.wrapper.priming_validator.execute(
            candidate=request.item,
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
        if isinstance(carrier, HumanPlayerCarrier):
            helper = HumanPlayerValidator()
            return helper.execute(validated_carrier=carrier)
        helper = MachinePlayerValidator()
        return helper.execute(validated_carrier=cast(MachinePlayerCarrier, carrier))

    
    