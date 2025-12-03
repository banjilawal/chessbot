# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import cast

from chess.system import IntegrityService
from chess.agent import Agent, AgentFactory, AgentValidator


class AgentIntegrityService(IntegrityService[Agent]):
    DEFAULT_NAME = "AgentIntegrityService"
    
    def __init__(
            self,
            id: int,
            name: str = DEFAULT_NAME,
            builder: AgentFactory = AgentFactory(),
            validator: AgentValidator = AgentValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
    @property
    def item_validator(self) -> AgentValidator:
        return cast(AgentValidator, self.item_validator)
    
    @property
    def item_builder(self) -> AgentFactory:
        return cast(AgentFactory, self.item_builder)
    
    
    