# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import cast

from chess.system import Service, id_emitter
from chess.agent import Agent, AgentFactory, AgentValidator


class AgentService(Service[Agent]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects Agent instance's internal state.
    3.  Masks implementation details and business logic making features easier to use.
    4.  Single entry point for managing Agent lifecycles with AgentBuilder and AgentValidator.

    # PROVIDES:
        *   AgentBuilder
        *   AgentValidator

    # ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   builder (AgentBuilder)
        *   validator (AgentValidator)
    """
    DEFAULT_NAME = "AgentService"
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            builder: AgentFactory = AgentFactory(),
            validator: AgentValidator = AgentValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def builder(self) -> AgentFactory:
        return cast(AgentFactory, self.builder)
    
    @property
    def validator(self) -> AgentValidator:
        return cast(AgentValidator, self.validator)
    
    
    