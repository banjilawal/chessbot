# src/consistency/maneuver/consistency.py

"""
Module: consistency.maneuver.consistency
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import ManeuverConsistencyException
from model import Maneuver
from result import ValidationResult
from toolkit import ManeuverToolkit
from util import LoggingLevelRouter


class ManeuverConsistency:
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
        Consistency
    """
    OPERATION_NAME = "maneuver_consistency"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def consistencyChecker(
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
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: ManeuverToolkit
        Returns:
            ValidationResult[int]
        Raises:
            ManeuverConsistencyException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = ManeuverToolkit()
        
        # Handle the case that, the consistency is not primed.
        consistency_priming_result = toolkit.priming_consistency.execute(
            candidate=candidate,
            target_model=toolkit.model,
            null_exception=toolkit.null_exception,
        )
        if consistency_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverConsistencyException.MSG,
                    err_code=ManeuverConsistencyException.ERR_CODE,
                    ex=consistency_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Maneuver for additional tests. ---#
        maneuver = cast(Maneuver, candidate)
        
        # Handle the case that, the path is not safe.
        path_validation_result = toolkit.path_consistency.execute(maneuver.path)
        if path_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverConsistencyException.MSG,
                    err_code=ManeuverConsistencyException.ERR_CODE,
                    ex=path_validation_result.exception,
                )
            )
        # Handle the case that, the token is not safe.
        token_validation_result = toolkit.token_consistency.execute(maneuver.path)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverConsistencyException.MSG,
                    err_code=ManeuverConsistencyException.ERR_CODE,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that, either the token is not at the origin or already at the destination.
        token_endpoint_relation_validation_result = toolkit.endpoint_consistency.execute(
            token=maneuver.token,
            origin=maneuver.path.origin,
            destination=maneuver.path.destination,
        )
        if token_endpoint_relation_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverConsistencyException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverConsistencyException.MSG,
                    err_code=ManeuverConsistencyException.ERR_CODE,
                    ex=token_endpoint_relation_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(maneuver)
        
        
