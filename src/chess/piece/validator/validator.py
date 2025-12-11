# src/chess/piece/validator/validator.py

"""
Module: chess.piece.validator.validator
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Any, cast

from chess.rank import RankCertifier
from chess.coord import CoordService
from chess.team import RosterNumberOutOfBoundsException, Team, TeamCertifier
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
    Piece, InvalidPieceException, NullPieceException, PieceNullCoordStackException, PieceRosterNumberIsNullException
)

class PieceValidator(Validator[Piece]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Piece instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * PieceValidator

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
            idservice: IdentityService = IdentityService()
    ) -> ValidationResult[Piece]:
        """"""
        method = "Piece.validate"
        
        try:
            # Prevents a validation `Piece` being accepted as method argument.
            if candidate is None:
                return ValidationResult.failure(
                    NullPieceException(
                        f"{method}:"
                        f" {NullPieceException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance(candidate, Piece):
                return ValidationResult.failure(
                    TypeError(
                        f"{method}: "
                        f"Expected Piece, got {type(candidate).__name__} instead."
                    )
                )
            
            piece = cast(Piece, candidate)
            identity_validation = idservice.validate_identity(
                id_candidate=piece.id,
                name_candidate=piece.name
            )
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            team_validation = team_service.item_validator.validate(piece.team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            roster_number_validation = team_service.item_validator
            
            rank_validation = rank_service.item_validator.validate(piece.rank)
            if rank_validation.is_failure():
                return ValidationResult.failure(rank_validation.exception)
            
            

            if piece.roster_number is None:
                return ValidationResult.failure(
                    PieceRosterNumberIsNullException(
                        f"{method}: "
                        f"{PieceRosterNumberIsNullException.DEFAULT_MESSAGE}"
                    )
                )
            
            if piece.roster_number < 1 or piece.roster_number > Team.MAX_ROSTER_SIZE:
                return ValidationResult.failure(
                    RosterNumberOutOfBoundsException(
                        f"{method}: "
                        f"{RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            if piece.positions is None:
                return ValidationResult.failure(
                    PieceNullCoordStackException(
                        f"{method}: "
                        f"{PieceNullCoordStackException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(piece)

        except Exception as ex:
            return ValidationResult.failure(
                InvalidPieceException(
                    ex=ex,
                    message=f"{method}: {InvalidPieceException.DEFAULT_MESSAGE}"
                )
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def piece_is_disabled(cls, candidate: Any) -> ValidationResult[bool]:
        """"""
        method = "PieceValidator.piece_is_disabled"
        try:
            piece_validation = cls.validate(candidate)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)

        except Exception as ex:
            return ValidationResult.failure(
                InvalidPieceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{InvalidPieceException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_piece_is_actionable(
            cls, candidate: Any,
            team_service: TeamCertifier = TeamCertifier(),
            board_service: BoardService = BoardService(),
    ) -> ValidationResult[Piece]:
        """"""
        method = "PieceValidator.verify_active_piece"
        try:
            piece_validation = cls.validate(candidate)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            piece = cast(Piece, piece_validation.payload)
            
            team = piece.team
            if piece not in team.roster:
                return ValidationResult.failure(
                    ActivePieceMissingFromTeamRoster(f"{method} {ActivePieceMissingFromTeamRoster.DEFAULT_MESSAGE}")
                )
            
            if isinstance(piece, KingPiece) and cast(KingPiece, piece).is_checkmated:
                return ValidationResult.failure(
                    CheckmatedKingException(f"{method} {CheckmatedKingException.DEFAULT_MESSAGE}")
                )
            
            if isinstance(piece, CombatantPiece) and cast(CombatantPiece, piece).captor is not None:
                return ValidationResult.failure(
                    CapturedPieceException(f"{method}: {CapturedPieceException.DEFAULT_MESSAGE}")
                )
            
            if piece.current_position is None or piece.postions.is_empty():
                return ValidationResult.failure(
                   PieceRequiresInitialPlacementException(
                       f"{method}: {PieceRequiresInitialPlacementException.DEFAULT_MESSAGE}"
                  )
                )
            
            return ValidationResult.success(piece)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidPieceException(f"{method}: {InvalidPieceException.DEFAULT_MESSAGE}", e)
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
                InvalidTeamException(ex=ex, message=f"{method}: {InvalidTeamException.DEFAULT_MESSAGE}")
            )
