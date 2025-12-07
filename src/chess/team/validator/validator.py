# src/chess/team/validator/validator.py

"""
Module: chess.team.validator.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import cast, Any

from chess.agent import Agent, AgentService
from chess.game import Game
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.team import (
    InvalidTeamException, NoTeamGameRelationshipException, NullTeamException, Team, TeamContext, TeamContextService,
    TeamMismatchesAgentException, TeamNotRegisteredWithAgentException, TeamSchemaValidator
)



class TeamValidator(Validator[Team]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    Verifies a candidate is an instance of Team, that meets integrity requirements, before 
    the candidate is used.

    # PROVIDES:
    ValidationResult[Team] containing either:
        - On success: Team in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes
    
    # CONSTRUCTOR:
    Default Constructor
    
    # CLASS METHODS:
           validate(
                candidate: Any, agent_certifier: AgentService, idservice: IdentityService
                team_schema_validator: TeamSchemaValidator
            ) -> ValidationResult[Team]:
            
           verify_agent_has_registered_team(
                team_candidate: Any, agent_candidate: Any, agent_certifier: AgentService,
                team_context_service: TeamContextService,
            ) -> ValidationResult[(Team, Agent)]:
            
           verify_team_and_game_relationship(
                team_candidate: Any, game_candidate: Any, game_service: GameService
            ) -> ValidationResult[(Team, Game)]:
    
    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            agent_service: AgentService = AgentService(),
            idservice: IdentityService = IdentityService(),
            schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ) -> ValidationResult[Team]:
        """
        # ACTION:
        1.  Check candidate is not null .
        2.  Check if candidate is a Team. If so cast it.
        3.  Check id safety with IdentityService
        4.  Verify schema's correctness with TeamSchemaValidator.
        5.  Check agent safety with PlayerAgentService.
        6.  If any check fails, return the exception inside a ValidationResult.
        7.  If all pass return the Team object in a ValidationResult

        # PARAMETERS:
            *   candidate (Any)
            *   schema (TeamSchema)
            *   agent_certifier (PlayerAgentService)
            *   idservice (IdentityService)

        # Returns:
        ValidationResult[Team] containing either:
            - On success:   Team in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TypeError
            *   NullTeamException
            *   InvalidTeamException
            *   TeamNotRegisteredWithAgentException
        """
        method = "TeamValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )
            if not isinstance(candidate, Team):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Team, got {type(candidate).__name__} instead.")
                )
            # Cast after the null and type checks are passed so Team attributes can be checked.
            team = cast(Team, candidate)
            
            # check schema first
            schema_validation = schema_validator.validate(team.schema)
            if schema_validation.is_failure():
                return ValidationResult.failure(schema_validation.exception)
            # After schema checks out. Test name and id at the same time.
            identity_validation = idservice.validate_identity(
                id_candidate=team.id,
                name_candidate=team.schema.name
            )
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            # Only baseline agent certification is necessary. An agent registering a team is not
            # the main use case for team objects. Separating registration verification from team
            # validation avoids circular dependencies, separates concerns and is flexible.
            agent_validation = agent_service.item_validator.validate(team.agent)
            if agent_validation.is_failure():
                return ValidationResult.failure(agent_validation.exception)
            
            # Check if the Team is registered in agent's team_assignments.
            search_result = team.agent.team_assignments.search(context=TeamContext(id=team.id))
            if search_result.is_failure():
                return ValidationResult.failure(search_result.exception)
            if search_result.is_empty():
                return ValidationResult.failure(
                    TeamNotRegisteredWithAgentException(
                        f"{method}: {TeamNotRegisteredWithAgentException.DEFAULT_MESSAGE}")
                )
            

            # For basic verification we only need to prove team has a safe game attribute.
            # Testng for a team<-->game relationship is not necessary. The team<--> game
            # relationship only matters during searches so a deeper check is not necessary.
            game_validation = game_service.item_validator.validate(team.game)
            if game_validation.is_failure():
                return ValidationResult.failure(game_validation.exception)
            
            
            # If no errors are detected return the successfully validated Team instance.
            return ValidationResult.success(team)
        
        # Finally, if there is an unhandled exception Wrap an InvalidTeamException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(ex=ex, message=f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}")
            )
 
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_agent_has_registered_team(
            cls,
            team_candidate: Any,
            agent_candidate: Any,
            agent_service: AgentService = AgentService(),
            team_context_service: TeamContextService = TeamContextService(),
    ) -> ValidationResult[(Team, Agent)]:
        """
        # ACTION:
        1.  Use validate to certify team_candidate is a safe team. If so pull from validation_result payload.
        2.  Use agent_certifier to certify agent_candidate is a safe agent. If so pull from validation_result payload.
        3.  If team.agent != agent return an exception inside a ValidationResult.
        4.  Build a search_context for the team with team_context service.
        5.  Finder for the team inside agent.team_assignments.
        6.  If the searcher generates an error or produces an no hits return an exception inside a ValidationResult.
        7.  If all checks pass return the (team, agent) registration tuple.

        # PARAMETERS:
            *   team_candidate (Any)
            *   agent_candidate (Any)
            *   agent_certifier (AgentService)
            *   team_context (TeamContextService)

        # Returns:
        ValidationResult[(Team, Agent)] containing either:
            - On success:   (Team,Agent) in the payload.
            - On failure:   Exception.

        # RAISES:
            *   TeamMismatchesAgentException
            *   TeamNotRegisteredWithAgentException
        """
        method = "TeamValidator.verify_agent_has_registered_team"
        
        try:
            # Start the error detection process.
            team_validation = cls.validate(team_candidate)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            team = team_validation.payload
            
            agent_validation = agent_service.item_validator.validate(agent_candidate)
            if agent_validation.is_failure():
                return ValidationResult.failure(agent_validation.exception)
            agent = agent_validation.payload
            
            if team.agent != agent:
                return ValidationResult.failure(
                    TeamMismatchesAgentException(f"{method}: {TeamMismatchesAgentException.DEFAULT_MESSAGE}")
                )
            
            # When team.agent == agent Finder agent.team_assignments; build a searcher context
            search_context_build = team_context_service.item_builder.build(id=team.id)
            if search_context_build.is_failure():
                return ValidationResult.failure(search_context_build.exception)
            # Run a searcher for the target.
            search_result = agent.team_assignments.searcher(search_context=search_context_build.payload)
            if search_result.is_failure():
                return ValidationResult.failure(search_result.exception)
            
            # An empty searcher result means there is no registration.
            if search_result.is_empty():
                return ValidationResult.failure(
                    TeamNotRegisteredWithAgentException(
                        f"{method}: {TeamNotRegisteredWithAgentException.DEFAULT_MESSAGE}"
                    )
                )
            # If no errors are detected return the (team, agent) tuple indicating
            # The agent has the team in its records.
            return ValidationResult.success(payload=(team, agent))
        
        # Finally, if there is an unhandled exception Wrap a TeamBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                TeamNotRegisteredWithAgentException(
                    ex=ex, message=f"{method}: {TeamNotRegisteredWithAgentException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_team_and_game_relationship(
            cls,
            team_candidate: Any,
            game_candidate: Any,
            game_service: GameService = GameService(),
    ) -> ValidationResult[(Team, Game)]:
        """
        # ACTION:
        1.  Use validate to certify team_candidate is a safe team. If so pull from validation_result payload.
        2.  Use agent_certifier to certify agent_candidate is a safe agent. If so pull from validation_result payload.
        3.  If team.game != game return an exception inside a ValidationResult.
        4.  If all checks pass return a ValidationResult containing the (team, game) relationship tuple.

        # PARAMETERS:
            *   team_candidate (Any)
            *   agent_candidate (Any)
            *   agent_certifier (AgentService)
            *   team_context (TeamContextService)

        # Returns:
        ValidationResult[(Team, Agent)] containing either:
            - On success:   (Team,Agent) in the payload.
            - On failure:   Exception.

        # RAISES:
            *   NoTeamGameRelationshipException
        """
        method = "TeamValidator.verify_team_and_game_relationship"
        
        try:
            # Start the error detection process.
            team_validation = cls.validate(team_candidate)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            team = team_validation.payload
            
            game_validation = game_service.item_validator.validate(game_candidate)
            if game_validation.is_failure():
                return ValidationResult.failure(game_validation.exception)
            game = game_validation.payload
            
            if team.game != game:
                return ValidationResult.failure(
                    NoTeamGameRelationshipException(f"{method}: {NoTeamGameRelationshipException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected return the (team, agent) tuple indicating
            # The agent has the team in its records.
            return ValidationResult.success(payload=(team, game))
        
        # Finally, if there is an unhandled exception Wrap a TeamBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                NoTeamGameRelationshipException(
                    ex=ex, message=f"{method}: {NoTeamGameRelationshipException.DEFAULT_MESSAGE}"
                )
            )
