# src/chess/catalog/service/service.py

"""
Module: chess.catalog.service.service
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.catalog import CatalogContext, CatalogContextBuilder, PersonaSuperKeyValidator, CatalogLookup

class CatalogService(EntityService[CatalogContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Persona search microservice API.
    2.  Provides a map aware utility for searching Persona objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Persona search results by having single entry and exit points for the
        Persona search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "CatalogService"
    _lookup: CatalogLookup
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            lookup: CatalogLookup = CatalogLookup(),
            builder: CatalogContextBuilder = CatalogContextBuilder(),
            validator: PersonaSuperKeyValidator = PersonaSuperKeyValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   id (int)
            *   name (str)
            *   lookup (CatalogLookup)
            *   builder (CatalogContextBuilder)
            *   validator (PersonaSuperKeyValidator))

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._lookup = lookup
        
    @property
    def lookup(self) -> CatalogLookup:
        """Gets CatalogLookup instance."""
        return self._lookup
    
    @property
    def builder(self) -> CatalogContextBuilder:
        """Gets CatalogContextBuilder instance."""
        return cast(CatalogContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> PersonaSuperKeyValidator:
        """Gets PersonaSuperKeyValidator instance."""
        return cast(PersonaSuperKeyValidator, self.entity_validator)