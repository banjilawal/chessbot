from typing import Generic, TypeVar, cast


from chess.piece import Piece, PieceValidator, PieceValidationException
from chess.square import Square, SquareValidator, SquareValidationException
from chess.common import Validator, Result, IdValidator, IdValidationException
from chess.operation.occupation import (
    OccupationDirective,
    NullOccupationDirectiveException,
    AutoOccupationException,
    InvalidOccupationDirectiveException
)

T = TypeVar('T')

class OccupationDirectiveValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[OccupationDirective]:
        """
        Validates an OccupationDirective meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess subject
            - `target` is a valid square
        Any validation failure raises an `InvalidOccupationDirectiveException`.

        Argument:
            `t` (`OccupationDirective`): `occupationDirective `to validate

         Returns:
             `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
                `InvalidOccupationDirectiveException` otherwise.

        Raises:
            `TypeError`: if `t` is not OperationDirective
            `NullOccupationDirectiveException`: if `t` is null

            `IdValidationException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `SquareValidationException`: if `target` fails validator

            `AutoOccupationException`: if target already occupies the square
            `KingAttackException`: if the target square is occupied by an enemy king

            `InvalidOccupationDirectiveException`: Wraps any preceding exceptions
        """
        method = "OccupationDirective.validate"

        try:
            if t is None:
                raise NullOccupationDirectiveException(
                    f"{method}: {NullOccupationDirectiveException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, OccupationDirective):
                raise TypeError(f"{method} Expected an OccupationDirective, got {type(t).__name__}")

            directive = cast(OccupationDirective, t)

            id_validation = IdValidator.validate(directive.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            piece_validation = PieceValidator.validate(directive.actor)
            if not piece_validation.is_success():
                raise PieceValidationException(f"{method}: {PieceValidationException.DEFAULT_MESSAGE}")
            piece = cast(Piece, directive.actor)

            square_validation = SquareValidator.validate(directive.resource)
            if not square_validation.is_success():
                raise SquareValidationException(f"{method}: {SquareValidationException.DEFAULT_MESSAGE}")
            square = cast(Square, directive.resource)

            if square.coord == piece.current_position:
                raise AutoOccupationException(f"{method}: {AutoOccupationException.DEFAULT_MESSAGE}")
            
            return Result(payload=directive)

        except (
            TypeError,
            IdValidationException,
            PieceValidationException,
            SquareValidationException,
            NullOccupationDirectiveException,
            AutoOccupationException
        ) as e:
            raise InvalidOccupationDirectiveException(
                f"{method}: {InvalidOccupationDirectiveException.DEFAULT_MESSAGE}"
            ) from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise InvalidOccupationDirectiveException(f"An unexpected error occurred during validation: {e}") from e

