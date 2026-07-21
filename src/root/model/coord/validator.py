# src/certifier/coord/validator.py

"""
Module: certifier.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import CoordCertifierException
from model import CoordBlueprint
from result import ValidationResult
from setting import BoardProperty
from toolkit import CoordBlueprintToolkit
from util import LoggingLevelRouter
from validator import Certifier


class CoordRootCertifier(RootCertifier[Coord]):
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
                    toolkit: CoordBlueprintToolkit,
            ) -> ValidationResult[Coord]:

    Super Class:
        Certifier
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: CoordBlueprintToolkit | None = None,
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
            toolkit: CoordBlueprintToolkit,
        Returns:
            ValidationResult[Coord]
        Raises:
            CoordCertifierException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = CoordBlueprintToolkit()
        
        # Handle the case that, the validator is not primed.
        priming_result = toolkit.blueprint_priming_validator.execute(
            candidate=candidate,
            blueprint_model=toolkit.blueprint_model_type,
            blueprint_null_exception=toolkit.null_blueprint_exception,
            validator_bootstrapper=toolkit.coord_toolkit.priming_validator
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordCertifierException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=CoordCertifierException.MSG,
                    err_code=CoordCertifierException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareBlueprint for routing attribute testing. ---#
        blueprint = cast(CoordBlueprint, candidate)
        
        # Certification whichever attribute is enabled.
        for attribute in [blueprint.row, blueprint.column]:
            validation_result = toolkit.coord_toolkit.number_validator.execute(
                candidate=attribute,
                ceiling=BoardProperty.MAX_COLUMN_INDEX.value,
                floor=0,
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    CoordCertifierException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=CoordCertifierException.MSG,
                        err_code=CoordCertifierException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)

        



