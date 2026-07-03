# src/microservice/identity/microservice.py

"""
Module: microservice.identity.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
import sys
from typing import Any, Dict

from err import IdentityValidationException
from integrity import NameValidator, NumberValidator
from result import ValidationResult
from system import IdFactory, LoggingLevelRouter


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

    Provides:
        -   def next_id(cls, class_name: str) -> int
        -   def validate_id(candidate: Any) -> ValidationResult[int]
        -   def validate_name(candidate: Any) -> ValidationResult[str]:

        -   def validate_identity(
                id_candidate: Any,
                name_candidate: Any
            ) -> ValidationResult[Dict[str, Any]]:6127219800

    Super Class:
    """
    _number_validator: NumberValidator
    _name_validator: NameValidator
    
    def __init__(
            self,
            number_validator: NumberValidator = NumberValidator(),
            name_validator: NameValidator = NameValidator(),
    ):
        """
        Args:
            number_validator: NumberValidator
            name_validator: NameValidator
        """
        self._number_validator=number_validator
        self._name_validator=name_validator
    
    @LoggingLevelRouter.monitor
    def next_id(self, class_name: str) -> int:
        return IdFactory.next_id(class_name=class_name)
      
    @LoggingLevelRouter.monitor
    def validate_id(self, candidate: Any) -> ValidationResult[int]:
        return self._number_validator.build(candidate)
    
    @LoggingLevelRouter.monitor
    def validate_name(self, candidate: Any) -> ValidationResult[str]:
        return self._name_validator.build(candidate)
    
    @LoggingLevelRouter.monitor
    def verify_bootstrap_id( self, id: Any, class_name: str,) -> ValidationResult[int]:
        """
        """
        method = f"{self.__name__}._verify_bootstrap_id"
        
        # Handle the case that, the class_name is flagged unsafe.
        class_name_validation_result = self._name_validator.build(
            candidate=class_name
        )
        if not class_name_validation_result.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityValidationException.MSG,
                    err_code=IdentityValidationException.ERR_CODE,
                    ex=class_name_validation_result.exception
                )
            )
        if id is not None:
            # Handle the case that, the id is flagged unsafe.
            id_validation_result = self._number_validator.build(id)
            if not id_validation_result.is_failure:
                # Send the exception chain on failure.
                ValidationResult.failure(
                    IdentityValidationException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=IdentityValidationException.MSG,
                        err_code=IdentityValidationException.ERR_CODE,
                        ex=id_validation_result.exception
                    )
                )
            # --- Otherwise, directly forward the work product. ---#
            return id_validation_result
        
        # --- If the id was null create a new id then, forward as the work product. ---#
        return ValidationResult.success(IdFactory.next_id(class_name=class_name))

        
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
            IdentityValidationException
        """
        method = f"{self.__class__.__name__}.validate_identity"
        
        # Handle the case that, the id gets flagged.
        id_validation_result = self._number_validator.build(
            candidate=id_candidate,
            floor=1,
            ceiling=sys.maxsize,
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityValidationException.MSG,
                    err_code=IdentityValidationException.ERR_CODE,
                    ex=id_validation_result.exception
                )
            )
        # Handle the case that, the name is flagged.
        name_validation_result = self._name_validator.build(candidate=name_candidate)
        if name_validation_result.is_failure:
            # Send the exception chain on failure.
            ValidationResult.failure(
                IdentityValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=IdentityValidationException.MSG,
                    err_code=IdentityValidationException.ERR_CODE,
                    ex=name_validation_result.exception
                )
            )
        identity_dict = {
            "id": id_validation_result.payload,
            "name": name_validation_result.payload
        }
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(identity_dict)
