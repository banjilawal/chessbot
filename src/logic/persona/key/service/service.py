# src/logic/persona/key/service/transaction.py

"""
Module: logic.persona.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast

from logic.system import QueryService, id_emitter
from logic.persona import PersonaLookupProcess, PersonaKey, PersonaKeyBuildTransaction, PersonaKeyValidationTransaction


class PersonaKeyService(QueryService[PersonaKey]):
    """
    Role:Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing PersonaKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PersonaKey state.
    4.  Single entry and entry points to PersonaKey lifecycle.

    Super Class:
        *   QueryService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "PersonaKeyService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: PersonaLookupProcess = PersonaLookupProcess(),
            builder: PersonaKeyBuildTransaction = PersonaKeyBuildTransaction(),
            validator: PersonaKeyValidationTransaction = PersonaKeyValidationTransaction(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   build (PersonaKeyBuildTransaction)
            *   validation (PersonaKeyValidationTransaction)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
    
    @property
    def build(self) -> PersonaKeyBuildTransaction:
        """get PersonaKeyBuildTransaction"""
        return cast(PersonaKeyBuildTransaction, self.entity_builder)
    
    @property
    def validation(self) -> PersonaKeyValidationTransaction:
        """get PersonaKeyValidationTransaction"""
        return cast(PersonaKeyValidationTransaction, self.entity_validator)
    
    @property
    def lookup(self) -> PersonaLookupProcess:
        return cast(PersonaLookupProcess, self.entity_finder)