from typing import Generic, cast

from assurance.exception.validation.name import NameValidationException
from assurance.result.base import Result
from assurance.validators.base import Validator, T
from chess.common.config import MIN_NAME_LENGTH
from chess.exception.name import NameLengthException, BlankNameException
from chess.exception.null.name import NullNameException


class NameValidator(Validator):

    @staticmethod
    def validate(t: Generic[T]) -> Result[str]:
        entity = "Name"
        class_name = f"{entity}Specification"
        method = f"{class_name}.is_satisfied_by"

        """
        Validates an Name meets specifications:
            - Not null
            - Not blank (only white space)
            - Not shorter than MIN_NAME_LENGTH
            
        Any validators error will have be encapsulated in a NameValidationException

        Args
            t (Coordinate): generic to be validated

         Returns:
             Result[T]: A Result object containing the validated payload if the specification is 
                satisfied, NameValidationException otherwise.

        Raises:
            NullNameException: if t is null
            TypeError: if t is not int
            BlankNameException: if t only contains white space.
            NameLengthException: if t is shorter than MIN_NAME_LENGTH
              
            
            NameValidationException: Wraps any
                (NullNameException, TypeError, NameLengthException)  
        """
        try:
            if t is None:
                raise NullNameException(f"{method} {NullNameException.DEFAULT_MESSAGE}")

            if not isinstance(t, str):
                raise TypeError(f"{method} Expected an integer, got {type(t).__name__}")

            name = cast(str, t)

            if len(name) < MIN_NAME_LENGTH:
                raise NameLengthException("{method} NameLengthException.default_message")

            if name.strip():
                raise BlankNameException(f"{method}: {BlankNameException.DEFAULT_MESSAGE}")

            return Result(payload=name)

        except(
            TypeError,
            NullNameException,
            BlankNameException,
            NameLengthException
        ) as e:
            raise NameValidationException(
                f"{method} {NameValidationException.DEFAULT_MESSAGE}"
            ) from e

# def main():
#     result = NameSpecification.is_satisfied_by(5)
#     if result.is_success():
#         print(f"Valid Name: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#
#     result = NameSpecification.is_satisfied_by(-3)
#     if result.is_success():
#         print(f"Valid Name: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#     result = NameSpecification.is_satisfied_by(None)
#     if result.is_success():
#         print(f"Valid Name: {result.payload}")
#     else:
#         print(f"Validation failed: {result.exception}")
#
# if __name__ == "__main__":
#     main()