# src/assurance/checker/model/coord/checker.py

"""
Module: assurance.checker.model.coord.checker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, cast

from err import CoordCheckerException
from domain.model import CoordBlueprint
from result import ValidationResult
from config.setting import BoardProperty
from operation.toolkit import CoordBlueprintToolkit
from util import LoggingLevelRouter


class CoordIntegrityChecker(ModelIntegrityChecker[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a CoordBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    bundle: CoordBlueprintToolkit,
            ) -> ValidationResult[Coord]:

    Super Class:
        IntegrityChecker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            bundle: CoordBlueprintToolkit | None = None,
    ) -> ValidationResult[Coord]:
        """
        Certify a candidate is a CoordBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            bundle: CoordBlueprintToolkit,
        Returns:
            ValidationResult[Coord]
        Raises:
            CoordCheckerException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = CoordBlueprintToolkit()
        
        # Handle the case that, the checker is not primed.
        priming_result = toolkit.blueprint_priming_validator.execute(
            candidate=candidate,
            blueprint_model=toolkit.blueprint_model_type,
            blueprint_null_exception=toolkit.null_blueprint_exception,
            checker_bootstrapper=toolkit.coord_toolkit.priming_validator
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordCheckerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=CoordCheckerException.MSG,
                    err_code=CoordCheckerException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareBlueprint for routing attribute testing. ---#
        blueprint = cast(CoordBlueprint, candidate)
        
        # Certification whichever attribute is enabled.
        for attribute in [blueprint.row, blueprint.column]:
            validation_result = toolkit.coord_toolkit.number_checker.execute(
                candidate=attribute,
                ceiling=BoardProperty.MAX_COLUMN_INDEX.value,
                floor=0,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CoordCheckerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CoordCheckerException.MSG,
                        err_code=CoordCheckerException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)

        



