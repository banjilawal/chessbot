# src/validation/maneuver/validator.py

"""
Module: validation.maneuver.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import ManeuverValidatorException
from model import Maneuver
from result import ValidationResult
from toolkit import ManeuverToolkit
from util import LoggingLevelRouter


class ManeuverValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a Maneuver instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: ManeuverToolkit,
            ) -> ValidationResult[Maneuver]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "maneuver_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validator(
            cls,
            candidate: Any,
            toolkit: ManeuverToolkit | None,
    ) -> ValidationResult[Maneuver]:
        """
        Verify there is consistency between the itinerary's elements.

        Action:
            1.  Send an exception chan in the validation result if any of the following occur:
                    -   The candidate is either null or the wrong type.
                    -   The maneuver's token in not valid.
                    -   The maneuver's path gets flagged.
                    -   The token is not at the origin.
                    -   The destination contains the token.
                    -   There is token-destination inconsistency.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: ManeuverToolkit
        Returns:
            ValidationResult[int]
        Raises:
            ManeuverValidatorException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ManeuverToolkit()
        
        # Handle the case that, the candidate fails an initial check.
        priming_validation_result = toolkit.priming_validator.validate(
            candidate=candidate,
            target_model=toolkit.model,
            null_exception=toolkit.null_exception,
        )
        if priming_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=priming_validation_result.exception,
                )
            )
        # --- Cast the candidate into a Maneuver for additional tests. ---#
        maneuver = cast(Maneuver, candidate)
        
        # Handle the case that, the path is not safe.
        path_validation_result = toolkit.path_validator.validate(maneuver.path)
        if path_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=path_validation_result.exception,
                )
            )
        # Handle the case that, the token is not safe.
        token_validation_result = toolkit.token_validator.validate(maneuver.path)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that, the token is not at the path's origin.
        origin_relation_validation_result = toolkit.origin_relation_validator.validate(
            token=maneuver.token,
            origin=maneuver.path.origin,
        )
        if origin_relation_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=origin_relation_validation_result.exception,
                )
            )
        # Handle the case that, the token is already at the path's destination.
        destination_relation_validation_result = toolkit.destination_relation_validator.validate(
            token=maneuver.token,
            destination=maneuver.path.destination,
        )
        if origin_relation_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ManeuverValidatorException.MSG,
                    err_code=ManeuverValidatorException.ERR_CODE,
                    ex=destination_relation_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(maneuver)
        
        
