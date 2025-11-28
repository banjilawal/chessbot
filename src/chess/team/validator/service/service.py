from typing import Any, cast

from pip._internal.models import candidate

from chess.agent import Agent, AgentContextService, AgentService, AgentValidator
from chess.game.model import Game
from chess.game.service import GameService
from chess.team import (
    Team, , TeamContextService, TeamNotRegisteredWithActorException, TeamNotRegisteredWithAgentException,
    TeamSchemaValidator, TeamValidator
)
from chess.system import Service, ValidationResult, Validator, id_emitter


class TeamValidatorService(Service[Team]):
    """"""
    DEFAULT_NAME = "TeamValidatorService"
    _id: int
    _name: str
    _validator: TeamValidator
    _schema_validator: TeamSchemaValidator
    
    def __init__(
            self,
            name: str = DEFAULT_NAME,
            id: int = id_emitter.service_id,
            validator: TeamValidator = TeamValidator(),
            schema_validator: TeamSchemaValidator = TeamSchemaValidator(),
    ):
        super().__init__(id=id, name=name, builder=None, validator=validator)
        self._id = id
        self._name = name
        self._validator = validator
        self._schema_validator = schema_validator
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def validator(self) -> TeamValidator:
        return self._validator
    
    @property
    def schema(self) -> TeamSchemaValidator:
        return self._schema_validator
    
    def verify_team(self, candidate: Any) -> ValidationResult[Team]:
        return self._validator.validate(candidate)


    def verify_team_has_registered(self
    ) -> ValidationResult[(Team)]:


    def verify_agent_has_registered_team(
            self, team_candidate: Any,
            agent_candidate: Any,
            agent_service: AgentService = AgentService(),
            team_context_service: TeamContextService = TeamContextService(),
    ) -> ValidationResult[(Team, Agent)]:
        """"""
        method = "TeamValidatorService.verify_agent_has_registered_team"
        
        try:
            # Start the error detection process.
            team_validation = self._validator.validate(team_candidate)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            team = team_validation.payload
            
            agent_validation = agent_service.validator.validate(agent_candidate)
            if agent_validation.is_failure():
                return ValidationResult.failure(agent_validation.exception)
            agent = agent_validation.payload
            
            if team.agent != agent:
                return ValidationResult.failure(
                    TeamAgentMismatchException(f"{method}: {TeamAgentMismatchException.DEFAULT_MESSAGE}")
                )
            
            search_context_build = team_context_service.builder.build(id=team.id)
            if search_context_build.is_failure():
                return ValidationResult.failure(search_context_build.exception)
            
            search_result = agent.team_stack.search(search_context=search_context_build.payload)
            if search_result.is_failure():
                return ValidationResult.failure(search_result.exception)
            
            if search_result.is_empty():
                return ValidationResult.failure(
                    TeamNotRegisteredWithAgentException(
                        f"{method}: {TeamNotRegisteredWithAgentException.DEFAULT_MESSAGE}"
                    )
                )
            
            # If no errors are detected return the (team, agent) tuple indicating
            # The agent has the team in its records.
            return ValidationResult.success(payload=(team, agent))
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                TeamNotRegisteredWithAgentException(
                    ex=ex, message=f"{method}: {TeamNotRegisteredWithAgentException.DEFAULT_MESSAGE}"
                )
            )
    
    def verify_team_and_game_relationship(
            self, team_candidate: Any,
            game_candidate: Any,
            game_service: GameService = GameService(),
    ) -> ValidationResult[(Team, Game)]:
        """"""
        method = "TeamValidatorService.vverify_team_and_game_relationship"
        
        try:
            # Start the error detection process.
            team_validation = self._validator.validate(team_candidate)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            team = team_validation.payload
            
            game_validation = game_service.validator.validate(game_candidate)
            if game_validation.is_failure():
                return ValidationResult.failure(game_validation.exception)
            game = game_validation.payload
            
            if team.game != game:
                return ValidationResult.failure(
                    NoTeamGameRelastionshipException(f"{method}: {NoTeamGameRelastionshipException.DEFAULT_MESSAGE}")
                )
            
            # If no errors are detected return the (team, agent) tuple indicating
            # The agent has the team in its records.
            return ValidationResult.success(payload=(team, game))
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return ValidationResult.failure(
                NoTeamGameRelastionshipException(
                    ex=ex, message=f"{method}: {TNoTeamGameRelastionshipException.DEFAULT_MESSAGE}"
                )
            )
