from typing import Generic, cast

from chess.exception import (
    LongNameException, ShortNameException, BlankNameException, NullNameException, NameValidationException
)
from chess.common import Validator, MIN_NAME_LENGTH, MAX_NAME_LENGTH, Result

from chess.common.config import MIN_NAME_LENGTH, MAX_NAME_LENGTH



class NameValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[str]:
        entity = "Name"
        class_name = f"{entity}Validator"
        method = f"{class_name}.validate"

        """
        Validates an Name meets specifications:
            - Not null
            - Not blank (only white space)
            - Not shorter than MIN_NAME_LENGTH     
        Any unmet specifications raise exceptions wrapped in a NameValidationException

        Args
            t (str): generic to be validated

         Returns:
             Result[T]: A Result object containing the validated payload if the Validator is 
                satisfied, NameValidationException otherwise.

        Raises:
            TypeError: if t is not int
            NullNameException: if t is null
            BlankNameException: if t only contains white space.
            ShortNameException: if t is shorter than MIN_NAME_LENGTH
            
            NameValidationException: Wraps any preceding team_exception 
        """
        try:
            if t is None:
                raise NullNameException(f"{method} {NullNameException.DEFAULT_MESSAGE}")

            if not isinstance(t, str):
                raise TypeError(f"{method} Expected an str, got {type(t).__name__}")

            name = cast(str, t)

            if not name.strip():
                raise BlankNameException(f"{method}: {BlankNameException.DEFAULT_MESSAGE}")

            if len(name) < MIN_NAME_LENGTH:
                raise ShortNameException(f"{method}: {ShortNameException.DEFAULT_MESSAGE}")

            if len(name) > MAX_NAME_LENGTH:
                raise LongNameException(f"{method}: {LongNameException.DEFAULT_MESSAGE}")

            return Result(payload=name)

        except(
            TypeError,
            NullNameException,
            BlankNameException,
            ShortNameException,
            LongNameException
        ) as e:
            raise NameValidationException(
                f"{method} {NameValidationException.DEFAULT_MESSAGE}"
            ) from e

# def main():
#     result = NameValidator.validate(5)
#     if result.is_success():
#         print(f"Valid Name: {result.payload}")
#     else:
#         print(f"Validation failed: {result.team_exception}")
#
#     result = NameValidator.validate(-3)
#     if result.is_success():
#         print(f"Valid Name: {result.payload}")
#     else:
#         print(f"Validation failed: {result.team_exception}")
#     result = NameValidator.validate(None)
#     if result.is_success():
#         print(f"Valid Name: {result.payload}")
#     else:
#         print(f"Validation failed: {result.team_exception}")
#
# if __name__ == "__main__":
#     main()