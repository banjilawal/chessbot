# src/chess/owner/model/validator/factory.py

"""
Module: chess.owner.model.validator.owner
Author: Banji Lawal
Created: 2025-10-22
Version: 1.0.0
"""

from typing import Tuple, Type, cast, TypeVar, Any

from chess.team import Team, RosterNumberOutOfBoundsException
from chess.rank import Bishop, King, Knight, Pawn, Queen, Rook, knight
from chess.system import IdValidator, NameValidator, LoggingLevelRouter, ValidationResult, Validator
from chess.piece import (
    NullAttackException, NullPieceException, Piece, AttackMissingCoordStackException,
    AttackMissingDiscoveryListException,
    AttackRankOutOfBoundsException, AttackRosterNumberIsNullException, AttackTeamFieldIsNullException,
    UnregisteredTeamMemberException
)

T = TypeVar('T')


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
            
            # With AutoId decorator, the ID check should never fail. It might not be necessary anymore.
            id_validation = IdValidator.validate(piece.id)
            if id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            # This is really minimal checking. `Piece` object names have format:
            # [color_letter][rank_symbol]-[value_in_quota]
            # Next step is use regexp to ensure the name fits the pattern and create a new rollback_exception for that.
            name_validation = NameValidator.validate(piece.name)
            if name_validation.is_failure():
                return ValidationResult.failure(name_validation.exception)
            
            # A `Piece` instance must have its `team` consistency set. This immutable consistency should have been set during
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
            
            if not isinstance(piece.rank, PieceValidator.VALID_RANKS):
                return ValidationResult.failure(
                    PieceRankOutOfBoundsException("{method}: {PieceRankOutOfBoundsException.DEFAULT_MESSAGE}")
                )
            
            # This test will have to be removed because a valid owner that has been captured is taken of
            # its team's roster and put on its enemy's hostage list.
            # team = owner.team
            # if owner not in team.roster:
            #   return ValidationResult(rollback_exception=UnregisteredTeamMemberException(
            #     f"{method}: {UnregisteredTeamMemberException.DEFAULT_MESSAGE}"
            #   ))
            
            if piece.positions is None:
                return ValidationResult.failure(
                    PieceMissingCoordStackException(f"{method}: {AttackMissingCoordStackException.DEFAULT_MESSAGE}")
                )
            
            if piece.discoveries is None:
                return ValidationResult.failure(
                    PieceMissingDiscoveriesException(f"{method}: {PieceMissingDiscoveriesException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(piece)
        
        except Exception as e:
            return ValidationResult(exception=e)
