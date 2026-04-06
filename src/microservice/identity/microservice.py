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
from system import IdFactory


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
       
    @classmethod
    def next_id(cls, class_name: str) -> int:
        return IdFactory.next_id(class_name=class_name)
        
    def validate_id(self, candidate: Any) -> ValidationResult[int]:
        return self._number_validator.validate(candidate)
    
    def validate_name(self, candidate: Any) -> ValidationResult[str]:
        return self._name_validator.validate(candidate)
    
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
        id_validation_result = self._number_validator.validate(
            candidate=id_candidate,
            floor=1,
            ceiling=sys.maxsize,
        )
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
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
        name_validation_result = self._name_validator.validate(candidate=name_candidate)
        if name_validation_result.is_failure:
            # Return the exception chain on failure.
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
