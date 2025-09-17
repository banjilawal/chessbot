from typing import Generic, TypeVar, cast

from assurance.exception.invalid_id import IdValidationException
from chess.piece.exception.invalid_piece import PieceValidationException
from assurance.exception.invalid_request import OccupationRequestValidationException
from chess.square.exception import SquareValidationException
from chess.action.outcome import ActionOutcome
from chess.common.id_validator import IdValidator
from chess.piece.validator import PieceValidator
from chess.square import Square
from chess.common.emit import id_emitter
from chess.action.validators.base import RequestValidator
from chess.square.square_validator import SquareValidator
from chess.common.permit import Event
from chess.action.null_occupation_request import NullOccupationRequestException
from chess.exception.occupation.occupy import OccupiedBySelfException
from chess.exception.piece_exception import AttackingKingException
from chess.action.send import OccupationRequest
from chess.piece.piece import KingPiece, Piece

T = TypeVar('T')

class OccupationRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> ActionOutcome:
        entity = "OccupySquare"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an OccupySquare meets specifications:
            - Not null
            - id does not validator
            - actor is a valid chess piece
            - target is a valid square
        If a condition is not met an OccupationRequestValidationException will be thrown.

        Argument:
            t (OccupySquare): occupationRequest to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                OccupationRequestValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullOccupationRequestException: if t is null   

            IdValidationException: if invalid id
            PieceValidationException: if t.actor fails validator
            SquareValidationException: if it.target fails validator
            
            OccupiedBySelfException: if actor already occupies the square
            AttackingKingException: if the target square is occupied by an enemy king
            FriendlyOccupantException: if the target square is occupied by a friendly

            OccupationRequestValidationException: Wraps any preceding exceptions      
        """
        try:
            outcome_id = id_emitter.outcome_id
            if t is None:
                raise NullOccupationRequestException(f"{method} {NullOccupationRequestException.DEFAULT_MESSAGE}")

            if not isinstance(t, OccupationRequest):
                raise TypeError(f"{method} Expected an OccupySquare, got {type(t).__name__}")

            occupation_request = cast(OccupationRequest, t)

            id_validation = IdValidator.validate(occupation_request.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            piece_validation = PieceValidator.validate(occupation_request.actor)
            if not piece_validation.is_success():
                raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")

            square_validation = SquareValidator.validate(occupation_request.target)
            if not square_validation.is_success():
                raise SquareValidationException(f"{method}: {SquareValidationException.DEFAULT_MESSAGE}")

            piece = cast(Piece, piece_validation.payload)
            target_square = cast(Square, square_validation.payload)

            if target_square.coord == piece.current_position:
                raise OccupiedBySelfException(f"{method}: {OccupiedBySelfException.DEFAULT_MESSAGE}")

            occupant = target_square.occupant
            if occupant is None:
                return ActionOutcome(
                    outcome_id=outcome_id,
                    request=occupation_request,
                    event=Event.OCCUPATION
                )

            if occupant is not None and not piece.is_enemy(occupant):
                return ActionOutcome(
                    outcome_id=outcome_id,
                    request=occupation_request,
                    event=Event.RECORD_ENCOUNTER
                )
                # raise FriendlyOccupantException(f"{method}: {FriendlyOccupantException.DEFAULT_MESSAGE}")

            if occupant is not None and isinstance(occupant, KingPiece):
                raise AttackingKingException(f"{method}: {AttackingKingException.DEFAULT_MESSAGE}")

            return ActionOutcome(outcome_id=outcome_id, request=occupation_request, event=Event.ATTACK)

        except (
            TypeError,
            PieceValidationException,
            SquareValidationException,
            NullOccupationRequestException
        ) as e:
            raise OccupationRequestValidationException(
                f"{method}: {OccupationRequestValidationException.DEFAULT_MESSAGE}"
            ) from e
