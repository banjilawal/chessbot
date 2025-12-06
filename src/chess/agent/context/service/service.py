# src/chess/agent/context/service/service.py

"""
Module: chess.agent.context.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import Service, id_emitter
from chess.agent import AgentContext, AgentContextBuilder, AgentContextValidator, AgentSearch


class AgentContextService(Service[AgentContext]):
    """
    # ROLE: Search, Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Search API.
    2.  Module for searching AgentDataServices.
    2.  Protects AgentContext's internal state from direct, unprotected access.
    3.  Encapsulates Search and Search filtering operations in an extendable module.
    4.  Single entry point for managing Vector integrity lifecycles with VectorBuilder and VectorValidator.

    # Parent
        *   Service

    # PROVIDES:
        *   AgentSearch
        *   AgentContextBuilder
        *   AgentContextValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   search (AgentSearch)
        *   builder (AgentContextBuilder)
        *   validator (AgentContextValidator)
    """
    DEFAULT_NAME = "AgentContextService"
    _search: AgentSearch
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            search: AgentSearch = AgentSearch(),
            builder: AgentContextBuilder = AgentContextBuilder(),
            validator: AgentContextValidator = AgentContextValidator(),
    ):
        """
        # Action:
            1.  Constructor

        # Parameters:
            *   name (str): Default value - DEFAULT_NAME
            *   id (int): Default value - id_emitter.service_id
            *   search (AgentSearch): Default value - AgentSearch()
            *   builder (AgentContextBuilder): Default value - AgentContextBuilder()
            *   validator (AgentContextValidator): Default value - AgentContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._search = search
        
        @property
        def search(self) -> AgentSearch:
            return self._search
        
        @property
        def builder(self) -> AgentContextBuilder:
            return cast(AgentContextBuilder, self.item_builder)
        
        @property
        def validator(self) -> AgentContextValidator:
            return cast(AgentContextValidator, self.item_validator)