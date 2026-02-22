# src/chess/system/identity/service.py

"""
Module: chess.system.identity.service
Author: Banji Lawal
Created: 2025-11-13
version: 1.0.0
"""

from typing import Any

from chess.system import (
    IdFactory, IdValidator, NameValidator, ValidationResult, IdEmitter, InvalidIdentityException, id_emitter
)


class IdentityService:
    """
    # ROLE: Service, Validation, Data Integrity, ID Generation

    # RESPONSIBILITIES:
    1.  Issue IDs to new objects.
    2.  Manage integrity checks on IDs and names of existing objects.
    3.  Assure names are:
        *   Not validation.
        *   Not white space only (" ", tab, newline).
        *   Not empty. (".", ".\n", ".\t", ".\r").
        *   Meet minimum length requirement specified in chess.syst.
        *   Meet maximum length requirement specified in class.

    # PROVIDES:
        *   IdEmitter
        *   IdValidator
        *   NameValidator


    # ATTRIBUTES:
        *   id_validator (type[IdValidator]):
        *   name_validator (type[NameValidator]):
        *   id_emitter (type[IdEmitter]):
    """
    _id_validator: IdValidator
    _name_validator: NameValidator
    
    def __init__(
            self,
            id_validator: IdValidator = IdValidator(),
            name_validator: NameValidator = NameValidator(),
    ):
        method = "IdentityService.__init__"
        self._id_validator=id_validator
        self._name_validator=name_validator
       
    @classmethod
    def next_id(cls, class_name: str) -> int:
        return IdFactory.next_id(class_name=class_name)
        
    def validate_id(self, candidate: Any) -> ValidationResult[int]:
        return self._id_validator.validate(candidate)
    
    def validate_name(self, candidate: Any) -> ValidationResult[str]:
        method = "IdentityService.validate_name"
        return self._name_validator.validate(candidate)
    
    def validate_identity(
            self,
            id_candidate: Any,
            name_candidate: Any
    ) -> ValidationResult[(int, str)]:
        """
        # ACTION:
        1.  IdentityService directs id_validator verify the id_candidate.
        2.  name_validator verifies the name_candidate.
        3.  If any checks fail their exception is sent to the caller inside a ValidationResult.
        4.  On success
                *   cast name_candidate to a STRING.
                *   cast id_candidate to an INT.
                *   send the (id, designation) tuple to the caller in a ValidationResult.

        # PARAMETERS:
            * id_candidate (Any): object to certify is a legal ID.
            * name_candidate (Any): object to certify is a legal designation.

        # RETURNS:
        ValidationResult[tuple(int, str)] containing either:
            - On success: tuple(int, str) in the payload.
            - On failure: Exception.

        # RAISES:
            *   InvalidIdentityException
        """
        method = "IdentityService.validate_identity"
        try:
            id_validation = self._id_validator.validate(id_candidate)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            id = id_validation.payload
            
            name_validation = self._name_validator.validate(name_candidate)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            name = name_validation.payload
            
            return ValidationResult.success(payload=(id, name))
        except Exception as ex:
            return ValidationResult.failure(
                InvalidIdentityException(ex=ex, message=f"{method}: {InvalidIdentityException.DEFAULT_MESSAGE}")
            )