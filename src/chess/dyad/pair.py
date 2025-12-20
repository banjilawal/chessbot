# src/chess/dyad/dyad.py

"""
Module: chess.dyad.dyad
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from typing import cast

from chess.arena import Arena, ArenaService
from chess.dyad import SchemaAgentPairException
from chess.schema import Schema
from chess.agent import PlayerAgent
from chess.system import IdentityService, InsertionResult, id_emitter
from chess.team import Team


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
    
    def insert_new_team(
            self,
            arena: Arena,
            id: int = id_emitter.team_id,
            arena_service: ArenaService = ArenaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> InsertionResult[Team]:
        """"""
        method = "SchemaAgentPair.insert_new_team"
        try:
            id_validation = identity_service.validate_id(candidate=id)
            if id_validation.is_failure:
                return InsertionResult(id_validation.exception)
            
            arena_validation = arena_service.validator.validate(candidate=arena)
            if arena_validation.is_failure:
                return InsertionResult(arena_validation.exception)
            
            agent_builder = self._agent.team_assignments.team_service.builder
            build = agent_builder.build(id=id, schema=self._schema, arena=arena, player_agent=self._agent)
            if build.is_failure:
                return InsertionResult.failure(build.exception)
            
            team = cast(Team, build.payload)
            if team not in arena.tea
            
            
        except Exception as ex:
            return InsertionResult(
                SchemaAgentPairException(ex=ex, message=f"{method}: {SchemaAgentPairException.DEFAULT_MESSAGE}")
            )
        
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, SchemaAgentPair):
            return self.schema == other.schema and self.agent == other.agent
        return False
    
    def __hash__(self) -> int:
        return hash((self.schema, self.agent.__hash__()))
        
    