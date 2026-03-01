# src/chess/edge/context/service/servicepy

"""
Module: chess.edge.context.service.service
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from chess.system import ContextService, id_emitter
from chess.edge import EdgeContext, EdgeContextBuilder, EdgeContextValidator, EdgeFinder


class EdgeContextService(ContextService[EdgeContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Edge search microservice API.
    2.  Provides a map aware utility for searching Edge objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Edge search results by having single entry and exit points for the
        Edge search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   EdgeContextService

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    SERVICE_NAME = "EdgeContextService"
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            finder: EdgeFinder = EdgeFinder(),
            builder: EdgeContextBuilder = EdgeContextBuilder(),
            validator: EdgeContextValidator = EdgeContextValidator(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   finder (EdgeFinder)
            *   builder (EdgeContextBuilder)
            *   validator (EdgeContextValidator)
        # RETURNS:
            None
        # RAISES:
            None
        """
        method = "EdgeContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> EdgeFinder:
        """Get EdgeFinder instance."""
        return cast(EdgeFinder, self.entity_finder)
    
    @property
    def builder(self) -> EdgeContextBuilder:
        """Get EdgeContextBuilder instance."""
        return cast(EdgeContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> EdgeContextValidator:
        """Get EdgeContextValidator instance."""
        return cast(EdgeContextValidator, self.entity_validator)