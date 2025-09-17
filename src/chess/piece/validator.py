from typing import cast, Generic

from chess.piece import Piece, NullPieceException,
from chess.common import Validator, Result
from chess.exception import


class PieceValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[Piece]:
        entity = "Piece"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a square with chained exceptions for square meeting specifications:
            - Not null
            - id fails validator
            - name fails validator
            - coord fails validator
        If validators fails their team_exception will be encapsulated in a SquareValidationException

        Args
            t (Square): square to validate

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
                SquareValidationException otherwise.

        Raises:
            TypeError: if t is not Square
            NullSquareException: if t is null   

            IdValidationException: if invalid id
            NameValidationException: if invalid name
            CoordValidationException: if invalid coord

            SquareValidationException: Wraps any preceding exceptions      
        """
        try:
            if t is None:
                raise NullPieceException(
                    f"{method} {NullPieceException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, Piece):
                raise TypeError(f"{method} Expected a Square, got {type(t).__name__}")

            piece= cast(Piece, t)

            id_result = IdValidator.validate(piece.id)
            if not id_result.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            name_result = NameValidator.validate(piece.name)
            if not name_result.is_success():
                raise NameValidationException(f"{method}: {NameValidationException.DEFAULT_MESSAGE}")

            # coord_validation = CoordValidator.validate(piece.current_position)
            # if not coord_validation.is_success():
            #     raise CoordValidationException(f"{method}: {CoordValidationException.DEFAULT_MESSAGE}")

            return Result(payload=piece)

        except (
                TypeError,
                NullPieceException,
                IdValidationException,
                NameValidationException,
                # CoordValidationException
        ) as e:
            raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}") from e



def main():
    person = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
    side = TeamBuilder.build()