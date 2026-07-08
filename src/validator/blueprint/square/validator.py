# src/validator/blueprint/square/validator.py

"""
Module: validator.blueprint.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from blueprint import SquareBlueprint
from err import SquareBlueprintValidatorException
from result import ValidationResult
from toolkit import SquareToolkit
from util import LoggingLevelRouter
from validator import BlueprintValidator


class SquareBlueprintValidator(BlueprintValidator[SquareBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SquareBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:
        toolkit: SquareToolkit

    Provides:
        -   execute(self, candidate: Any) -> ValidationResult:

    Super Class:
        BlueprintValidator
    """
    
    def __init__(self, toolkit: SquareToolkit | None = SquareToolkit()):
        """
        Args:
            toolkit: SquareToolkit
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> SquareToolkit:
        return cast(SquareToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Certify a candidate is a SquareBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The validation_priming fails.
                    -   Either the board, owner or id get flagged unsafe.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
        Returns:
            ValidationResult
        Raises:
            SquareBlueprintValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the validator is not primed.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            blueprint_model=self.toolkit.blueprint_model,
            blueprint_null_exception=self.toolkit.blueprint_null_exception,
            priming_validator=self.toolkit.priming_validator,
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBlueprintValidatorException.MSG,
                    err_code=SquareBlueprintValidatorException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareBlueprint for routing attribute testing. ---#
        blueprint = cast(SquareBlueprint, candidate)
        
        # Handle the case that, any id in the blueprint is flagged.
        id_validation_result = self.toolkit.blueprint_id_validator.execute(
            candidate=blueprint.id,
            identity_service=self.toolkit.identity_service,
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBlueprintValidatorException.MSG,
                    err_code=SquareBlueprintValidatorException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, square.coord is not safe.
        coord_validation_result = self.toolkit.coord_validator.execute(blueprint.coord)
        if coord_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBlueprintValidatorException.MSG,
                    err_code=SquareBlueprintValidatorException.ERR_CODE,
                    ex=coord_validation_result.exception,
                )
            )
        # Handle the case that, square.board does not pass a validation check.
        board_validator_result = self.toolkit.board_validator.execute(blueprint.board)
        if board_validator_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBlueprintValidatorException.MSG,
                    err_code=SquareBlueprintValidatorException.ERR_CODE,
                    ex=board_validator_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)