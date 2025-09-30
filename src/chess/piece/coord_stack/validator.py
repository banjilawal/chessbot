from typing import Generic, cast


from chess.coord import CoordValidator
from chess.piece import CoordStack, CoordStackValidationException, NullCoordStackException
from chess.common import Validator, Result,ResultPayloadConflictException
from chess.exception import InconsistentCurrentCoordException


__all__ = [
    'CoordStackValidator'
]

class CoordStackValidator(Validator):

    @staticmethod
    def validate(t: CoordValidator) -> Result[CoordinateStack]:
        """
        Validates a CoordStack meets requirements:
            - Not null
            - CoordStack.items is not null
            - CoordStack.current_coordinate is null if the stack is empty, otherwise is a validated Coord
            - if CoordStack.is_empty() is True then current_coordinate.size == 0
            - if CoordStack.is_empty() is False then current_coordinate is not null
            - If CoordStack.is_empty() then current_coordinate is null
        Any failed requirement raise an team_exception wrapped in a CoordStackValidationException      

        Validation tests do not change state so pushes and pops are:
            - Tested in unit tests
            - Piece life-cycles and flows.

        Args
            t (CoordStack): coordinate_stack to validate

         Returns:
             Result[T]: Result instance containing a validated coordinate_stack as payload if validations 
             are satisfied, CoordStackValidationException otherwise.

        Raises:
            TypeError: if t is not CoordStack
            NullCoordStackException: if t is null

            InternalStackDataStructureException: If CoordStack.items is null
            InconsistentCurrentCoordException: If current_coordinate does not meet CoordValidator

            CoordStackValidationException: Wraps any preceding exceptions
        """
        method = "CoordinateStackValidator.validate"

        try:
            if t is None:
                raise NullCoordStackException(
                    f"{method} {NullCoordStackException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, CoordStack):
                raise TypeError(f"{method} Expected a CoordStack, got {type(t).__name__}")

            coords  = cast(CoordStack, t)

            if coords.size() > 0 and coords.is_empty():
                raise StackSizeConflictException(f"{method}: {StackSizeConflictException.DEFAULT_MESSAGE}")

            if coords.is_empty() and coords.current_coord is not None:
                raise InconsistentCurrentCoordException(
                    f"{method}: {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
                )

            if coords.current_coord is None and not coords.is_empty():
                raise InconsistentCurrentCoordException(
                    f"{method} {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
                )

            if coords.items is None:
                raise CorruptedStackException(f"{method} {CorruptedStackException.DEFAULT_MESSAGE}")

            current_coord = coords.current_coord

            if (current_coord is not None and
                    not CoordValidator.validate(current_coord).is_success()):
                raise InconsistentCurrentCoordException(
                    f"{method} {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
                )

            return Result(payload=coords)

        except (
                TypeError,
                NullCoordStackException,
                StackSizeConflictException,
                InconsistentCurrentCoordException
        ) as e:
            raise CoordStackValidationException(
                f"{method}: {CoordStackValidationException.DEFAULT_MESSAGE}"
            ) from e
#
#
# def main():
#     coordinate_stack = CoordStack()
#     validator_result = CoordinateStackValidatorvalidate(coordinate_stack)
#     if validator_result.is_success():
#         print("CoordStack validator satisfied.")
#     else:
#         print("CoordStack validator not satisfied.")
#
#
# if __name__ == "__main__":
#     main()