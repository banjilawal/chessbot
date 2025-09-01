from typing import cast, Generic

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.owner import OwnerValidationException
from assurance.exception.validation.team import TeamHistoryValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from assurance.validators.team_hist import TeamHistoryValidator

from chess.exception.null.owner import NullOwnerException
from chess.owner.model import Owner


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
            - valid id
            - valid name
            - Owner.team_history meets validation requirements
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
                raise NullOwnerException(f"{method} {NullOwnerException.DEFAULT_MESSAGE}")

            # If cannot cast from t to Owner need to break
            if not isinstance(t, Owner):
                raise TypeError(f"{method} Expected a Owner, got {type(t).__name__}")

            # cast and run checks for the fields
            owner = cast(Owner, t)

            id_validation = IdValidator.validate(owner.id)
            if not id_validation.is_success():
                raise id_validation.exception

            name_validation = NameValidator.validate(owner.name)
            if not name_validation.is_success():
                raise name_validation.exception

            team_history_validation = TeamHistoryValidator.validate(owner.team_history)
            if not team_history_validation.is_success():
                raise team_history_validation.exception

            # Return the result if checks passed
            return Result(payload=owner)

        except (
            TypeError,
            NullOwnerException,
            IdValidationException,
            NameValidationException,
            TeamHistoryValidationException
        ) as e:
            raise OwnerValidationException(
                f"{method}: {OwnerValidationException.DEFAULT_MESSAGE}"
            ) from e