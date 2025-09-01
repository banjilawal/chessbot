from typing import cast, Generic


from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.owner.base import Owner


class OwnerValidator(Validator):
    """
    Validates an Owner used in a domain module meets requirements:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements will raise a OwnerValidationException

    For performance and single source of truth OwnerValidator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result[Owner]:
        entity = "Owner"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a owner meets domain requirements:
            - Not null
            - row is not null
            - column is not null
            - row is within the bounds of the chess chessboard
            - column is within the bounds of the chess chessboard
        Any failed requirement raise an exception wrapped in a OwnerValidationException
            
        Args
            t (Owner): owner to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. OwnerValidationException otherwise.
        
        Raises:
            TypeError: if t is not Owner
            NullOwnerException: if t is null   

            RowBelowBoundsException: If owner.row < 0
            RowAboveBoundsException: If owner.row >= ROW_SIZE
                
            ColumnBelowBoundsException: If owner.column < 0
            ColumnAboveBoundsException: If owner.column>= ROW_SIZE
                
            OwnerValidationException: Wraps any preceding exception     
        """

        try:
            """
            Tests are chained in this specific order for a reason.
            """

            # If t is null no point continuing
            if t is None:
                raise NullOwnerException(
                    f"{method} NullOwnerException.DEFAULT_MESSAGE"
                )

            # If cannot cast from t to Owner need to break
            if not isinstance(t, Owner):
                raise TypeError(f"{method} Expected a Owner, got {type(t).__name__}")

            # cast and run checks for the fields
            owner = cast(Owner, t)

            if owner.row is None:
                raise NullRowException(f"{method} {NullRowException.DEFAULT_MESSAGE}")

            if owner.row < 0:
                raise RowBelowBoundsException(f"{method} {RowBelowBoundsException.DEFAULT_MESSAGE}")

            if owner.row >= ROW_SIZE:
                raise RowAboveBoundsException(f"{method} {RowAboveBoundsException.DEFAULT_MESSAGE}")

            if owner.column is None:
                raise NullColumnException(f"{method} {NullColumnException.DEFAULT_MESSAGE}")

            if owner.column < 0:
                raise ColumnBelowBoundsException(f"{method} {ColumnBelowBoundsException.DEFAULT_MESSAGE}")

            if owner.column >= COLUMN_SIZE:
                raise ColumnAboveBoundsException(f"{method} {ColumnAboveBoundsException.DEFAULT_MESSAGE}")

            # Return the result if checks passed
            return Result(payload=owner)

        except (
            TypeError,
            NullOwnerException,

            NullRowException,
            RowBelowBoundsException,
            RowAboveBoundsException,

            NullColumnException,
            ColumnBelowBoundsException,
            ColumnAboveBoundsException
        ) as e:
            raise OwnerValidationException(
                f"{method}: {OwnerValidationException.DEFAULT_MESSAGE}"
            ) from e