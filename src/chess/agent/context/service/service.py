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
    """"""
    DEFAULT_NAME = "AgentContextService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: AgentContextBuilder = AgentContextBuilder(),
            validator: AgentContextValidator = AgentContextValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        
        @property
        def builder(self) -> AgentContextBuilder:
            return cast(AgentContextBuilder, self.item_builder)
        
        @property
        def validator(self) -> AgentContextValidator:
            return cast(AgentContextValidator, self._validator)