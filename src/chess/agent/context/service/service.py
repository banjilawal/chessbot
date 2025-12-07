# src/chess/agent/context/service/service.py

"""
Module: chess.agent.context.service.service
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
    1.  Public facing API for querying Agent datasets.
    2.  Encapsulates Search and search filter validation in one extendable module.
    3.  Manage AgentContext integrity lifecycle.

    # PARENT
        *   ContextService

    # PROVIDES:
        *   AgentFinder
        *   AgentContextBuilder
        *   AgentContextValidator

    # ATTRIBUTES:
    See super class for inherited attributes.
    """
    DEFAULT_NAME = "AgentContextService"
    _finder: AgentFinder
    
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
            1.  Constructor

        # Parameters:
            *   name (str): Default value - DEFAULT_NAME
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
        return cast(AgentFinder, self.entity_finder)
    
    @property
    def builder(self) -> AgentContextBuilder:
        return cast(AgentContextBuilder, self.entity_builder)
    
    @property
    def validator(self) -> AgentContextValidator:
        return cast(AgentContextValidator, self.entity_validator)