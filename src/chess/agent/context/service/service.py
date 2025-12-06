# src/chess/agent/context/service/service.py

"""
Module: chess.agent.context.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import Service, id_emitter
from chess.agent import AgentContext, AgentContextBuilder, AgentContextValidator


class AgentContextService(Service[AgentContext]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects AgentContext instance's internal state.
    3.  Masks implementation details and business logic making features easier to use.
    4.  Single entry point for managing AgentContext lifecycles with AgentContextBuilder and AgentContextValidator.
    
    # Parent
        *   Service

    # PROVIDES:
        *   AgentContextBuilder
        *   AgentContextValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (AgentContextBuilder)
        *   validator (AgentContextValidator)
    """
    DEFAULT_NAME = "AgentContextService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: AgentContextBuilder = AgentContextBuilder(),
            validator: AgentContextValidator = AgentContextValidator(),
    ):
        """
        # Action:
            1.  Constructor

        # Parameters:
        Only one these must be provided:
            *   name (str): Default value - DEFAULT_NAME
            *   id (int): Default value - id_emitter.service_id
            *   builder (AgentContextBuilder): Default value - AgentContextBuilder()
            *   validator (AgentContextValidator): Default value - AgentContextValidator()

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
        @property
        def builder(self) -> AgentContextBuilder:
            return cast(AgentContextBuilder, self.item_builder)
        
        @property
        def validator(self) -> AgentContextValidator:
            return cast(AgentContextValidator, self.item_validator)