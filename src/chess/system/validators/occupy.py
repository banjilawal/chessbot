from typing import Generic, TypeVar, cast

from assurance.exception.validation.id import IdValidationException
from chess.piece.exception.invalid_piece import PieceValidationException
from assurance.exception.validation.request import OccupationRequestValidationException
from chess.square.exception.invalid import SquareValidationException
from assurance.result.event import CommandOutcome
from assurance.validators.id import IdValidator
from chess.piece.validator import PieceValidator
from chess.square import Square
from chess.creator.emit import id_emitter
from chess.system.validators.base import RequestValidator
from assurance.validators.square import SquareValidator
from chess.common.permit import Event
from chess.exception.null.request import NullOccupationRequestException
from chess.exception.occupy import OccupiedBySelfException
from chess.exception.exception import AttackingKingException
from chess.system.send import OccupationRequest
from chess.piece.piece import KingPiece, Piece

T = TypeVar('T')

class OccupationRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> CommandOutcome:
        entity = "OccupySquare"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an OccupySquare meets specifications:
            - Not null
            - id does not validator
            - client is a valid chess piece
            - resource is a valid square
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
            PieceValidationException: if t.client fails validator
            SquareValidationException: if it.resource fails validator
            
            OccupiedBySelfException: if client already occupies the square
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

            piece_validation = PieceValidator.validate(occupation_request.client)
            if not piece_validation.is_success():
                raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")

            square_validation = SquareValidator.validate(occupation_request.resource)
            if not square_validation.is_success():
                raise SquareValidationException(f"{method}: {SquareValidationException.DEFAULT_MESSAGE}")

            piece = cast(Piece, piece_validation.payload)
            target_square = cast(Square, square_validation.payload)

            if target_square.coord == piece.current_position:
                raise OccupiedBySelfException(f"{method}: {OccupiedBySelfException.DEFAULT_MESSAGE}")

            occupant = target_square.occupant
            if occupant is None:
                return CommandOutcome(
                    outcome_id=outcome_id,
                    request=occupation_request,
                    event=Event.OCCUPATION
                )

            if occupant is not None and not piece.is_enemy(occupant):
                return CommandOutcome(
                    outcome_id=outcome_id,
                    request=occupation_request,
                    event=Event.RECORD_ENCOUNTER
                )
                # raise FriendlyOccupantException(f"{method}: {FriendlyOccupantException.DEFAULT_MESSAGE}")

            if occupant is not None and isinstance(occupant, KingPiece):
                raise AttackingKingException(f"{method}: {AttackingKingException.DEFAULT_MESSAGE}")

            return CommandOutcome(outcome_id=outcome_id, request=occupation_request, event=Event.ATTACK)

        except (
            TypeError,
            PieceValidationException,
            SquareValidationException,
            NullOccupationRequestException
        ) as e:
            raise OccupationRequestValidationException(
                f"{method}: {OccupationRequestValidationException.DEFAULT_MESSAGE}"
            ) from e
