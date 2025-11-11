# src/chess/owner/model/validator/factory.py

"""
Module: chess.owner.model.validator.owner
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Type, Any, cast

from chess.domain import PieceWithNoStartingPlacementException
from chess.king import KingPiece
from chess.pawn import ActorPlacementRequiredException
from chess.piece.model.exception import CapturedPieceException, CheckmatedKingException
from chess.team import Team, RosterNumberOutOfBoundsException
from chess.rank import Bishop, King, Knight, Pawn, Queen, RankValidatorFactory, Rook, knight
from chess.system import IdValidator, NameValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
    CombatantPiece, NullAttackException, NullPieceException, Piece, AttackMissingCoordStackException,
    AttackMissingDiscoveryListException,
    AttackRankOutOfBoundsException, AttackRosterNumberIsNullException, AttackTeamFieldIsNullException,
    PieceNullCoordStackException, PieceRequiresInitialPlacementException, PieceRosterNumberIsNullException,
    PieceTeamFieldIsNullException,
    UnregisteredTeamMemberException
)
from chess.travel.attack.exception import CapturePieceException


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
                    NullPieceException(f"{method} {NullPieceException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Piece):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected team Piece, got {type(candidate).__name__}")
                )
            
            # For safety cast the candidate to a `Piece` instance.
            piece = cast(Piece, candidate)
            

            id_validation = IdValidator.validate(piece.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            # This is really minimal checking. `Piece` object names have format:
            # [color_letter][rank_symbol]-[value_in_quota]
            # Next step is use regexp to ensure the visitor_name fits the pattern and create a new rollback_exception for that.
            name_validation = NameValidator.validate(piece.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            # A `Piece` instance must have its `team_name` consistency set. This immutable consistency should have been set during
            # the build. If it's null there might be service loss or corruption.
            if piece.team is None:
                return ValidationResult.failure(
                    PieceTeamFieldIsNullException(f"{method}: {PieceTeamFieldIsNullException.DEFAULT_MESSAGE}")
                )
            
            if piece.roster_number is None:
                return ValidationResult.failure(
                    PieceRosterNumberIsNullException(f"{method}: {PieceRosterNumberIsNullException.DEFAULT_MESSAGE}")
                )
            
            if piece.roster_number < 1 or piece.roster_number > Team.MAX_ROSTER_SIZE:
                return ValidationResult.failure(
                    RosterNumberOutOfBoundsException(f"{method}: {RosterNumberOutOfBoundsException.DEFAULT_MESSAGE}")
                )
            
            rank_validation = RankValidatorFactory.validate(piece.rank)
            if rank_validation.is_failure():
                return ValidationResult.failure(rank_validation.exception)

            
            if piece.positions is None:
                return ValidationResult.failure(
                    PieceNullCoordStackException(f"{method}: {PieceNullCoordStackException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(piece)
        
        except Exception as e:
            return ValidationResult(exception=e)
        
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_active_piece(cls, candidate: Any) -> ValidationResult[Piece]:
        """"""
        method = "PieceValidator.validate_piece_is_free"
        try:
            piece_validation = cls.validate(candidate)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            piece = cast(Piece, piece_validation.payload)
            
            team = piece.team
            if piece not in team.roster:
                return ValidationResult.failure(
                    UnregisteredTeamMemberException(f"{method} {UnregisteredTeamMemberException.DEFAULT_MESSAGE}")
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
            return ValidationResult.failure(e)
        
