from typing import Generic, cast

from assurance.exception.validation.coord_stack import CoordinateStackValidationException
from assurance.result.base import Result
from assurance.validators.coord import CoordinateValidator
from assurance.validators.base import Validator, T
from chess.exception.coord_stack import InconsistentCurrentCoordinateException

from chess.exception.stack import CorruptedStackException, StackSizeConflictException

from chess.exception.null.coord_stack import NullCoordinateStackException
from chess.geometry.coordinate.stack import CoordinateStack


class CoordinateStackValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[CoordinateStack]:
        entity = "CoordinateStack"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a new CoordinateStack meets requirements:
            - Not null
            - CoordinateStack.items is not null
            - CoordinateStack.current_coordinate is either null or meets CoordinateValidator
            - if CoordinateStack.is_empty() is True then current_coordinate.size == 0
            - if CoordinateStack.is_empty() is False then current_coordinate is not null
            - If CoordinateStack.is_empty() then current_coordinate is null
            
        Do not test for pushing or popping coordinates here. They might change state unexpectedly.
        Those operations are tested in their own unit tests.
        If any validators state fails their exception will be encapsulated in a 
        CoordinateStackValidationException
            
        Args
            t (CoordinateStack): coordinate_stack to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if the validator is satisfied,
                        CoordinateStackValidationException otherwise.
        
        Raises:
            NullCoordinateStackException: if t is null
            TypeError: if t is not CoordinateStack
            
            RowOutOfBoundsException: If coordinate.row is outside the range 
                (0, ROW_SIZE - 1) inclusive
                
            IsEmptyStackResultConflictsWithSizeException: If CoordinateStack.is_empty()
                result conflicts with size()
                
            EmptyStackCurrentCoordinateValueMismatch: If CoordinateStack.is_empty()
                result conflicts with current_coordinate value
                
            InternalStackDataStructureException: If CoordinateStack.items is null
            
            CurrentCoordinateInconsistentStateException`: If current_coordinate
                does not meet CoordinateValidator
.
            CoordinateStackValidationException: Wraps any
                (preceding exceptions)
                
        """
        try:
            if t is None:
                raise NullCoordinateStackException(
                    f"{method} {NullCoordinateStackException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, CoordinateStack):
                raise TypeError(f"{method} Expected a CoordinateStack, got {type(t).__name__}")

            coords  = cast(CoordinateStack, t)

            if coords.size() > 0 and coords.is_empty():
                raise StackSizeConflictException(f"{method}: {StackSizeConflictException.DEFAULT_MESSAGE}")

            if coords.is_empty() and coords.current_coordinate is not None:
                raise InconsistentCurrentCoordinateException(
                    f"{method}: {InconsistentCurrentCoordinateException.DEFAULT_MESSAGE}"
                )

            if coords.current_coordinate is None and not coords.is_empty():
                raise InconsistentCurrentCoordinateException(
                    f"{method} {InconsistentCurrentCoordinateException.DEFAULT_MESSAGE}"
                )

            if coords.items is None:
                raise CorruptedStackException(f"{method} {CorruptedStackException.DEFAULT_MESSAGE}")

            current_coord = coords.current_coordinate

            if (current_coord is not None and
                    not CoordinateValidator.validate(current_coord).is_success()):
                raise InconsistentCurrentCoordinateException(
                    f"{method} {InconsistentCurrentCoordinateException.DEFAULT_MESSAGE}"
                )

            return Result(payload=coords)

        except (
            TypeError,
            NullCoordinateStackException,
            StackSizeConflictException,
            InconsistentCurrentCoordinateException
        ) as e:
            raise CoordinateStackValidationException(
                f"{method}: {CoordinateStackValidationException.DEFAULT_MESSAGE}"
            ) from e
#
#
# def main():
#     coordinate_stack = CoordinateStack()
#     validator_result = CoordinateStackValidatorvalidate(coordinate_stack)
#     if validator_result.is_success():
#         print("CoordinateStack validator satisfied.")
#     else:
#         print("CoordinateStack validator not satisfied.")
#
#
# if __name__ == "__main__":
#     main()