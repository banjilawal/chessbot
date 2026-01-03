# src/chess/token/validator/validator.py

"""
Module: chess.token.validator
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Any, cast

from chess.coord import CoordDataService, CoordService
from chess.rank import RankService
from chess.system import (
    BoundNumberValidator, IdentityService, LoggingLevelRouter, ServiceValidator, ValidationResult,
    Validator
)
from chess.team import Team, TeamService
from chess.token.model import Token
from chess.token.validator.exception.wrapper import TokenValidationFailedException


class TokenValidator(Validator[Token]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Token instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * TokenValidator

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
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
            service_validator: ServiceValidator = ServiceValidator(),
            number_validation: BoundNumberValidator = BoundNumberValidator(),
    ) -> ValidationResult[Token]:
        """
        # ACTION:
            1.  If the candidate fails existence or type tests send the exception in the ValidationResult.
                Else, cast to Token instance token.
            2.  If any of the attributes; id, designation, roster_number, rank or positions fail their validation
                tests send the exception in the ValidationResult.
            3.  The token has passed all verification tests. Send the token in the ValidationResult.
        # PARAMETERS:
            *   candidate (Any)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   coord_service (CoordService)
            *   identity_service (IdentityService)
            *   number_validator (BoundNumberValidator)
        # RETURNS:
            *   ValidationResult[Team] containing either:
                    - On failure: Exception.
                    - On success: Team in the payload.
        # RAISES:
            *   TypeError
            *   NullTeamException
            *   TeamValidationFailedException
        """
        method = "Token.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullTokenException(f"{method}: {NullTokenException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Token):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}:Expected Token, got {type(candidate).__name__} instead.")
                )
            )
        # After existence and type checks cast the candidate to a Token for additional tests.
        token = cast(Token, candidate)
        
        # Handle the case that id or designation are not certified safe.
        identity_validation = identity_service.validate_identity(
            id_candidate=token.id,
            name_candidate=token.designation
        )
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case that the token's team fails validation.
        team_validation = team_service.item_validator.validate(token.team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=team_validation.exception
                )
            )
        # Handle the case that the Token's roster number fails validation and in the allowed range.
        roster_number_validation = number_validation.validate(
            candidate=token.roster_number,
            floor=1,
            ceiling=Team.MAX_ROSTER_SIZE
        )
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=roster_number_validation.exception
                )
            )
        # Handle the case that the rank is not certified safe.
        rank_validation = rank_service.validator.validate(candidate=token.rank)
        if rank_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=rank_validation.exception
                )
            )
        # Handle the case that token.positions fails its validation.
        service_validation = service_validator.validate(candidate=token.positions, expected_type=CoordDataService)
        if service_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                TokenValidationFailedException(
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}",
                    ex=service_validation.exception
                )
            )
        # With all tests passed return the token in the ValidationResult.
        return ValidationResult.success(payload=token)
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def token_is_disabled(cls, candidate: Any) -> ValidationResult[bool]:
    #     """"""
    #     method = "TokenValidator.token_is_disabled"
    #     try:
    #         token_validation = cls.validate(candidate)
    #         if token_validation.is_failure():
    #             return ValidationResult.failure(token_validation.exception)
    #
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             TokenValidationFailedException(
    #                 ex=ex,
    #                 message=(
    #                     f"{method}: "
    #                     f"{TokenValidationFailedException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #         )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def validate_token_is_actionable(
    #         cls, candidate: Any,
    #         team_service: TeamService = TeamService(),
    #         board_service: BoardService = BoardService(),
    # ) -> ValidationResult[Token]:
    #     """"""
    #     method = "TokenValidator.verify_active_token"
    #     try:
    #         token_validation = cls.validate(candidate)
    #         if token_validation.is_failure():
    #             return ValidationResult.failure(token_validation.exception)
    #
    #         token = cast(Token, token_validation.payload)
    #
    #         team = token.team
    #         if token not in team.roster:
    #             return ValidationResult.failure(
    #                 ActiveTokenMissingFromTeamRoster(f"{method} {ActiveTokenMissingFromTeamRoster.DEFAULT_MESSAGE}")
    #             )
    #
    #         if isinstance(token, KingToken) and cast(KingToken, token).is_checkmated:
    #             return ValidationResult.failure(
    #                 CheckmatedKingException(f"{method} {CheckmatedKingException.DEFAULT_MESSAGE}")
    #             )
    #
    #         if isinstance(token, CombatantToken) and cast(CombatantToken, token).captor is not None:
    #             return ValidationResult.failure(
    #                 CapturedTokenException(f"{method}: {CapturedTokenException.DEFAULT_MESSAGE}")
    #             )
    #
    #         if token.current_position is None or token.postions.is_empty():
    #             return ValidationResult.failure(
    #                 TokenRequiresInitialPlacementException(
    #                     f"{method}: {TokenRequiresInitialPlacementException.DEFAULT_MESSAGE}"
    #                 )
    #             )
    #
    #         return ValidationResult.success(token)
    #
    #     except Exception as e:
    #         return ValidationResult.failure(
    #             TokenValidationFailedException(f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}", e)
    #         )
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def token_bound_to_team_roster(
    #         cls,
    #         team: Team,
    #         token: Token,
    #         token_validator: type[TokenValidator] = TokenValidator
    # ) -> ValidationResult[(Team, Token)]:
    #     try:
    #         team_validation = cls.validate(team)
    #         if team_validation.is_failure():
    #             return ValidationResult.failure(team_validation.exception)
    #
    #         token_validation = token_validator.validate_token_is_actionable(token)
    #         if token_validation.is_failure():
    #             return ValidationResult.failure(token_validation.exception)
    #
    #         if token.team != team:
    #             return ValidationResult.failure()
    #
    #         if (
    #                 (isinstance(token, CombatantToken) and cast(CombatantToken, token).captor is not None) or
    #                 isinstance(token, KingToken) and cast(KingToken, token).is_checkmated
    #         ):
    #             return ValidationResult.failure()
    #
    #         if token not in team.roster:
    #             return ValidationResult.failure()
    #
    #         return ValidationResult.success((team, token))
    #     except Exception as ex:
    #         return ValidationResult.failure(ex)
    #
    # @classmethod
    # @LoggingLevelRouter.monitor
    # def token_bound_to_team_hostages(
    #         cls,
    #         team: Team,
    #         token: Token,
    #         token_validator: type[TokenValidator] = TokenValidator
    # ) -> ValidationResult[(Team, Token)]:
    #     try:
    #         team_validation = cls.validate(team)
    #         if team_validation.is_failure():
    #             return ValidationResult.failure(team_validation.exception)
    #
    #         token_validation = token_validator.validate_token_is_actionable(token)
    #         if token_validation.is_failure():
    #             return ValidationResult.failure(token_validation.exception)
    #
    #         if token.team == team:
    #             return ValidationResult.failure()
    #
    #         if token not in team.hostages:
    #             return ValidationResult.failure()
    #
    #         return ValidationResult.success((team, token))
    #     except Exception as ex:
    #         return ValidationResult.failure(ex)
    #
    # @classmethod
    #
    # LoggingLevelRouter.monitor
    #
    # def validate_token_registration(
    #         cls,
    #         token_candidate: Any,
    #         team_candidate: Any,
    #         token_validator: TokenValidator = TokenValidator(),
    #         team_data_service: TeamDataService = TeamDataService(),
    # ) -> ValidationResult(Team, Token):
    #     method = "TeamValidator.validate_token_registration"
    #     try:
    #         token_validation = token_validator.validate(token_candidate)
    #         if token_validation.is_failure():
    #             return ValidationResult.failure(token_validation.exception)
    #
    #         token = cast(Token, token_candidate)
    #
    #         team_validation = cls.validate(team_candidate)
    #         if team_validation.is_failure():
    #             return ValidationResult.failure(team_validation.exception)
    #
    #         team = cast(Team, team_candidate)
    #
    #
    #     except Exception as ex:
    #         return ValidationResult.failure(
    #             InvalidTeamException(ex=ex, message=f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}")
    #         )