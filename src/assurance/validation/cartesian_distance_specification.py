from typing import Generic, cast

from assurance.result.base_result import Result
from assurance.validation.coordinate_specification import CoordinateSpecification
from assurance.validation.specification import Specification, T
from assurance.validation.validation_exception import CoordinateValidationException
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coordinate.column_out_of_bounds import ColumnOutOfBoundsException
from chess.exception.coordinate.row_out_of_bounds import RowOutOfBoundsException
from chess.exception.null.cartesian_distance_null import NullCartesianDistanceException
from chess.exception.null.coordinate_null import NullCoordinateException
from chess.exception.null.null_column_exception import NullColumnException
from chess.exception.null.null_row_exception import NullRowException
from chess.geometry.coordinate.cartesian_distance import CartesianDistance
from chess.geometry.coordinate.coordinate import Coordinate


class CartesianDistanceSpecification(Specification):

    DEFAULT_MESSAGE = "CoordinateSpecification: Coordinate validation failed"

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> Result[CartesianDistance]:
        method = "CartesianDistanceSpecification.is_satisfied_by"

        """
        Validates a Cartesian distance between coordinates:
            - Not null
            - row is not null
            - row is within the bounds of the chess chessboard
            - column is not null
            - column is within the bounds of the chess chessboard
        If either validation fails their exception will be encapsulated in a CoordinateValidationException
            
        Args
            t (CoordinateDistance): CartesianDistance to validate
            
        Returns:
            bool: True if coordinate passes validation. In testing only ever returns
                true. It throws an exception if any validation condition is not met.
        
        Raises:

            NullCoordinateException: if t is null
            
            TypeError: if t is not Coordinate
            
            RowOutOfBoundsException: If coordinate.row is outside the range 
                (0, ROW_SIZE - 1) inclusive
                
            ColumnOutOfBoundsException: If coordinate.column is outside the range
                (0, COLUMN_SIZE - 1) inclusive
.
            CoordinateValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)
                
        """
        try:
            if t is None:
                raise NullCartesianDistanceException(
                    f"{method} NullCoordinateException.DEFAULT_MESSAGE"
                )

            if not isinstance(t, CartesianDistance):
                raise TypeError(f"{method} Expected a CartesianDistance, got {type(t).__name__}")

            cartesian_distance = cast(CartesianDistance, t)

            p_coord_spec_result = CoordinateSpecification.is_satisfied_by(cartesian_distance.p)
            if not p_coord_spec_result.is_success():
                raise p_coord_spec_result.exception

            q_coord_spec_result = CoordinateSpecification.is_satisfied_by(cartesian_distance.q)
            if not q_coord_spec_result.is_success():
                raise q_coord_spec_result.exception

            # if cartesian_distance.distance is None:
            #     raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")


        except (
            NullCoordinateException, TypeError,
            NullRowException, RowOutOfBoundsException,
            NullColumnException, ColumnOutOfBoundsException) as e:
            raise CoordinateValidationException(
                f"{method} CartesianDistanceSpecification: CoordinateDistance: validation failed"
            ) from e