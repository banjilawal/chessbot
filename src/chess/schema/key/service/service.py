# src/chess/schema/key/service/service.py

"""
Module: chess.schema.key.service.service
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""
from typing import cast


from chess.system import ContextService, id_emitter
from chess.schema import SchemaLookup, SchemaKey, SchemaKeyBuilder, SchemaKeyValidator


class SchemaKeyService(ContextService[SchemaKey]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing SchemaKey microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for SchemaKey state.
    4.  Single entry and entry points to SchemaKey lifecycle.

    # PARENT:
        *   ContextService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "SchemaKeyService"
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: SchemaLookup = SchemaLookup(),
            builder: SchemaKeyBuilder = SchemaKeyBuilder(),
            validator: SchemaKeyValidator = SchemaKeyValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (SchemaKeyBuilder)
            *   validator (SchemaKeyValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=lookup)
        
    @property
    def builder(self) -> SchemaKeyBuilder:
        """get SchemaKeyBuilder"""
        return cast(SchemaKeyBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SchemaKeyValidator:
        """get SchemaKeyValidator"""
        return cast(SchemaKeyValidator, self.entity_validator)
    
    @property
    def lookup(self) -> SchemaLookup:
        return cast(SchemaLookup, self.entity_finder)