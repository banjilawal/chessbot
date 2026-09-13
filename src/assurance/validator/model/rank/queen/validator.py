# src/assurance/validator/model/rank/queen/validator.py

"""
Module: assurance.validator.model.rank.queen.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import RankValidatorToolkit
from domain import Queen, QueenBlueprint, Persona
from err import QueenCarrierEmptyException, QueenValidatorException, PersonaNullException, WrongPersonaException
from transit import QueenCarrier
from util import LoggingLevelRouter


class QueenValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a RankCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: RankValidationToolkit

    Provides:
        -   def execute(validated_carrier: QueenCarrier) -> ValidationResult[QueenCarrier]

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
    def execute(self, validated_carrier: QueenCarrier) -> ValidationResult[QueenCarrier]:
        """
        Send a validated Queen or Blueprint which inside the validated
        QueenCarrier.

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
            validated_carrier: QueenCarrier
        Returns:
            ValidationResult[QueenCarrier]
        Raises:
            QueenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that there is no blueprint in the carrier.
        blueprint = validated_carrier.extract_blueprint()
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QueenValidatorException.MSG,
                    err_code=QueenValidatorException.ERR_CODE,
                    ex=QueenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=QueenCarrierEmptyException.MSG,
                        err_code=QueenCarrierEmptyException.ERR_CODE,
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
                QueenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QueenValidatorException.MSG,
                    err_code=QueenValidatorException.ERR_CODE,
                    ex=persona_validation.exception,
                )
            )
        # Handle the case that the Persona is not a Queen's.
        persona = cast(Persona, persona_validation.payload)
        if persona != Persona.QUEEN:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                QueenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QueenValidatorException.MSG,
                    err_code=QueenValidatorException.ERR_CODE,
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
            model = Queen(persona=persona)
            return ValidationResult.success(QueenCarrier(model=model))
        # Else the blueprint case
        return ValidationResult.success(
            QueenCarrier(
                blueprint=QueenBlueprint(persona=persona)
            )
        )
    
    