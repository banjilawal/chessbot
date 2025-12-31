# src/chess/persona/key/service/service.py

"""
Module: chess.persona.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast

from chess.system import ContextService, id_emitter
from chess.persona import PersonaLookup, PersonaSuperKey, PersonaSuperKeyBuilder, PersonaSuperKeyValidator


class PersonaSuperKeyService(ContextService[PersonaSuperKey]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PersonaSuperKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for PersonaSuperKey state.
    4.  Single entry and entry points to PersonaSuperKey lifecycle.

    # PARENT:
        *   ContextService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "PersonaSuperKeyService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: PersonaLookup = PersonaLookup(),
            builder: PersonaSuperKeyBuilder = PersonaSuperKeyBuilder(),
            validator: PersonaSuperKeyValidator = PersonaSuperKeyValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (PersonaSuperKeyBuilder)
            *   validator (PersonaSuperKeyValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
    
    @property
    def builder(self) -> PersonaSuperKeyBuilder:
        """get PersonaSuperKeyBuilder"""
        return cast(PersonaSuperKeyBuilder, self.entity_builder)
    
    @property
    def validator(self) -> PersonaSuperKeyValidator:
        """get PersonaSuperKeyValidator"""
        return cast(PersonaSuperKeyValidator, self.entity_validator)
    
    @property
    def lookup(self) -> PersonaLookup:
        return cast(PersonaLookup, self.entity_finder)