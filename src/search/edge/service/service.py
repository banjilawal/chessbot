# src/logic/edge/context/service/servicepy

"""
Module: logic.edge.context.service.service
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from system import QueryService, id_emitter
from graph.edge import EdgeContext, EdgeContextBuilder, EdgeContextValidator, EdgeFinder


class EdgeQueryService(QueryService[EdgeContext]):
    """
    Role:Search Microservice, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Edge search microservice API.
    2.  Provides a map aware utility for searching Edge objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Edge search results by having single entry and exit points for the
        Edge search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   EdgeQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "EdgeQueryService"
    
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
            *   schema (str)
            *   id (int)
            *   route (EdgeFinder)
            *   build (EdgeContextBuilder)
            *   validation (EdgeContextValidator)
        # RETURNS:
            None
        Raises:
            None
        """
        method = "EdgeQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
    
    @property
    def finder(self) -> EdgeFinder:
        """Get EdgeFinder instance."""
        return cast(EdgeFinder, self.entity_finder)
    
    @property
    def build(self) -> EdgeContextBuilder:
        """Get EdgeContextBuilder instance."""
        return cast(EdgeContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> EdgeContextValidator:
        """Get EdgeContextValidator instance."""
        return cast(EdgeContextValidator, self.entity_validator)