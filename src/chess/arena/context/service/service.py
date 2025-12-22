# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import ContextService, id_emitter
from chess.agent import AgentContext, AgentContextBuilder, AgentContextValidator, AgentFinder


class AgentContextService(ContextService[AgentContext]):
    """
    # ROLE: Search Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing PlayerAgent search microservice API.
    2.  Provides a map aware utility for searching PlayerAgent objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth for PlayerAgent search results by having single entry and exit points for the
        PlayerAgent search flow.

    # PARENT:
        *   ContextService

    # PROVIDES:
        *   builder:    -> AgentContextBuilder
        *   validator:  -> AgentContextValidator
        *   finder:     -> AgentFinder

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ContextService for inherited attributes.
    """
    DEFAULT_NAME = "AgentContextService"
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            finder:AgentFinder = AgentFinder(),
            builder: AgentContextBuilder = AgentContextBuilder(),
            validator: AgentContextValidator = AgentContextValidator(),
    ):
        """
        # Action:
        Constructor

        # Parameters:
            *   designation (str): Default value - SERVICE_NAME
            *   id (int): Default value - id_emitter.service_id
            *   finder (AgentFinder): Default value - AgentFinder()
            *   builder (AgentContextBuilder): Default value - AgentContextBuilder()
            *   validator (AgentContextValidator): Default value - AgentContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "AgentContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator, finder=finder)
        
    @property
    def finder(self) -> AgentFinder:
        """Get AgentFinder instance."""
        return cast(AgentFinder, self.entity_finder)
    
    @property
    def builder(self) -> AgentContextBuilder:
        """Get AgentContextBuilder instance."""
        return cast(AgentContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> AgentContextValidator:
        """Get AgentContextValidator instance."""
        return cast(AgentContextValidator, self.entity_validator)