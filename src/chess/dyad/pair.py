# src/chess/dyad/dyad.py

"""
Module: chess.dyad.dyad
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.schema import Schema
from chess.agent import PlayerAgent



class SchemaAgentPair:
    _schema: Schema
    _agent: PlayerAgent
    
    def __init__(self, schema: Schema, agent: PlayerAgent):
        self._schema = schema
        self._agent = agent
        
    @property
    def schema(self) -> Schema:
        return self._schema
    
    @property
    def agent(self) -> PlayerAgent:
        return self._agent
        
    