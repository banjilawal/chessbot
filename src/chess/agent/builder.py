# src/chess/agent/build.py

"""
Module: chess.agent.build
Author: Banji Lawal
Created: 2025-09-11
version: 1.0.0
"""


from typing import Optional

from chess.engine import DecisionEngine
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.agent import Agent, HumanPlayerAgent, MachinePlayerAgent, PlayerAgentBuildFailed, TeamStackService


class AgentBuilder(Builder[Agent]):
    """
    # ROLE: Builder, Data Integrity Guarantor

    # RESPONSIBILITIES:
    Produce Agent instances whose integrity is always guaranteed. If any attributes do not pass
    their integrity checks, send an exception instead of an unsafe Agent.

    # PROVIDES:
    BuildResult[Agent] containing either:
        - On success: Agent in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    def build(
            cls,
            id: int,
            name: str,
            engine: Optional[DecisionEngine] = None,
            identity_service: IdentityService = IdentityService(),
            team_stack_service: TeamStackService=TeamStackService(),
    ) -> BuildResult[Agent]:
        """
        # ACTION:
        1.  Run safety checks on id and name with identity_service checks with identity_service.
        2.  If any checks fail, send their exception to the caller in a BuildResult.
        3.  When all checks pass, create a new Agent object then send to the caller in a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   engine (Optional[DecisionEngine])
            *   identity_service (IdentityService)
            *   team_stack_service (teamStackService])

        # Returns:
        ValidationResult[TeamStackService] containing either:
            - On success: TeamStackService in the payload.
            - On failure: Exception.

        # Raises:
            *   AgentBuildFailedException
        """
        method = "AgentBuilder.build"
        
        try:
            # id_validation = IdValidator.validate(commander_id)
            # if not id_validation.is_success():
            #   LoggingLevelRouter.throw_if_invalid(AgentBuilder, id_validation.err)
            name_validation = NameValidator.validate(name)
            if not name_validation.is_success():
                LoggingLevelRouter.log_and_raise_error(AgentBuilder, name_validation.exception)
            
            if engine is not None and not isinstance(engine, DecisionEngine):
                error = TypeError(f"Expected agent_name Decision, but got {type(engine).__name__}.")
                LoggingLevelRouter.log_and_raise_error(AgentBuilder, error)
            
            if engine is not None and isinstance(engine, DecisionEngine):
                return BuildResult(payload=Bot(name=name, engine=engine))
            
            # If no engine is provided and all the checks are passed, agent_name HumanPlayerAgent agent is returned
            return BuildResult(payload=Human(name=name))
        
        except (
                TypeError,
                InvalidNameException
        ) as e:
            raise CommanderBuildFailedException(f"{method}: {e}") from e
        
        # Catch any unexpected errors with details about type and message
        except Exception as e:
            raise CommanderBuildFailedException(
                f"{method}: Unexpected error ({type(e).__name__}): {e}"
            ) from e
#
#
# def main():
#   build_result = AgentBuilder.build(commander_id=id_emitter.person_id, visitor_name=RandomName.person())
#   if build_result.is_success():
#     competitor = build_result.payload
#     print(f"Successfully built competitor: {competitor}")
#   else:
#     print(f"Failed to build competitor: {build_result.err}")
#
#   build_result = AgentBuilder.build(-1, 4)
#   if build_result.is_success():
#     competitor = build_result.payload
#     print(f"Successfully built competitor: {competitor}")
#   else:
#     print(f"Failed to build competitor: {build_result.err}")
#
# if __name__ == "__main__":
#   main()
