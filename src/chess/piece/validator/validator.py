# src/chess/piece/validator/validator.py

"""
Module: chess.piece.validator.validator
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Type, Any, cast

from chess.coord import CoordService
from chess.piece import (
    Piece, InvalidPieceException, NullPieceException, PieceNullCoordStackException,
    PieceRosterNumberIsNullException
)
from chess.rank import RankService
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult, Validator
from chess.team import RosterNumberOutOfBoundsException, Team, TeamService


# class PieceValidator(Validator[Piece]):
#     VALID_RANKS: tuple[Type, ...] = (King, Queen, Bishop, Knight, Rook, Pawn)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            team_service: TeamService = TeamService(),
            rank_service: RankService = RankService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService()
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
            identity_validation = identity_service.validate_identity(
                id_candidate=piece.id,
                name_candidate=piece.name
            )
            if identity_validation.is_failure():
                return ValidationResult.failure(identity_validation.exception)
            
            team_validation = team_service.validator.validate(piece.team)
            if team_validation.is_failure():
                return ValidationResult.failure(team_validation.exception)
            
            rank_validation = rank_service.validator.validate(piece.rank)
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
            
            if
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
            team_service: TeamService = TeamService(),
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
        
