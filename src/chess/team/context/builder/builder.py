# src/chess/team/context/builder/builder.py

"""
Module: chess.team.context.builder.builder
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.agent import Agent, AgentService
from chess.game import Game
from chess.game.service import GameService
from chess.system import Builder, BuildResult, GameColor, IdentityService, LoggingLevelRouter
from chess.team import (
    NoTeamContextFlagsException, TeamContext, TeamContextBuildFailedException, TeamSchema, TeamSchemaValidator,
    TeamValidator,
    TooManyTeamContextFlagsException
)


class TeamContextBuilder(Builder[TeamContext]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce TeamContext instances whose integrity is always guaranteed.
     2.  Manage construction of TeamContext instances that can be used safely by the client.
     3.  Ensure params for TeamContext creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT:
         * Builder

     # PROVIDES:
         *   TeamContextBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: Optional[int] = None,
            name: Optional[str] = None,
            game: Optional[Game] = None,
            agent: Optional[Agent] = None,
            color: Optional[GameColor] = None,
            game_service: GameService = GameService(),
            agent_service: AgentService = AgentService(),
            idservice: IdentityService = IdentityService(),
            schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ) -> BuildResult[TeamContext]:
        """
        # Action:
            1. Confirm that only one in the tuple (id, name, agent, color, team_schema), is not null.
            2. Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3. If all checks pass build the PieceContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   id (Optional[int])
            *   name (Optional[int])
            8   game (Optional[Game])
            *   agent (Optional[Agent])
            *   color (Optional[GameColor])

        These Parameters must be provided:
            *   game_service (GameService)
            *   agent_certifier (AgentService)
            *   identity_service (IdentityService)
            *   schema_validator (TeamSchemaValidator)

        # Returns:
          BuildResult[TeamContext] containing either:
                - On success: TeamContext in the payload.
                - On failure: Exception.

        # Raises:
            *   TeamContextBuildFailedException
            *   NoTeamContextFlagsException
            *   TooManyTeamContextFlagsException
        """
        method = "PieceSearchContextBuilder.builder"
        
        try:
            # Start the error detection process.
            params = [id, name, agent, color, schema]
            param_count = sum(bool(p) for p in params)
            
            if param_count == 0:
                return BuildResult.failure(
                    NoTeamContextFlagsException(f"{method}:  {NoTeamContextFlagsException.DEFAULT_MESSAGE}")
                )
            
            if param_count > 1:
                return BuildResult.failure(
                    TooManyTeamContextFlagsException(f"{method}: {TooManyTeamContextFlagsException}")
                )
            # If no errors are detected pick the flag whose value is not for processing.
            
            if id is not None:
                validation = idservice.validate_id(id)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # If id is correct create a id.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(id=validation.payload))
            
            if agent is not None:
                validation = agent_service.item_validator.validate(agent)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # If agent is correct create a agent.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(agent=validation.payload))
            
            if name is not None:
                validation = schema_validator.verify_name_in_schema(candidate=name)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # If name is correct create a name.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(name=validation.payload))

            if color is not None:
                validation = schema_validator.verify_color_in_schema(candidate=color)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # If color is correct create a color.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(color=validation.payload))
            
            if game is not None:
                validation = game_service.item_validator.validate(candidate=color)
                if validation.is_failure():
                    return BuildResult.failure(validation.exception)
                # If game is correct create a game.TeamContext and return it.
                return BuildResult.success(payload=TeamContext(game=validation.payload))
            
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                TeamContextBuildFailedException(
                    ex=ex, message=f"{method}: {TeamContextBuildFailedException.DEFAULT_MESSAGE}"
                )
            )