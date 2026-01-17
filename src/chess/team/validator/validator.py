# src/chess/team/validator/validator.py

"""
Module: chess.team.validator
Author: Banji Lawal
Created: 2025-09-11
"""

from typing import cast, Any

from chess.schema import SchemaService
from chess.board import Board, BoardService, TeamBelongsToDifferentOwnerException
from chess.board import Board, BoardService, TeamPlayingDifferentBoardException
from chess.system import IdentityService, LoggingLevelRouter, Validator, ValidationResult
from chess.team import (
    NullTeamException, Team, TeamNotSubmittedOwnerRegistrationException, TeamNotSubmittedBoardRegistrationException,
    TeamValidationFailedException
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
            board_service: BoardService(),
            owner_service: BoardService = BoardService(),
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
            4.  If team.owner is not validated by owner_service or team is not registered by its owner return
                the exception.
            5.  The tests passed. Send team in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   team_schema (Schema)
            *   board_certifier (BoardService)
            *   identity_service (IdentityService)
        # RETURNS:
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
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=NullTeamException(f"{method}: {NullTeamException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Team):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TypeError(f"{method}: Expected Team, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast the candidate to a Team for additional tests ---#
        team = cast(Team, candidate)
        
        # Handle the case team.id certification fails.
        id_validation = identity_service.validate_id(candidate=team.id)
        if id_validation.is_failure:
            # Return the exception chain on failure.
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
                # Return the exception chain on failure.
                return ValidationResult(
                    TeamValidationFailedException(
                        message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                        ex=schema_validation.exception
                    )
                )
        # Handle the case that team.owner safety and relation validation fails.
        owner_verification = cls._validate_owner(team=team, owner_service=owner_service)
        if owner_verification.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=owner_verification.exception
                )
            )
        # Handle the case the team.board safety and relation fails.
        board_verification = cls._validate_board(team=team, board_service=board_service)
        if board_verification.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=board_verification.exception
                )
            )
        # On certification successes send the team instance in the ValidationResult.
        return ValidationResult.success(payload=team)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_owner(cls, team: Team, owner_service: BoardService = BoardService()) -> ValidationResult[Board]:
        """
        # ACTION:
            1.  If team.owner is not validated by owner_service return validation exception.
            2.  If the team is not owner.teams return an exception in the ValidationResult.
            3.  The tests passed. Send team.owner in the ValidationResult.
        # PARAMETERS:
            *   team (Team)
            *   owner_service (BoardService)
        # RETURNS:
        ValidationResult[Board] containing either:
            - On failure: Exception.
            - On success: Board in the payload.
        # RAISES:
            *   TeamValidationFailedException
        """
        method = "TeamValidator._validate_owner"
        
        # Handle the case team.owner certification fails.
        owner_team_relation = owner_service.board_team_relation_analyzer.analyze(
            candidate_primary=team.owner,
            candidate_satellite=team,
        )
        # Handle the case that there is a direct failure of analyzer.
        if owner_team_relation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=owner_team_relation.exception
                )
            )
        # Handle the case that the team belongs to a different owner.
        if owner_team_relation.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TeamBelongsToDifferentOwnerException(
                        f"{method}: {TeamBelongsToDifferentOwnerException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the team has not been added to the owner's teams.
        if owner_team_relation.partially_exists:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TeamNotSubmittedOwnerRegistrationException(
                        f"{method}: {TeamNotSubmittedOwnerRegistrationException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # On certification successes send the owner back to the validator.
        return ValidationResult.success(payload=team.owner)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_board(cls, team: Team, board_service: BoardService = BoardService()) -> ValidationResult[Board]:
        """
        # ACTION:
            1.  If team.board is not validated by owner_service return validation exception.
            2.  If the team is not one of the two teams in the board return the exception.
            3.  The tests are passed. Send team.board in the ValidationResult.
        # PARAMETERS:
            *   team (Team)
            *   board_service (BoardService)
        # RETURNS:
        ValidationResult[Board] containing either:
            - On failure: Exception.
            - On success: Board in the payload.
        # RAISES:
            *   TeamValidationFailedException
        """
        method = "TeamValidator._validate_board"
        # Handle the case that board is not certified
        board_team_relation = board_service.board_team_relation_analyzer.analyze(
            candidate_primary=team.board,
            candidate_satellite=team
        )
        # Handle the case that the relation analysis fails.
        if board_team_relation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=board_team_relation.exception
                )
            )
        # Handle the case that there is no relation between the board and team.
        if board_team_relation.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TeamPlayingDifferentBoardException(
                        f"{method}: {TeamPlayingDifferentBoardException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the team has not occupied its slot in the board.
        if board_team_relation.partially_exists:
            # Return the exception chain on failure.
            return ValidationResult(
                TeamValidationFailedException(
                    message=f"{method}: {TeamValidationFailedException.ERROR_CODE}",
                    ex=TeamNotSubmittedBoardRegistrationException(
                        f"{method}: {TeamNotSubmittedBoardRegistrationException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # The only outcome left is the board has occupied its slot. Validate the board,
        return ValidationResult.success(payload=team.board)