# src/microservice/identity/microservice.py

"""
Module: microservice.identity.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
import sys
from typing import Any, Dict, cast

from blueprint import Blueprint
from err import IdentityServiceException
from result import ValidationResult
from tester import BlueprintIdExtractor
from util import IdFactory, LoggingLevelRouter
from validator import NameValidator, NumberValidator


class IdentityService:
    """
        Role:
        -   API
        -   Lifecycle Manager
        -   Operations Provider
        -   Stateless microservice

    Responsibilities:
        1.  Bundles id, name verification, 

    Attributes:
        number_validator: NumberValidator
        name_validator: NameValidator
        blueprint_id_extractor: BlueprintIdExtractor

    Provides:
        -   next_id(cls, class_name: str) -> int
        -   validate_id(candidate: Any) -> ValidationResult
        -   validate_name(candidate: Any) -> ValidationResult:
        -   validate_blueprint_id(blueprint: Blueprint, model_name: str)-> ValidationResult

    Super Class:
    """
    _number_validator: NumberValidator
    _name_validator: NameValidator
    _blueprint_id_extractor: BlueprintIdExtractor
    
    def __init__(
            self,
            number_validator: NumberValidator | None = NumberValidator(),
            name_validator: NameValidator | None = NameValidator(),
            blueprint_id_extractor: BlueprintIdExtractor | None = BlueprintIdExtractor(),
    ):
        """
        Args:
            number_validator: NumberValidator
            name_validator: NameValidator
            blueprint_id_extractor: BlueprintIdExtractor
        """
        self._number_validator=number_validator
        self._name_validator=name_validator
        self._blueprint_id_extractor = blueprint_id_extractor
    
    @LoggingLevelRouter.monitor
    def next_id(self, class_name: str) -> int:
        return IdFactory.next_id(class_name=class_name)
      
    @LoggingLevelRouter.monitor
    def validate_id(self, candidate: Any) -> ValidationResult:
        method = f"{self.__class__.__name__}.validate_id"
        
        # Handle the case that, the id is not safe to use.
        validation_result = self._number_validator.execute(candidate)
        if validation_result.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward as the work product. ---#
        return ValidationResult.success(cast(int, candidate))
    
    @LoggingLevelRouter.monitor
    def validate_name(self, candidate: Any) -> ValidationResult:
        method = f"{self.__class__.__name__}.validate_name"
        
        # Handle the case that, the id is not safe to use.
        validation_result = self._name_validator.execute(candidate)
        if validation_result.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward as the work product. ---#
        return ValidationResult.success(cast(str, candidate))
    
    @LoggingLevelRouter.monitor
    def validate_blueprint_id(self, model_blueprint: Blueprint, model_name: str, ) -> ValidationResult:
        method = f"{self.__name__}.validate_blueprint_id"
        
        # Handle the case that, the class_name is flagged unsafe.
        validation_result = self._blueprint_id_extractor.execute(
            blueprint=model_blueprint,
            mol
        )
        if not class_name_validation_result.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        if id is not None:
            # Handle the case that, the id is flagged unsafe.
            id_validation_result = self._number_validator.execute(id)
            if not id_validation_result.is_failure:
                # Send the exception chain on failure.
                ValidationResult.failure(
                    IdentityValidatorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=IdentityValidatorException.MSG,
                        err_code=IdentityValidatorException.ERR_CODE,
                        ex=id_validation_result.exception
                    )
                )
            # --- Otherwise, directly forward the work product. ---#
            return id_validation_result
        
        # --- If the id was null create a new id then, forward as the work product. ---#
        return ValidationResult.success(IdFactory.next_id(class_name=model_name))

        
    @LoggingLevelRouter.monitor
    def validate_identity(
            self,
            id_candidate: Any,
            name_candidate: Any
    ) -> ValidationResult[Dict[str, Any]]:
        """
        Verify the name and id obey the rules.
        
        Action:
            1.  Send an exception chain in the ValidationResult if either
                candidate gets flagged.
            2.  Otherwise, send the success result.
        Args:
            id_candidate: Any
            name_candidate: Any
        Returns:
            ValidationResult[Dict[str, Any]]
        Raises:
            IdentityValidatorException
        """
        method = f"{self.__class__.__name__}.execute_identity"
        
        # Handle the case that, the id gets flagged.
        id_validation_result = self._number_validator.execute(
            candidate=id_candidate,
            floor=1,
            ceiling=sys.maxsize,
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityValidatorException.MSG,
                    err_code=IdentityValidatorException.ERR_CODE,
                    ex=id_validation_result.exception
                )
            )
        # Handle the case that, the name is flagged.
        name_validation_result = self._name_validator.execute(candidate=name_candidate)
        if name_validation_result.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityValidatorException.MSG,
                    err_code=IdentityValidatorException.ERR_CODE,
                    ex=name_validation_result.exception
                )
            )
        identity_dict = {
            "id": id_validation_result.payload,
            "name": name_validation_result.payload
        }
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(identity_dict)
