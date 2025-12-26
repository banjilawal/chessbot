# src/chess/team/validator/validator.py

"""
Module: chess.team.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import cast, Any

from chess.schema import SchemaService
from chess.arena import Arena, ArenaService
from chess.agent import PlayerAgent, AgentService
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.team import (
    TeamContext, TeamNotRegisteredWithOwnerException, TeamValidationFailedException, NullTeamException, Team,
    TeamNotInsideArenaException,
)


class TeamValidator(Validator[Team]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Team instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * TeamValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            arena_service: ArenaService(),
            player_service: AgentService = AgentService(),
            schema_service: SchemaService = SchemaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Team]:
        """
        # ACTION:
            1.  If the candidate fails existence or type checks return the exception in the ValidationResult.
                Else, cast Team into team.
            2.  If the team.id is not certified by identity_service return the exception in the ValidationResult.
            3.  If the team.schema is not certified by schema_service then return the exception in the
                ValidationResult.
            4.  If team.owner is not validated by player_service or team is not registered by its owner return
                the exception.
            5.  The tests passed. Send team in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   team_schema (Schema)
            *   agent_certifier (AgentService)
            *   identity_service (IdentityService)
        # Returns:
        ValidationResult[Team] containing either:
            - On success:   Team in the payload.
            - On failure:   Exception.
        # RAISES:
            *   TypeError
            *   NullTeamException
            *   TeamValidationFailedException
        """
        method = "TeamValidator.validate"
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain.
            return ValidationResult.failure(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Team):
            return ValidationResult.failure(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Team instance, got {type(candidate).__name__} instead.")
                )
            )
        # After the existence and type checks cast the candidate to Team for aditional tests.
        team = cast(Team, candidate)
        
        # Handle the case team.id certification fails.
        id_validation = identity_service.validate_id(candidate=team.id)
        if id_validation.is_failure:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case team.schema certification fails.
        schema_validation = schema_service.schema_validator.validate(team.schema)
        if schema_validation.is_failure:
            if id_validation.is_failure:
                # Return the exception chain.
                return ValidationResult(
                    TeamValidationFailedException(
                        message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                        ex=schema_validation.exception
                    )
                )
        # Handle the case team.owner certification fails.
        owner_verification = cls._validate_owner(team=team, player_service=player_service)
        if owner_verification.is_failure:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=owner_verification.exception
                )
            )
        # Handle the case the team.arena certification fails.
        arena_verification = cls._validate_arena(team=team, arena_service=arena_service)
        if arena_verification.is_failure:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=arena_verification.exception
                )
            )
        # On certification successes send the team instance in the ValidationResult.
        return ValidationResult.success(payload=team)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_owner(cls, team: Team, player_service: AgentService = AgentService()) -> ValidationResult[PlayerAgent]:
        """
        # ACTION:
            1.  If team.owner is not validated by player_service return validation exception.
            2.  If the team is not owner.team_assignments return an exception in the ValidationResult.
            3.  The tests passed. Send team.owner in the ValidationResult.
        # PARAMETERS:
            *   team (Team)
            *   player_service (AgentService)
        # Returns:
        ValidationResult[PlayerAgent] containing either:
            - On failure: Exception.
            - On success: PlayerAgent in the payload.
        # RAISES:
            *   TeamValidationFailedException
        """
        method = "TeamValidator._validate_owner"
        # Handle the case that team.agent certification fails.
        agent_validation = player_service.validator.validate(candidate=team.owner)
        if agent_validation.is_failure:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}", ex=agent_validation.exception
                )
            )
        # Handle the case that team is not registered with the agent.
        agent = team.owner
        search_result = agent.team_assignments.search_teams(context=TeamContext(id=team.id))
        if search_result.is_failure:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}", ex=search_result.exception
                )
            )
        # Return an exception chain if the team is not registered with the player_agent
        if search_result.is_empty:
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TeamNotRegisteredWithOwnerException(f"{method}: {TeamNotRegisteredWithOwnerException}")
                )
            )
        # On certification successes send the owner back to the validator.
        return ValidationResult.success(payload=team.owner)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_arena(cls, team: Team, arena_service: ArenaService = ArenaService()) -> ValidationResult[Arena]:
        """
        # ACTION:
            1.  If team.arena is not validated by player_service return validation exception.
            2.  If the team is not one of the two teams in the arena return the exception.
            3.  The tests are passed. Send team.arena in the ValidationResult.
        # PARAMETERS:
            *   team (Team)
            *  arena_service (ArenaService)
        # Returns:
        ValidationResult[Arena] containing either:
            - On failure: Exception.
            - On success: PlayerAgent in the payload.
        # RAISES:
            *   TeamValidationFailedException
        """
        method = "TeamValidator._validate_arena"
        # Handle the case that arena is not certified
        arena_validation = arena_service.validator.validate(candidate=team.arena)
        if arena_validation.is_failure:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=arena_validation.exception
                )
            )
        # Handle the case that the team is not in the arena
        arena = team.arena
        if team not in [arena.white_team, arena.black_team]:
            # Return the exception chain.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TeamNotInsideArenaException(f"{method}: {TeamNotInsideArenaException.DEFAULT_MESSAGE}")
                )
            )
        # On certification successes send the arena back to the validator.
        return ValidationResult.success(payload=team.arena)