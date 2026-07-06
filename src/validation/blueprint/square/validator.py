# src/validation/blueprint/square/validator.py

"""
Module: validation.blueprint.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Formation, SquareBlueprint, SquareState
from result import ValidationResult
from toolkit import SquareBlueprintToolkit
from util import LoggingLevelRouter
from validation import BlueprintValidator
from err import (
    FormationNullException, SquareBlueprintValidationException, SquareBlueprintValidationRouteException,
    SquareStateNullException
)



class SquareBlueprintValidator(BlueprintValidator[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a SquareBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: SquareBlueprintToolkit,
            ) -> ValidationResult[Square]:

    Super Class:
        BlueprintValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: SquareBlueprintToolkit | None = None,
    ) -> ValidationResult[Square]:
        """
        Certify a candidate is a SquareBlueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Validation is not primed.
                    -   The enabled attribute fails a safety check.
                    -   There is no validation path for the attribute.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any,
            toolkit: SquareBlueprintToolkit,
        Returns:
            ValidationResult[Square]
        Raises:
            SquareBlueprintValidationException
            SquareBlueprintValidationRouteException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = SquareBlueprintToolkit()
        
        # handle the case that, priming the validator fails.
        priming_result = toolkit.blueprint_priming_validator.build(
            candidate=candidate,
            blueprint_model=toolkit.blueprint_model_type,
            blueprint_null_exception=toolkit.null_blueprint_exception,
            priming_validator=toolkit.square_toolkit.priming_validator
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareBlueprintValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareBlueprintValidationException.MSG,
                    err_code=SquareBlueprintValidationException.ERR_CODE,
                    ex=priming_result.exception
                )
            )
        # --- Cast the candidate into SquareBlueprint for routing attribute testing. ---#
        blueprint = cast(SquareBlueprint, candidate)
        
        # Certification for the search-by-id target.
        if blueprint.id is not None:
            validation_result = toolkit.square_toolkit.identity_service.validate_id(
                candidate=blueprint.id
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-schema target.
        if blueprint.name is not None:
            validation_result = toolkit.square_toolkit.identity_service.validate_name(
                candidate=blueprint.name
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-coord target.
        if blueprint.coord is not None:
            validation_result = toolkit.square_toolkit.coord_validator.execute(
                candidate=blueprint.coord
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-board target.
        if blueprint.board is not None:
            validation_result = toolkit.square_toolkit.board_validator.execute(
                candidate=blueprint.board
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-occupant target.
        if blueprint.occupant is not None:
            validation_result = toolkit.square_toolkit.token_validator.execute(
                candidate=blueprint.occupant
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-state.
        if blueprint.state is not None:
            validation_result = toolkit.square_toolkit.priming_validator.execute(
                candidate=blueprint.state,
                model_type=SquareState,
                null_exception=SquareStateNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Certification for the search-by-formation.
        if blueprint.formation is not None:
            validation_result = toolkit.square_toolkit.priming_validator.execute(
                candidate=blueprint.formation,
                model_type=Formation,
                null_exception=FormationNullException()
            )
            if validation_result.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    SquareBlueprintValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=SquareBlueprintValidationException.MSG,
                        err_code=SquareBlueprintValidationException.ERR_CODE,
                        ex=validation_result.exception
                    )
                )
            # On validation success forward the work product to the caller.
            return ValidationResult.success(blueprint)
        
        # Return the exception chain if there is no validation route for the blueprint.
        return ValidationResult.failure(
            SquareBlueprintValidationException(
                cls_mthd=method,
                cls_name=cls.__name__,
                msg=SquareBlueprintValidationException.MSG,
                err_code=SquareBlueprintValidationException.ERR_CODE,
                ex=SquareBlueprintValidationRouteException(
                    msg=SquareBlueprintValidationRouteException.MSG,
                    err_code=SquareBlueprintValidationRouteException.ERR_CODE,
                )
            )
        )

