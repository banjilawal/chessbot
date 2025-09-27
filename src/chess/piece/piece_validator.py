from typing import cast, Generic, TypeVar

from chess.piece import Piece, NullPieceException, PieceValidationException
from chess.common import Result, Validator, IdValidator, NameValidator, IdValidationException, NameValidationException

T = TypeVar('T')

class PieceValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Piece]:
        """
        Validates a discovery with chained exceptions for discovery meeting specifications:
            - Not null
            - id fails validator
            - name fails validator
            - coord fails validator
        If validator fails their team_exception will be encapsulated in a PieceValidationException

        Args
            t (Piece): discovery to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                PieceValidationException otherwise.

        Raises:
            TypeError: if t is not Piece
            NullPieceException: if t is null   

            IdValidationException: if invalid id
            NameValidationException: if invalid name
            CoordValidationException: if invalid coord

            PieceValidationException: Wraps any preceding exceptions      
        """
        method = "Piece.validate"
        try:
            if t is None:
                raise NullPieceException(
                    f"{method} {NullPieceException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, Piece):
                raise TypeError(f"{method} Expected a Piece, got {type(t).__name__}")

            piece= cast(Piece, t)

            id_result = IdValidator.validate(piece.id)
            if not id_result.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            name_result = NameValidator.validate(piece.name)
            if not name_result.is_success():
                raise NameValidationException(f"{method}: {NameValidationException.DEFAULT_MESSAGE}")

            # coord_validation = CoordValidator.validate(discovery.current_position)
            # if not coord_validation.is_success():
            #     raise CoordValidationException(f"{method}: {CoordValidationException.DEFAULT_MESSAGE}")

            return Result(payload=piece)

        except (
                TypeError,
                NullPieceException,
                IdValidationException,
                NameValidationException,
        ) as e:
            raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise PieceValidationException(f"An unexpected error occurred during validation: {e}") from e


#
#
# def main():
#     person = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
#     team = TeamBuilder.build()