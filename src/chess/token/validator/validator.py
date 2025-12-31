# src/chess/token/validator/validator.py

"""
Module: chess.token.validator
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Any, cast

from chess.rank import RankCertifier
from chess.coord import CoordService
from chess.team import RosterNumberOutOfBoundsException, Team, TeamCertifier
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.token import (
    Token, TokenValidationFailedException, NullTokenException, TokenNullCoordStackException, TokenRosterNumberIsNullException
)


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
            team_service: TeamCertifier = TeamCertifier(),
            rank_service: RankCertifier = RankCertifier(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService()
    ) -> ValidationResult[Token]:
        """"""
        method = "Token.validate"
        
        try:
            # Prevents a validation `Token` being accepted as method argument.
            if candidate is None:
                return ValidationResult.failure(
                    NullTokenException(
                        f"{method}:"
                        f" {NullTokenException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, Token):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected Token,, got {type(candidate).__name__} instead."
                    )
                )
            
            token = cast(Token, candidate)
            identity_validation = identity_service.validate_identity(
                id_candidate=token.id,
                name_candidate=token.name
            )
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            team_validation = team_service.item_validator.validate(token.team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            roster_number_validation = team_service.item_validator
            
            rank_validation = rank_service.item_validator.validate(token.rank)
            if rank_validation.is_failure():
                return ValidationResult.failure(rank_validation.exception)
            
            if token.roster_number is None:
                return ValidationResult.failure(
                    TokenRosterNumberIsNullException(
                        f"{method}: "
                        f"{TokenRosterNumberIsNullException.DEFAULT_MESSAGE}"
                    )
                )
            
            if token.roster_number < 1 or token.roster_number > Team.MAX_ROSTER_SIZE:
                return ValidationResult.failure(
                    RosterNumberOutOfBoundsException(
                        f"{method}: "
                        f"{RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if token.positions is None:
                return ValidationResult.failure(
                    TokenNullCoordStackException(
                        f"{method}: "
                        f"{TokenNullCoordStackException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(token)
        
        except Exception as ex:
            return ValidationResult.failure(
                TokenValidationFailedException(
                    ex=ex,
                    message=f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def token_is_disabled(cls, candidate: Any) -> ValidationResult[bool]:
        """"""
        method = "TokenValidator.token_is_disabled"
        try:
            token_validation = cls.validate(candidate)
            if token_validation.is_failure():
                return ValidationResult.failure(token_validation.exception)
        
        except Exception as ex:
            return ValidationResult.failure(
                TokenValidationFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{TokenValidationFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_token_is_actionable(
            cls, candidate: Any,
            team_service: TeamCertifier = TeamCertifier(),
            board_service: BoardService = BoardService(),
    ) -> ValidationResult[Token]:
        """"""
        method = "TokenValidator.verify_active_token"
        try:
            token_validation = cls.validate(candidate)
            if token_validation.is_failure():
                return ValidationResult.failure(token_validation.exception)
            
            token = cast(Token, token_validation.payload)
            
            team = token.team
            if token not in team.roster:
                return ValidationResult.failure(
                    ActiveTokenMissingFromTeamRoster(f"{method} {ActiveTokenMissingFromTeamRoster.DEFAULT_MESSAGE}")
                )
            
            if isinstance(token, KingToken) and cast(KingToken, token).is_checkmated:
                return ValidationResult.failure(
                    CheckmatedKingException(f"{method} {CheckmatedKingException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(token, CombatantToken) and cast(CombatantToken, token).captor is not None:
                return ValidationResult.failure(
                    CapturedTokenException(f"{method}: {CapturedTokenException.DEFAULT_MESSAGE}")
                )
            
            if token.current_position is None or token.postions.is_empty():
                return ValidationResult.failure(
                    TokenRequiresInitialPlacementException(
                        f"{method}: {TokenRequiresInitialPlacementException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult.success(token)
        
        except Exception as e:
            return ValidationResult.failure(
                TokenValidationFailedException(f"{method}: {TokenValidationFailedException.DEFAULT_MESSAGE}", e)
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def token_bound_to_team_roster(
            cls,
            team: Team,
            token: Token,
            token_validator: type[TokenValidator] = TokenValidator
    ) -> ValidationResult[(Team, Token)]:
        try:
            team_validation = cls.validate(team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            token_validation = token_validator.validate_token_is_actionable(token)
            if token_validation.is_failure():
                return ValidationResult.failure(token_validation.exception)
            
            if token.team != team:
                return ValidationResult.failure()
            
            if (
                    (isinstance(token, CombatantToken) and cast(CombatantToken, token).captor is not None) or
                    isinstance(token, KingToken) and cast(KingToken, token).is_checkmated
            ):
                return ValidationResult.failure()
            
            if token not in team.roster:
                return ValidationResult.failure()
            
            return ValidationResult.success((team, token))
        except Exception as ex:
            return ValidationResult.failure(ex)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def token_bound_to_team_hostages(
            cls,
            team: Team,
            token: Token,
            token_validator: type[TokenValidator] = TokenValidator
    ) -> ValidationResult[(Team, Token)]:
        try:
            team_validation = cls.validate(team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            token_validation = token_validator.validate_token_is_actionable(token)
            if token_validation.is_failure():
                return ValidationResult.failure(token_validation.exception)
            
            if token.team == team:
                return ValidationResult.failure()
            
            if token not in team.hostages:
                return ValidationResult.failure()
            
            return ValidationResult.success((team, token))
        except Exception as ex:
            return ValidationResult.failure(ex)
    
    @classmethod
    
    LoggingLevelRouter.monitor
    
    def validate_token_registration(
            cls,
            token_candidate: Any,
            team_candidate: Any,
            token_validator: TokenValidator = TokenValidator(),
            team_data_service: TeamDataService = TeamDataService(),
    ) -> ValidationResult(Team, Token):
        method = "TeamValidator.validate_token_registration"
        try:
            token_validation = token_validator.validate(token_candidate)
            if token_validation.is_failure():
                return ValidationResult.failure(token_validation.exception)
            
            token = cast(Token, token_candidate)
            
            team_validation = cls.validate(team_candidate)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            team = cast(Team, team_candidate)
        
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTeamException(ex=ex, message=f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}")
            )