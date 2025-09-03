from typing import cast, Generic, TYPE_CHECKING

from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.competitor import CompetitorValidationException
from assurance.exception.validation.team import TeamHistoryValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from assurance.validators.id import IdValidator
from assurance.validators.name import NameValidator
from assurance.validators.team_hist import SideRecordValidator

from chess.exception.null.owner import NullCompetitorException

if TYPE_CHECKING:
    from chess.competitor.model import Competitor


class CompetitorValidator(Validator):
    """
    Validates an Competitor used in a domain module meets requirements:
        - Is not null.
        - Its fields meet the specifications for the domain.
    Unmet requirements will raise a CompetitorValidationException

    For performance and single source of truth CompetitorValidator has:
        - No fields
        - only static method validate
    subclasses must implement validate.
    """

    @staticmethod
    def validate(t: Generic[T]) -> Result['Competitor']:
        entity = "Competitor"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates a competitor meets domain requirements:
            - Not null
            - valid id
            - valid name
            - Competitor.team_history meets validation requirements
        Any failed requirement raise an exception wrapped in a CompetitorValidationException
            
        Args
            t (Competitor): competitor to validate
            
         Returns:
             Result[T]: A Result object containing the validated payload if all domain requirements 
             are satisfied. CompetitorValidationException otherwise.
        
        Raises:
            TypeError: if t is not Competitor
            NullCompetitorException: if t is null   

            RowBelowBoundsException: If competitor.row < 0
            RowAboveBoundsException: If competitor.row >= ROW_SIZE
                
            ColumnBelowBoundsException: If competitor.column < 0
            ColumnAboveBoundsException: If competitor.column>= ROW_SIZE
                
            CompetitorValidationException: Wraps any preceding exception     
        """

        try:
            """
            Tests are chained in this specific order for a reason.
            """

            # If t is null no point continuing
            if t is None:
                raise NullCompetitorException(f"{method} {NullCompetitorException.DEFAULT_MESSAGE}")

            # If cannot cast from t to Competitor need to break
            from chess.competitor.model import Competitor
            if not isinstance(t, Competitor):
                raise TypeError(f"{method} Expected a Competitor, got {type(t).__name__}")

            # cast and run checks for the fields
            from chess.competitor.model import Competitor
            competitor = cast(Competitor, t)

            id_validation = IdValidator.validate(competitor.id)
            if not id_validation.is_success():
                raise id_validation.exception

            name_validation = NameValidator.validate(competitor.name)
            if not name_validation.is_success():
                raise name_validation.exception

            team_history_validation = SideRecordValidator.validate(competitor.sides_played)
            if not team_history_validation.is_success():
                raise team_history_validation.exception

            # Return the result if checks passed
            return Result(payload=competitor)

        except (
            TypeError,
            NullCompetitorException,
            IdValidationException,
            NameValidationException,
            TeamHistoryValidationException
        ) as e:
            raise CompetitorValidationException(
                f"{method}: {CompetitorValidationException.DEFAULT_MESSAGE}"
            ) from e