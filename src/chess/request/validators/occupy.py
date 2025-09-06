from typing import Generic, TypeVar, cast

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.piece import PieceValidationException
from assurance.exception.validation.request import OccupationRequestValidationException
from assurance.exception.validation.square import SquareValidationException
from assurance.result.event import RequestOutcome
from assurance.validators.id import IdValidator
from assurance.validators.piece import PieceValidator
from chess.board.square import Square
from chess.creator.emit import id_emitter
from chess.request.validators.base import RequestValidator
from assurance.validators.square import SquareValidator
from chess.common.permit import Event
from chess.exception.null.request import NullOccupationRequestException
from chess.exception.occupy import OccupiedBySelfException, FriendlyOccupantException
from chess.exception.piece import AttackingKingException
from chess.request.occupy import OccupationRequest
from chess.token.model import KingPiece, Piece

T = TypeVar('T')

class OccupationRequestValidator(RequestValidator):

    @staticmethod
    def validate(t: Generic[T]) -> RequestOutcome:
        entity = "OccupationRequest"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an OccupationRequest meets specifications:
            - Not null
            - id does not validation
            - client is a valid chess piece
            - resource is a valid square
        If a condition is not met an OccupationRequestValidationException will be thrown.

        Argument:
            t (OccupationRequest): occupationRequest to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                OccupationRequestValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullOccupationRequestException: if t is null   

            IdValidationException: if invalid id
            PieceValidationException: if t.client fails validation
            SquareValidationException: if it.resource fails validation
            
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
                raise TypeError(f"{method} Expected an OccupationRequest, got {type(t).__name__}")

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
                return RequestOutcome(
                    outcome_id=outcome_id,
                    request=occupation_request,
                    event=Event.OCCUPATION
                )

            if occupant is not None and not piece.is_enemy(occupant):
                return RequestOutcome(
                    outcome_id=outcome_id,
                    request=occupation_request,
                    event=Event.RECORD_ENCOUNTER
                )
                # raise FriendlyOccupantException(f"{method}: {FriendlyOccupantException.DEFAULT_MESSAGE}")

            if occupant is not None and isinstance(occupant, KingPiece):
                raise AttackingKingException(f"{method}: {AttackingKingException.DEFAULT_MESSAGE}")

            return RequestOutcome(outcome_id=outcome_id, request=occupation_request,event=Event.ATTACK)

        except (
            TypeError,
            PieceValidationException,
            SquareValidationException,
            NullOccupationRequestException
        ) as e:
            raise OccupationRequestValidationException(
                f"{method}: {OccupationRequestValidationException.DEFAULT_MESSAGE}"
            ) from e
