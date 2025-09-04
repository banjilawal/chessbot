from typing import Generic, cast

from assurance.exception.validation.coord_stack import CoordStackValidationException
from assurance.result.base import Result
from assurance.validators.coord import CoordValidator
from assurance.validators.base import Validator, T
from chess.exception.coord_stack import InconsistentCurrentCoordinateException

from chess.exception.stack import CorruptedStackException, StackSizeConflictException

from chess.exception.null.coord_stack import NullCoordStackException
from chess.token.model.coord import CoordinateStack


class CoordStackValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[CoordinateStack]:
        entity = "CoordStack"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a CoordStack meets requirements:
            - Not null
            - CoordStack.items is not null
            - CoordStack.current_coordinate is null if the stack is empty, otherwise is a validated Coord
            - if CoordStack.is_empty() is True then current_coordinate.size == 0
            - if CoordStack.is_empty() is False then current_coordinate is not null
            - If CoordStack.is_empty() then current_coordinate is null
        Any failed requirement raise an exception wrapped in a CoordStackValidationException      

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
            InconsistentCurrentCoordinateException: If current_coordinate does not meet CoordValidator

            CoordStackValidationException: Wraps any preceding exceptions
        """
        try:
            if t is None:
                raise NullCoordStackException(
                    f"{method} {NullCoordStackException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, CoordinateStack):
                raise TypeError(f"{method} Expected a CoordStack, got {type(t).__name__}")

            coords  = cast(CoordinateStack, t)

            if coords.size() > 0 and coords.is_empty():
                raise StackSizeConflictException(f"{method}: {StackSizeConflictException.DEFAULT_MESSAGE}")

            if coords.is_empty() and coords.current_coord is not None:
                raise InconsistentCurrentCoordinateException(
                    f"{method}: {InconsistentCurrentCoordinateException.DEFAULT_MESSAGE}"
                )

            if coords.current_coord is None and not coords.is_empty():
                raise InconsistentCurrentCoordinateException(
                    f"{method} {InconsistentCurrentCoordinateException.DEFAULT_MESSAGE}"
                )

            if coords.items is None:
                raise CorruptedStackException(f"{method} {CorruptedStackException.DEFAULT_MESSAGE}")

            current_coord = coords.current_coord

            if (current_coord is not None and
                    not CoordValidator.validate(current_coord).is_success()):
                raise InconsistentCurrentCoordinateException(
                    f"{method} {InconsistentCurrentCoordinateException.DEFAULT_MESSAGE}"
                )

            return Result(payload=coords)

        except (
                TypeError,
                NullCoordStackException,
                StackSizeConflictException,
                InconsistentCurrentCoordinateException
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