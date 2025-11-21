# src/chess/piece/collision.py

"""
Module: chess.piece.exception
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Type, Any, cast

from chess.king import KingPiece
from chess.piece.exception import CapturedPieceException, CheckmatedKingException, InvalidPieceException
from chess.team import Team, RosterNumberOutOfBoundsException
from chess.rank import Bishop, King, Knight, Pawn, Queen, RankValidatorFactory, Rook
from chess.system import IdValidator, NameValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
    CombatantPiece, NullPieceException, Piece, PieceNullCoordStackException, PieceRequiresInitialPlacementException, PieceRosterNumberIsNullException,
    PieceTeamFieldIsNullException,
    ActivePieceMissingFromTeamRoster
)


class PieceValidator(Validator[Piece]):
    VALID_RANKS: tuple[Type, ...] = (King, Queen, Bishop, Knight, Rook, Pawn)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[Piece]:
        """"""
        method = "Piece.validate"
        
        try:
            # Prevents a null `Piece` being accepted as method argument.
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
                        f"Expected team Piece, got {type(candidate).__name__} instead."
                    )
                )
            
            # For safety cast the candidate to a `Piece` instance.
            piece = cast(Piece, candidate)
            

            id_validation = IdValidator.validate(piece.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
        
            name_validation = NameValidator.validate(piece.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            if piece.team is None:
                return ValidationResult.failure(
                    PieceTeamFieldIsNullException(
                        f"{method}: "
                        f"{PieceTeamFieldIsNullException.DEFAULT_MESSAGE}")
                )
            
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
            
            rank_validation = RankValidatorFactory.validate(piece.rank)
            if rank_validation.is_failure():
                return ValidationResult.failure(rank_validation.exception)

            
            if piece.positions is None:
                return ValidationResult.failure(
                    PieceNullCoordStackException(
                        f"{method}: "
                        f"{PieceNullCoordStackException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(piece)

        except Exception as e:
            return ValidationResult.failure(
                InvalidPieceException(f"{method}: {InvalidPieceException.DEFAULT_MESSAGE}", e)
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_piece_is_actionable(cls, candidate: Any) -> ValidationResult[Piece]:
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
        
