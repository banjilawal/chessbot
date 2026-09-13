# src/assurance/validator/model/rank/knight/validator.py

"""
Module: assurance.validator.model.rank.knight.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import RankValidatorToolkit
from domain import knight, knightBlueprint, Persona
from err import knightCarrierEmptyException, knightValidatorException, PersonaNullException, WrongPersonaException
from transit import knightCarrier
from util import LoggingLevelRouter


class knightValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a RankCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: RankValidationToolkit

    Provides:
        -   def execute(validated_carrier: knightCarrier) -> ValidationResult[knightCarrier]

    Super Class:
    """
    _toolkit: RankValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[RankValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[RankValidationToolkit]
        """
        self._toolkit=toolkit or RankValidatorToolkit()
    
    @LoggingLevelRouter.monitor
    def execute(self, validated_carrier: knightCarrier) -> ValidationResult[knightCarrier]:
        """
        Send a validated knight or Blueprint which inside the validated
        knightCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The carrier is empty.
                    - The id check fails.
                    - The team check fails.
                    - The persona is null or the wrong type.
                    - The readiness is null or the wrong type.
                    - the deployment is null or the wrong type.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            validated_carrier: knightCarrier
        Returns:
            ValidationResult[knightCarrier]
        Raises:
            knightValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                knightValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=knightValidatorException.MSG,
                    err_code=knightValidatorException.ERR_CODE,
                    ex=knightCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=knightCarrierEmptyException.MSG,
                        err_code=knightCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the persona does not pass a validation check.
        persona_validation = self._toolkit.helper.priming_validator.execute(
            candidate=blueprint.persona,
            target_model=Persona,
            null_exception=PersonaNullException(),
        )
        if persona_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                knightValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=knightValidatorException.MSG,
                    err_code=knightValidatorException.ERR_CODE,
                    ex=persona_validation.exception,
                )
            )
        # Handle the case that the Persona is not a knight's.
        persona = cast(Persona, persona_validation.payload)
        if persona != Persona.knight:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                knightValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=knightValidatorException.MSG,
                    err_code=knightValidatorException.ERR_CODE,
                    ex=WrongPersonaException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=WrongPersonaException.MSG,
                        err_code=WrongPersonaException.ERR_CODE,
                    ),
                )
            )

        # --- Forward the appropriate work product to the caller. ---#
        
        # The model case.
        if validated_carrier.is_carrying_model:
            model = knight(persona=persona)
            return ValidationResult.success(knightCarrier(model=model))
        # Else the blueprint case
        return ValidationResult.success(
            knightCarrier(
                blueprint=knightBlueprint(persona=persona)
            )
        )
    
    