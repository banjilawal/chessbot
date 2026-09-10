# src/microservice/identity/microservice.py

"""
Module: microservice.identity.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import NameValidator, NumberValidator
from authorization import BlueprintIdExtractor
from domain import Blueprint, IdentityRegister
from err import IdentityServiceException
from util import IdFactory, LoggingLevelRouter


class IdentityService:
    """
        Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless microservice

    Responsibilities:
        1.  Bundles id, name verification, 

    Attributes:
        name_validator: NameValidator
        number_validator: NumberValidator

    Provides:
        - next_id(cls, class_name: str) -> int
        - validate_id(candidate: Any) -> ValidationResult
        - validate_name(candidate: Any) -> ValidationResult:

    Super Class:
    """
    _name_validator: NameValidator
    _number_validator: NumberValidator
    
    def __init__(
            self,
            name_validator: Optional[NameValidator] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            blueprint_id_extractor: Optional[BlueprintIdExtractor] | None = None,
    ):
        """
        Args:
            name_validator: Optional[NameValidator] | None = None,
            number_validator: Optional[NumberValidator] | None = None,
            blueprint_id_extractor: Optional[BlueprintIdExtractor
        """
        self._name_validator=name_validator or NameValidator()
        self._number_validator = number_validator or NumberValidator()
        self._blueprint_id_extractor = blueprint_id_extractor or BlueprintIdExtractor()
    
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
    def validate_id(self, candidate: Any) -> ValidationResult[int]:
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
        
        # Handle the case that the id is not safe to use.
        validation = self._number_validator.execute(candidate)
        if validation.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=validation.exception
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
        
        # Handle the case that the id is not safe to use.
        validation = self._name_validator.execute(candidate)
        if validation.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=validation.exception
                )
            )
        # --- Forward the work product. ---#
        return ValidationResult.success(cast(str, candidate))
    
    @LoggingLevelRouter.monitor
    def validate_blueprint_id(
            self,
            owner_blueprint: Blueprint,
            owner_name: str,
    ) -> ValidationResult:
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
        
        # Handle the case that the class_name is flagged unsafe.
        name_validation = self._name_validator.execute(
            candidate=owner_blueprint.domain_class_name,
        )
        if name_validation.is_failure:
            # Send the exception chain in the result.
            return ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=name_validation.exception
                )
            )
        # --- Otherwise, directly forward the work product. ---#
        return validation

        
    @LoggingLevelRouter.monitor
    def validate_identity(self, id_candidate: Any, name_candidate: Any) -> ValidationResult:
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
        
        # Handle the case that the id gets flagged.
        id_validation = self.validate_id(candidate=id_candidate)
        if id_validation.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=id_validation.exception
                )
            )
        id = cast(int, id_validation.payload)
        name_validation = self.validate_name(candidate=name_candidate)
        if name_validation.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityServiceException.MSG,
                    err_code=IdentityServiceException.ERR_CODE,
                    ex=name_validation.exception
                )
            )
        name = cast(str, name_validation.payload)
        identity_register = IdentityRegister(id=id, name=name)
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(identity_register)
