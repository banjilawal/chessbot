# src/checker/model/maneuver/checker.py

"""
Module: checker.model.maneuver.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import ManeuverCheckerException
from domain.model import Maneuver
from artifcat.result import ValidationResult
from operation.toolkit import ManeuverToolkit
from util import LoggingLevelRouter


class ManeuverIntegrityChecker(ModelIntegrityChecker[Maneuver]):
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
                    bundle: ManeuverToolkit,
            ) -> ValidationResult[Maneuver]:

    Super Class:
        ModelChecker
    """
    
    def __init__(self, bundle: ManeuverToolkit | None = ManeuverToolkit()):
        """
        Args:
            bundle: ManeuverToolkit
        """
        super().__init__(bundle=bundle)
    
    @property
    def toolkit(self) -> ManeuverBundle:
        return cast(ManeuverToolkit, super().bundle)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any,) -> ValidationResult[Maneuver]:
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
            bundle: ManeuverToolkit
        Returns:
            ValidationResult[int]
        Raises:
            ManeuverCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if self.toolkit is None:
            toolkit = ManeuverToolkit()
        
        # Handle the case that, the checker is not primed.
        checker_priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=self.toolkit.model,
            null_exception=self.toolkit.null_exception,
        )
        if checker_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverCheckerException.MSG,
                    err_code=ManeuverCheckerException.ERR_CODE,
                    ex=checker_priming_result.exception,
                )
            )
        # --- Cast the candidate into a Maneuver for additional tests. ---#
        maneuver = cast(Maneuver, candidate)
        
        # Handle the case that, the path is not safe.
        path_validation_result = self.toolkit.path_checker.execute(maneuver.path)
        if path_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverCheckerException.MSG,
                    err_code=ManeuverCheckerException.ERR_CODE,
                    ex=path_validation_result.exception,
                )
            )
        # Handle the case that, the token is not safe.
        token_validation_result = self.toolkit.token_checker.execute(maneuver.path)
        if token_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverCheckerException.MSG,
                    err_code=ManeuverCheckerException.ERR_CODE,
                    ex=token_validation_result.exception,
                )
            )
        # Handle the case that, either the token is not at the origin or already at the destination.
        token_endpoint_relation_validation_result = self.toolkit.endpoint_checker.execute(
            token=maneuver.token,
            origin=maneuver.path.origin,
            destination=maneuver.path.destination,
        )
        if token_endpoint_relation_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverCheckerException.MSG,
                    err_code=ManeuverCheckerException.ERR_CODE,
                    ex=token_endpoint_relation_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(maneuver)
        
        
