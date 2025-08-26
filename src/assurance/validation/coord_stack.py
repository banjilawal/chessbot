from typing import Generic, cast

from assurance.exception.validation.coord_stack import CoordinateStackValidationException
from assurance.exception.validation.coord import CoordinateValidationException
from assurance.result.base import Result
from assurance.validation.coord import CoordinateSpecification
from assurance.validation.base import Specification, T
from chess.exception.coordinate_stack.conflict import IsEmptyStackResultConflictsWithSizeException
from chess.exception.coordinate_stack.current import CurrentCoordinateInconsistentStateException
from chess.exception.coordinate_stack.internal_structure import InternalStackDataStructureException
from chess.exception.coordinate.row import RowOutOfBoundsException
from chess.exception.coordinate_stack.mismatch import EmptyStackCurrentCoordinateValueMismatch
from chess.exception.null.coord import NullCoordinateException
from chess.exception.null.coord_stack import NullCoordinateStackException
from chess.geometry.coordinate.coord_stack import CoordinateStack


class CoordinateStackSpecification(Specification):


    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[CoordinateStack]:
        method = "CoordinateSpecification.is_satisfied_by"

        """
        Validates a new CoordinateStack meets specifications:
            - Not null
            - CoordinateStack.items is not null
            - CoordinateStack.current_coordinate is either null or meets CoordinateSpecification
            - if CoordinateStack.is_empty() is True then current_coordinate.size == 0
            - if CoordinateStack.is_empty() is False then current_coordinate is not null
            - If CoordinateStack.is_empty() then current_coordinate is null
            
        Do not test for pushing or popping coordinates here. They might change state unexpectedly.
        Those operations are tested in their own unit tests.
        If any validation check fails their exception will be encapsulated in a 
        CoordinateStackValidationException
            
        Args
            t (CoordinateStack): coordinate_stack to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if the specification is satisfied,
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
                does not meet CoordinateSpecification
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
                raise IsEmptyStackResultConflictsWithSizeException(
                    f"{method} {IsEmptyStackResultConflictsWithSizeException.DEFAULT_MESSAGE}"
                )

            if coords.is_empty() and coords.current_coordinate is not None:
                raise EmptyStackCurrentCoordinateValueMismatch(
                    f"{method} Stack is empty but current_coordinate is not null. "
                )

            if coords.current_coordinate is None and not coords.is_empty():
                raise EmptyStackCurrentCoordinateValueMismatch(
                    f"{method} current_coordinate is null but stack is not empty. "
                )

            if coords.items is None:
                raise InternalStackDataStructureException(
                    f"{method} {InternalStackDataStructureException.DEFAULT_MESSAGE}"
                )

            current_coord = coords.current_coordinate
            if (current_coord is not None and
                    CoordinateSpecification.is_satisfied_by(current_coord).is_failure()):
                raise CurrentCoordinateInconsistentStateException(
                    f"{method} {CurrentCoordinateInconsistentStateException.DEFAULT_MESSAGE}"
                )


            return Result(payload=coords)

        except (
            TypeError,
            NullCoordinateException,
            IsEmptyStackResultConflictsWithSizeException,
            EmptyStackCurrentCoordinateValueMismatch,
            InternalStackDataStructureException,
            CurrentCoordinateInconsistentStateException
        ) as e:
            raise CoordinateStackValidationException(
                f"{method} CoordinateStack validation failed"
            ) from e
#
#
# def main():
#     coordinate_stack = CoordinateStack()
#     specification_result = CoordinateStackSpecification.is_satisfied_by(coordinate_stack)
#     if specification_result.is_success():
#         print("CoordinateStack specification satisfied.")
#     else:
#         print("CoordinateStack specification not satisfied.")
#
#
# if __name__ == "__main__":
#     main()