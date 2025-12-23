# src/chess/schema/key/service/service.py

"""
Module: chess.schema.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast


from chess.system import ContextService, id_emitter
from chess.schema import SchemaLookup, SchemaSuperKey, SchemaSuperKeyBuilder, SchemaSuperKeyValidator


class SchemaSuperKeyService(ContextService[SchemaSuperKey]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing SchemaSuperKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for SchemaSuperKey state.
    4.  Single entry and entry points to SchemaSuperKey lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
    """
    SERVICE_NAME = "SchemaSuperKeyService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: SchemaLookup = SchemaLookup(),
            builder: SchemaSuperKeyBuilder = SchemaSuperKeyBuilder(),
            validator: SchemaSuperKeyValidator = SchemaSuperKeyValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SchemaSuperKeyBuilder)
            *   validator (SchemaSuperKeyValidator)

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
        
    @property
    def builder(self) -> SchemaSuperKeyBuilder:
        """get SchemaSuperKeyBuilder"""
        return cast(SchemaSuperKeyBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SchemaSuperKeyValidator:
        """get SchemaSuperKeyValidator"""
        return cast(SchemaSuperKeyValidator, self.entity_validator)
    
    @property
    def lookup(self) -> SchemaLookup:
        return cast(SchemaLookup, self.entity_finder)