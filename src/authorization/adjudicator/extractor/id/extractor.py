# src/authorization/adjudicator/extractor/id/extractor.py

"""
Module: authorization.adjudicator.extractor.id.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import PrimingValidator
from domain import StateModelBlueprint
from err import BlueprintIdExctractorException, BlueprintNullException
from microservice import IdentityService
from util import IdFactory, LoggingLevelRouter


class BlueprintIdExtractor:
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Process Runner

    Responsibilities:
        1.  Validate a Blueprint's id if one is present. Otherwise, generate a unique one for
            the Blueprint's class.

    Attributes:
        priming_validator: IdetntiyService
        
    Provides:
        - execute(candidate: Any, model_name: str) -> ValidationResult:

    Super Class:
        Adjudicator
    """
    _identity_service: IdentityService
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            identity_service: Optional[IdentityService] | None = None,
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        self._identity_service = identity_service or IdentityService()
        self._priming_validator = priming_validator or PrimingValidator()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            blueprint_owner_name: str,
            blueprint_type: Type[StateModelBlueprint],
            blueprint_null_exception: BlueprintNullException,
    ) -> ValidationResult[int]:
        """
        Verify the id if it already exists or create a new one.

        Action:
            1.  If the candidate is not null:
                    - Send an exception chain in the ValidationResult when its not an int.
                    - Otherwise, send the success result.
            2.  If the candidate is null:
                    - Send an exception chain in the ValidationResult if the model_name is not a string.
                    - Otherwise, generate a unique id for the next model instance.
        Args:
            candidate: Any
            blueprint_owner_name: str
            blueprint_type: Type[Blueprint]
            blueprint_null_exception: BlueprintNullException
        Returns:
            ValidationResult[int]
        Raises:
            BlueprintIdExtractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        priming = self._priming_validator.execute(
            candidate=candidate,
            target_model=blueprint_type,
            null_exception=blueprint_null_exception,
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintIdExctractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintIdExctractorException.MSG,
                    err_code=BlueprintIdExctractorException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        blueprint = cast(Type[blueprint_type], priming.payload)
        if not isinstance(blueprint, StateModelBlueprint):
            return ValidationResult.failure(
                BlueprintIdExctractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintIdExctractorException.MSG,
                    err_code=BlueprintIdExctractorException.ERR_CODE,
                    ex=TypeError(
                        f"{blueprint.__class__.__name__} is not a StateModelBlueprint "
                        f" It does not have an id property to extract and validate."
                    ),
                )
            )
        state_blueprint = cast(StateModelBlueprint, blueprint)
        candidate_id = state_blueprint.id
        
        # --- If the candidate_id is null send a new one to the caller. ---#
        if candidate_id is None:
            id = IdFactory.next_id(class_name=blueprint_owner_name)
            return ValidationResult.success(id)
        
        # --- Otherwise, process the existing id. ---#
        validation = self._identity_service.validate_id(candidate_id)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintIdExctractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintIdExctractorException.MSG,
                    err_code=BlueprintIdExctractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        id = cast(int, validation.payload)
        return ValidationResult.success(id)


        

