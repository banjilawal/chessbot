# src/chess/agent/context/service/service.py

"""
Module: chess.agent.context.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import EntityService, id_emitter
from chess.agent import AgentContext, AgentContextBuilder, AgentContextValidator, AgentFinder


class AgentContextService(EntityService[AgentContext]):
    """
    # ROLE: Finder, EntityService, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Finder API.
    2.  Module for searching AgentDataServices.
    2.  Protects AgentContext's internal state from direct, unprotected access.
    3.  Encapsulates Finder and Finder filtering operations in an extendable module.
    4.  Single entry point for managing AgentContext integrity lifecycles with AgentContextBuilder
        and AgentContextValidator.

    # PARENT
        *   EntityService

    # PROVIDES:
        *   AgentFinder
        *   AgentContextBuilder
        *   AgentContextValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   searcher (AgentFinder)
        *   builder (AgentContextBuilder)
        *   validator (AgentContextValidator)
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
            *   searcher (AgentFinder): Default value - AgentFinder()
            *   builder (AgentContextBuilder): Default value - AgentContextBuilder()
            *   validator (AgentContextValidator): Default value - AgentContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        method = "AgentContextService.__init__"
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._finder = finder
        
    @property
    def finder(self) -> AgentFinder:
        return self._finder
    
    @property
    def builder(self) -> AgentContextBuilder:
        return cast(AgentContextBuilder, self.item_builder)
    
    @property
    def validator(self) -> AgentContextValidator:
        return cast(AgentContextValidator, self.item_validator)