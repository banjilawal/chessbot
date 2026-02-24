# src/chess/team/validator/validator.py

"""
Module: chess.team.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import cast, Any

from chess.player import PlayerService
from chess.schema import SchemaService
from chess.board import Board, BoardService, TeamBelongsToDifferentOwnerException
from chess.board import Board, BoardService, TeamPlayingDifferentBoardException
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.team import (
    NullTeamException, OwnerHasStaleTeamLinkException, Team, TeamNotRegisteredOwnerException,
    TeamNotSubmittedBoardRegistrationException,
    TeamValidationException
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
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
    None

    # LOCAL METHODS:
        *   validate(
                candidate: Any,
                board_service: BoardService(),
                player_service: BoardService = BoardService(),
                schema_service: SchemaService = SchemaService(),
                identity_service: IdentityService = IdentityService(),
            ) -> ValidationResult[Team]

    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService(),
            player_service: PlayerService = PlayerService(),
            schema_service: SchemaService = SchemaService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Team]:
        """
        # ACTION:
            1.  If the candidate fails either
                    *   A null check.
                    *   A type check.
                Send an exception chain in the ValidationResult. Else, cast candidate to Team instance team.
            2.  Send an exception chain in the ValidationResult if either
                    *   The id
                    *   The schema
                    *   The board
                    *   The owner
                are is not certified as safe by their services.
            3.  The team has been certified as safe, send the validation success result.
        # PARAMETERS:
            *   candidate (Any)
            *   board_service (BoardService)
            *   player_service (PlayerService)
            *   schema_service (SchemaService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        # RAISES:
            *   TypeError
            *   NullTeamException
            *   TeamValidationException
        """
        method = "TeamValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Team):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Team, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to a Team for additional tests ---#
        team = cast(Team, candidate)
        
        # Handle the case that, team.id is not certified as safe.
        id_validation = identity_service.validate_id(candidate=team.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that, team.schema is not certified as safe.
        schema_validation = schema_service.validator.validate(team.schema)
        if schema_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=schema_validation.exception
                )
            )
        # Handle the case that, team.owner safety and relation validation fails.
        owner_verification = cls._verify_team_owner(team=team, player_service=player_service)
        if owner_verification.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=owner_verification.exception
                )
            )
        # Handle the case the team.board safety and relation fails.
        board_verification = cls._verify_team_board(team=team, board_service=board_service)
        if board_verification.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=board_verification.exception
                )
            )
        # --- On certification successes send the team in the ValidationResult. ---#
        return ValidationResult.success(payload=team)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_team_owner(
            cls, 
            team: Team, 
            player_service: PlayerService = PlayerService()
    ) -> ValidationResult[Board]:
        """
        # ACTION:
            1.  If the TeamOwnerRelationAnalyzer provided by player_service does not return a
                bidirectional relationship result send the exception to the caller.
            2.  Else, send the success validation result to the caller.
        # PARAMETERS:
            *   team (Team)
            *   player_service (PlayerService)
        # RETURNS:
            *   ValidationResult[Player] containing either:
                    - On failure: Exception.
                    - On success: Player in the payload.
        # RAISES:
            *   TeamBelongsToDifferentOwnerException
            *   TeamNotRegisteredOwnerException
        """
        method = "TeamValidator._verify_team_owner"
        
        # Handle the case that, either team.owner is not certified as safe or the analysis aborts.
        owner_team_relation = player_service.player_team_relation_analyzer.analyze(
            candidate_primary=team.owner,
            candidate_satellite=team,
        )
        if owner_team_relation.is_failure:
            return ValidationResult.failure(owner_team_relation.exception)
        
        # Handle the case that, the team belongs to a different owner.
        if owner_team_relation.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamBelongsToDifferentOwnerException(
                        f"{method}: {TeamBelongsToDifferentOwnerException.DEFAULT_MESSAGE}"
                )
            )
        # Handle the case that, the team has not been added to the owner's teams.
        if owner_team_relation.registration_does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamNotRegisteredOwnerException(
                    f"{method}: {TeamNotRegisteredOwnerException.DEFAULT_MESSAGE}"
                )
            )
        # Handle the case that, the player has stale link to the team.
        if owner_team_relation.registration_does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                OwnerHasStaleTeamLinkException(
                    f"{method}: {OwnerHasStaleTeamLinkException.DEFAULT_MESSAGE}"
                )
            )
        # --- On certification successes send the owner in the ValidationResult. ---#
        return ValidationResult.success(payload=team.owner)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _verify_team_board(
            cls,
            team: Team,
            board_service: BoardService = BoardService()
    ) -> ValidationResult[Board]:
        """
        # ACTION:
            1.  If the TeamOwnerRelationAnalyzer provided by board_service does not return a
                bidirectional relationship result send the exception to the caller.
            2.  Else, send the success validation result to the caller.
        # PARAMETERS:
            *   team (Team)
            *   board_service (BoardService)
        # RETURNS:
            *   ValidationResult[Board] containing either:
                    - On failure: Exception.
                    - On success: Board in the payload.
        # RAISES:
            *   TeamBelongsToDifferentOwnerException
            *   TeamNotRegisteredOwnerException
        """
        method = "TeamValidator._verify_team_board"
        # Handle the case that, board is not certified
        board_team_relation = board_service.board_team_relation_analyzer.analyze(
            candidate_primary=team.board,
            candidate_satellite=team
        )
        # Handle the case that, the relation analysis fails.
        if board_team_relation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=board_team_relation.exception
                )
            )
        # Handle the case that, there is no relation between the board and team.
        if board_team_relation.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=TeamPlayingDifferentBoardException(
                        f"{method}: {TeamPlayingDifferentBoardException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that, the team has not occupied its slot in the board.
        if board_team_relation.partially_exists:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationException(
                    message=f"{method}: {TeamValidationException.ERROR_CODE}",
                    ex=TeamNotSubmittedBoardRegistrationException(
                        f"{method}: {TeamNotSubmittedBoardRegistrationException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # The only outcome left is the board has occupied its slot. Validate the board,
        return ValidationResult.success(payload=team.board)