# src/transit/dispatcher/validator/model/maneuver/validator.py

"""
Module: transit.dispatcher.validator.model.maneuver.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import ManeuverValidatorException
from domain.model import Maneuver
from assurance import ManeuverValidator
from artifcat import ValidationResult
from assurance import ManeuverValidator
from util import LoggingLevelRouter


class ManeuverValidator:
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a Maneuver instance is certified safe, reliable, and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    validator: ManeuverValidator,
            ) -> ValidationResult[Maneuver]:

    Super Class:
        ModelValidator
    """
    def __init__(self, validator: ManeuverValidator):
        super().__init__(validator=validator)
    

    @LoggingLevelRouter.monitor
    def validator(self, candidate: Any,) -> ValidationResult[Maneuver]:
        """
        Verify there is consistency between the itinerary's elements.

        Action:
            1.  Send an exception chan in the validation result if any of the following occur:
                    - The candidate is either null or the wrong type.
                    - The maneuver's token in not valid.
                    - The maneuver's path gets flagged.
                    - The token is not at the origin.
                    - The destination contains the token.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            validator: ManeuverValidator
        Returns:
            ValidationResult[int]
        Raises:
            ManeuverValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if validator is None:
            validator = ManeuverValidator()
        
        # Handle the case that the validator is not primed.
        validator_priming_result = validator.priming_validator.execute(
            candidate=candidate,
            target_model=validator.model,
            null_exception=validator.domain_null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Maneuver for additional tests. ---#
        maneuver = cast(Maneuver, candidate)
        
        # Handle the case that the path is not safe.
        path_validation_result = validator.path_validator.execute(maneuver.path)
        if path_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=path_validation_result.exception,
                )
            )
        # Handle the case that the token is not safe.
        token_validation_result = validator.token_validator.execute(maneuver.path)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that either the token is not at the origin or already at the destination.
        token_endpoint_relation_validation_result = validator.endpoint_validator.execute(
            token=maneuver.token,
            origin=maneuver.path.origin,
            destination=maneuver.path.destination,
        )
        if token_endpoint_relation_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=token_endpoint_relation_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(maneuver)
        
        
