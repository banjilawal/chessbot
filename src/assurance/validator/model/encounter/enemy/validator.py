# src/assurance/validator/model/encounter/enemy/validator.py

"""
Module: assurance.validator.model.encounter.enemy.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Encounter
from err import EncounterEnemyValidatorException
from exchange import EncounterValidationRequest, EncounterValidationResponseWrapper
from util import LoggingLevelRouter


class EncounterEnemyValidator:
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a EncounterBlueprint enemy and previous_enemys fields
            are safe to use.

    Attributes:
        response_wrapper: EncounterValidationResponseWrapper

    Provides:
        -   def execute(
                    request: EncounterValidationRequest
            ) -> ValidationResult[Encounter]:

    Super Class:
    """
    _response_wrapper: EncounterValidationResponseWrapper
    
    def __init__(
            self,
            response_wrapper: Optional[EncounterValidationResponseWrapper]
                              | None = None,
    ):
        """
        Args:
            response_wrapper: Optional[EncounterValidationResponseWrapper]
        """
        self._response_wrapper = (
                response_wrapper or EncounterValidationResponseWrapper()
        )

    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: EncounterValidationRequest,
    ) -> ValidationResult[Encounter]:
        """
        Run a safety check on an enemy.

        Action:
            1.  Send an exception chain in the ValidationResult if
                the responder fails.
            2.  Otherwise, send the validated enemy in the
                success result.
        Args:
            request: EncounterValidationRequest
        Returns:
            ValidationResult[Encounter]
        Raises:
            EncounterEnemyValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the response is an unsafe Toke.
        result = self._response_wrapper.extract_model(
            request=request,
        )
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterEnemyValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterEnemyValidatorException.MSG,
                    err_code=EncounterEnemyValidatorException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Send the work product. ---#
        encounter = cast(Encounter, result.payload)
        return ValidationResult.success(encounter)
    