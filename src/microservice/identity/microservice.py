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
from model import IdentityRegister
from result import ValidationResult
from tester import BlueprintIdExtractor
from util import IdFactory, LoggingLevelRouter
from validator import IdentityRegisterCertifier, NameValidator, NumberValidator


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
        identity_register_certifier: IdentityRegisterCertifier

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
    _identity_register_certifier: IdentityRegisterCertifier
    
    def __init__(
            self,
            number_validator: NumberValidator | None = NumberValidator(),
            name_validator: NameValidator | None = NameValidator(),
            blueprint_id_extractor: BlueprintIdExtractor | None = BlueprintIdExtractor(),
            identity_register_certifier: IdentityRegisterCertifier | None = IdentityRegisterRootCertifier()
    ):
        """
        Args:
            number_validator: NumberValidator
            name_validator: NameValidator
            blueprint_id_extractor: BlueprintIdExtractor
            identity_register_certifier: IdentityRegisterCertifier
        """
        self._number_validator=number_validator
        self._name_validator=name_validator
        self._blueprint_id_extractor = blueprint_id_extractor
        self._identity_register_certifier = identity_register_certifier
    
    @LoggingLevelRouter.monitor
    def next_id(self, class_name: str) -> int:
        """
        Produce the unique id for the class.
        Args:
            class_name: str
        Returns:
            int
        Raises:
        """
        return IdFactory.next_id(class_name=class_name)
      
    @LoggingLevelRouter.monitor
    def validate_id(self, candidate: Any) -> ValidationResult:
        """
        Verify that an id is safe to use.
        Action:
            1.  Send and exception chain if candidate is not safe.
                Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            IdentityServiceException
        """
        method = f"{self.__class__.__name__}.execute_id"
        
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
        # --- Forward the work product. ---#
        return ValidationResult.success(cast(int, candidate))
    
    @LoggingLevelRouter.monitor
    def validate_name(self, candidate: Any) -> ValidationResult:
        """
        Verify that a name is safe to use.
        Action:
            1.  Send and exception chain if candidate is not safe.
                Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult
        Raises:
            IdentityServiceException
        """
        method = f"{self.__class__.__name__}.execute_name"
        
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
        # --- Forward the work product. ---#
        return ValidationResult.success(cast(str, candidate))
    
    @LoggingLevelRouter.monitor
    def validate_blueprint_id(self, owner_blueprint: Blueprint, owner_name: str, ) -> ValidationResult:
        """
        Verify that blueprint contains an id that's safe for its owning model.
        Action:
            1.  Send and exception chain if candidate is not safe.
                Otherwise, send the success result.
        Args:
            owner_blueprint: Blueprint
            owner_name: str
        Returns:
            ValidationResult
        Raises:
            IdentityServiceException
        """
        method = f"{self.__name__}.validate_blueprint_id"
        
        # Handle the case that, the class_name is flagged unsafe.
        validation_result = self._blueprint_id_extractor.execute(
            blueprint=owner_blueprint,
            model_name=owner_name,
        )
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
        # --- Otherwise, directly forward the work product. ---#
        return validation_result

        
    @LoggingLevelRouter.monitor
    def validate_identity_register(self, candidate: Any) -> ValidationResult:
        """
        Verify the name and id obey the rules.
        
        Action:
            1.  Send an exception chain in the ValidationResult if either
                candidate gets flagged.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[IdentityRegister]
        Raises:
            IdentityServiceException
        """
        method = f"{self.__class__.__name__}.validate_identity_register"
        
        # Handle the case that, the id gets flagged.
        validation_result = self._identity_register_certifier.execute(candidate=candidate)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(IdentityRegister, candidate))
