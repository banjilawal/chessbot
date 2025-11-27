# src/chess/agent/service/service.py

"""
Module: chess.agent.service.service
Author: Banji Lawal
Created: 2025-08-31
version: 1.0.0
"""

from chess.system import Service, id_emitter
from chess.agent import Agent, AgentFactory, AgentValidator

class AgentService(Service[Agent]):
    DEFAULT_NAME = "AgentService"
    
    def __init__(
            self,
            id: int = id_emitter.service_id,
            name: str = DEFAULT_NAME,
            builder: AgentFactory = AgentFactory(),
            validator: AgentValidator = AgentValidator(),
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)