# src/logic/owner/service/transaction.py

"""
Module: logic.owner.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from logic.system import QueryService, id_emitter
from logic.agent import AgentContext, AgentContextBuilder, AgentContextValidator, AgentFinder


class AgentQueryService(QueryService[AgentContext]):
    """
    Role:Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facing Player search microservice API.
    2.  Provides a map aware utility for searching Player objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for Player search results by having single entry and exit points for the
        Player search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *   build:    -> AgentContextBuildProcess
        *   validation:  -> AgentContextValidator
        *   route:     -> AgentFinder


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    DEFAULT_NAME = "PlayerQueryService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder:AgentFinder = AgentFinder(),
            builder: AgentContextBuilder = AgentContextBuilder(),
            validator: AgentContextValidator = AgentContextValidator(),
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   name (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   route (AgentFinder): Default value - AgentFinder()
            *   build (AgentContextBuildProcess): Default value - AgentContextBuildProcess()
            *   validation (AgentContextValidator): Default value - AgentContextValidator()

        # RETURNS:
        None

        Raises:
        """
        method = "PlayerQueryService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
        
    @property
    def finder(self) -> AgentFinder:
        """Get AgentFinder instance."""
        return cast(AgentFinder, self.entity_finder)
    
    @property
    def build(self) -> AgentContextBuilder:
        """Get AgentContextBuildProcess instance."""
        return cast(AgentContextBuilder, self.entity_builder)
    
    @property
    def validation(self) -> AgentContextValidator:
        """Get AgentContextValidator instance."""
        return cast(AgentContextValidator, self.entity_validator)