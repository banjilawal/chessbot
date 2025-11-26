# src/chess/team/coord_stack_validator.py

"""
Module: chess.team.coord_stack_validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import cast, Any


from chess.agent import PlayerAgentService
from chess.agent.service import AgentService
from chess.king import KingPiece
from chess.piece import CombatantPiece, Piece, PieceValidator
from chess.system import GameColor, IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.team import (
    InvalidTeamException, NullTeamException, Team, TeamDataService, TeamNotRegisteredWithAgentException, TeamSchema,
    TeamSchemaValidator
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
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
            schema_validation: TeamSchemaValidator = TeamSchemaValidator(),
    ) -> ValidationResult[Team]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a Team. If so casyt it.
        3.  Check id safety with IdentityService
        4.  Verify schema's correctness with TeamSchemaValidator.
        5.  Check agent safety with PlayerAgentService.
        6.  If any check fails, return the exception inside a ValidationResult.
        7.  If all pass return the Team object in a ValidationResult

        # PARAMETERS:
            *   candidate (Any):                            Object to validate as a Team object.
            
            *   identity_service (IdentityService):         Validates id safety
            
            *   agent_service (PlayerAgentService):         Validares agnent if candidate is a Team .
            
            *   schema_validator (TeamSchemaValidator):     Validates Schema instance's correctness.

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
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Team):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected Team, got {type(candidate).__name__} instead.")
                )
            
            team = cast(Team, candidate)
            
            id_validation = identity_service.validate_id(team.id)
            if not id_validation.is_success():
                return ValidationResult.failure(id_validation.exception)
            
            schema_validation = schema_validation.validate(team.schema)
            if schema_validation.is_failure():
                return ValidationResult.failure(schema_validation.exception)
            
            agent_validation = agent_service.validate(team.agent)
            if agent_validation.is_failure():
                return ValidationResult.failure(agent_validation.exception)
            
            if agent_service.found_team(team) is None:
                return ValidationResult.failure(
                    TeamNotRegisteredWithAgentException(
                        f"{method}: {TeamNotRegisteredWithAgentException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(team)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(
                    f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}",
                    ex)
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_schema(cls, candidate: Any) -> ValidationResult[TeamSchema]:
        method = "TeamValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamSchemaException(f"{method} {NullTeamSchemaException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, TeamSchema):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected TeamSchema, got {type(candidate).__name__} instead."
                    )
                )
            
            team_schema = cast(TeamSchema, candidate)
            return ValidationResult.success(team_schema)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamSchemaException(
                    ex=ex,
                    message=(
                        f"{method} "
                        f"{InvalidTeamSchemaException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
    @classmethod
    LoggingLevelRouter.monitor
    def validate_piece_registration(
            cls,
            piece_candidate: Any,
            team_candidate: Any,
            piece_validator: PieceValidator = PieceValidator(),
            team_data_service: TeamDataService = TeamDataService(),
    ) -> ValidationResult(Team, Piece):
        method = "TeamValidator.validate_piece_registration"
        try:
            piece_validation = piece_validator.validate(piece_candidate)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            piece = cast(Piece, piece_candidate)
            
            team_validation = cls.validate(team_candidate)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            team = cast(Team, team_candidate)
            
            
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(
                    ex=ex,
                    message=(
                        f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}"
                    )
                    
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_team_name(cls, candidate: Any) -> ValidationResult[str]:
        method = "TeamValidator.validate_team_name"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamNameException(f"{method} {NullTeamNameException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected str, got {type(candidate).__name__} instead."
                    )
                )
            
            name = cast(str, candidate)
            if name not in [TeamSchema.WHITE.name, TeamSchema.BLACK.name]:
                return ValidationResult.failure(
                    TeamNameBoundsException(
                        f"{method} {TeamNameBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(name)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(
                    ex=ex,
                    message=(
                        f"{method} "
                        f"{InvalidTeamException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def validate_team_color(cls, candidate: Any) -> ValidationResult[GameColor]:
        method = "TeamValidator.validate_team_color"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullTeamColorException(f"{method} {NullTeamColorException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected GameColor, got {type(candidate).__name__} instead."
                    )
                )
            
            color = cast(GameColor, candidate)
            if name not in [TeamSchema.WHITE.name, TeamSchema.BLACK.name]:
                return ValidationResult.failure(
                    TeamColorBoundsException(
                        f"{method} {TeamColorBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(color)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(
                    ex=ex,
                    message=(
                        f"{method} "
                        f"{InvalidTeamException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def piece_bound_to_team_roster(
            cls,
            team: Team,
            piece: Piece,
            piece_validator: type[PieceValidator] = PieceValidator
    ) -> ValidationResult[(Team, Piece)]:
        try:
            team_validation = cls.validate(team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            piece_validation = piece_validator.validate_piece_is_actionable(piece)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            if piece.team != team:
                return ValidationResult.failure()
                
            if (
                    (isinstance(piece, CombatantPiece) and cast(CombatantPiece, piece).captor is not None) or
                    isinstance(piece, KingPiece) and cast(KingPiece, piece).is_checkmated
                ):
                return ValidationResult.failure()
            
            if piece not in team.roster:
                return ValidationResult.failure()
            
            return ValidationResult.success((team, piece))
        except Exception as ex:
            return ValidationResult.failure(ex)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def piece_bound_to_team_hostages(
            cls,
            team: Team,
            piece: Piece,
            piece_validator: type[PieceValidator] = PieceValidator
    ) -> ValidationResult[(Team, Piece)]:
        try:
            team_validation = cls.validate(team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            piece_validation = piece_validator.validate_piece_is_actionable(piece)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            if piece.team == team:
                return ValidationResult.failure()
                
            if piece not in team.hostages:
                return ValidationResult.failure()
            
            return ValidationResult.success((team, piece))
        except Exception as ex:
            return ValidationResult.failure(ex)