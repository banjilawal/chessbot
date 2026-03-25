# src/logic/edge/query/service/servicepy

"""
Module: logic.edge.query.service.service
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from __future__ import annotations
from typing import cast

from logic.system import QueryService, id_emitter
from logic.edge import EdgeContext, EdgeContextBuildProcess, EdgeContextValidationProcess, EdgeFinder


class EdgeQueryService(QueryService[EdgeContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

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
            builder: EdgeContextBuildProcess = EdgeContextBuildProcess(),
            validator: EdgeContextValidationProcess = EdgeContextValidationProcess(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (str)
            *   id (int)
            *   route (EdgeFinder)
            *   build (EdgeContextBuildProcess)
            *   validation (EdgeContextValidationProcess)
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
    def build(self) -> EdgeContextBuildProcess:
        """Get EdgeContextBuildProcess instance."""
        return cast(EdgeContextBuildProcess, self.entity_builder)
    
    @property
    def validation(self) -> EdgeContextValidationProcess:
        """Get EdgeContextValidationProcess instance."""
        return cast(EdgeContextValidationProcess, self.entity_validator)