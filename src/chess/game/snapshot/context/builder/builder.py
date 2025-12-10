# src/chess/game/snapshot/context/builder/builder.py

"""
Module: chess.game.snapshot.context.builder.builder
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BuildResult, Builder
from chess.game import GameSnapshotContext


class GameSnapShotContextBuilder(Builder[GameSnapshotContext]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            team_service: TeamService = TeamService(),
            agent_service: AgentService = AgentService(),
            number_validator: NumberValidator = NumberValidator(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[GameSnapshotContext]:
        """
        # Action:
            1.  Confirm that only one in the (id, agent, team , arena) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success send the verified GameSnapshotContext in a BuildResult.

        # Parameters:
        Only one these must be provided:
            *   timestamp (Optional[int])
            *   agent (Optional[Agent])
            *   team (Optional[Team])

        These Parameters must be provided:
            *   agent_service (AgentService)
            *   number_validator (NumberValidator)

        # Returns:
        BuildResult[GameSnapshotContext] containing either:
            - On success: GameSnapshotContext in the payload.
            - On failure: Exception.

        # Raises:
            *   TypeError
            *   NullGameSnapshotContextException
            *   NoGameSnapshotContextFlagException
            *   TooManyGameSnapshotContextFlagsException
            *   GameSnapshotBuildFailedException
        """
        method = "GameSnapshotContextValidator.validate"
        try:
            # If the candidate is null no other checks are needed.
            if candidate is None:
                return BuildResult.failure(
                    NullGameSnapshotContextException(f"{method}: {NullGameSnapshotContextException.DEFAULT_MESSAGE}")
                )
            # If the candidate is not an GameSnapshotContext validation has failed.
            if not isinstance(candidate, GameSnapshotContext):
                return BuildResult.failure(
                    TypeError(f"{method}: Expected GameSnapshotContext, got {type(candidate).__name__} instead.")
                )
            # Once the two existence checks are passed candidate can be cast to an GameSnapshotContext
            # For additional checks.
            context = cast(GameSnapshotContext, candidate)
            
            # Perform the two checks ensuring only one Game attribute value will be used in the searcher.
            if len(context.to_dict()) == 0:
                return BuildResult.failure(
                    NoGameSnapshotContextFlagException(
                        f"{method}: {NoGameSnapshotContextFlagException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(context.to_dict()) > 1:
                return BuildResult.failure(
                    TooManyGameSnapshotContextFlagsException(
                        f"{method}: {TooManyGameSnapshotContextFlagsException.DEFAULT_MESSAGE}"
                    )
                )
            # Certify the context if search is going to be by the snapshot's timestamp
            if context.timestamp is not None:
                validation = number_validator.validate_id(candidate=context.timestamp)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return the search_by_game_id context.
                return BuildResult.success(context)
            
            # Certify the context if search is going to be by the an arena team's player agent.
            if context.agent is not None:
                validation = agent_service.validator.validate(candidate=context.agent)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return the search_by_arena_team_agent context.
                return BuildResult.success(context)
            
            # Certify the context if search is going to be by the snapshot's arena team
            if context.team is not None:
                validation = team_service.validator.validate(candidate=context.team)
                if validation.is_failure:
                    return BuildResult.failure(validation.exception)
                # On validation success return the search_by_arena_team context.
                return BuildResult.success(context)
        
        # Finally, if none of the execution paths matches the state wrap the unhandled exception inside
        # an GameSnapshotBuildFailedException. Then send exception chain a BuildResult.failure.
        except Exception as ex:
            return BuildResult.failure(
                GameSnapshotBuildFailedException(
                    ex=ex, message=f"{method}: {GameSnapshotBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
