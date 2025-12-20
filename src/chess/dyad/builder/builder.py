# src/chess/dyad/builder/builder.py

"""
Module: chess.dyad.builder.builder
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.dyad import SchemaAgentPair, SchemaAgentPairBuildFailedException
from chess.schema import Schema, SchemaLookup
from chess.agent import AgentService, PlayerAgent
from chess.system import BuildResult, Builder, LoggingLevelRouter


class SchemaAgentPairBuilder(Builder[SchemaAgentPair]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            schema: Schema,
            agent: PlayerAgent,
            agent_service: AgentService = AgentService(),
            schema_service: SchemaLookup = SchemaLookup(),
    ) -> BuildResult[SchemaAgentPair]:
        """"""
        method = "SchemaAgentPairBuilder.build"
        try:
            agent_validation = agent_service.validator.validate(agent)
            if agent_validation.is_failure:
                return BuildResult.failure(agent_validation.exception)
            schema_validation = schema_service.validator.validate(schema)
            if schema_validation.is_failure:
                return BuildResult.failure(schema_validation.exception)
            return BuildResult.success(SchemaAgentPair(schema=schema, agent=agent))
        except Exception as ex:
            return BuildResult.failure(
                SchemaAgentPairBuildFailedException(
                    ex=ex, message=f"{method}: {SchemaAgentPairBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    