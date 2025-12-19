from typing import Any, cast

from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.system.err.number.exception import InvalidNumberException, NullNumberException


class NumberValidator(Validator[int]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Verifies a candidate is not null and is an int.
    2.  Don't have to keep writing not null and isinstance int.

    # PROVIDES:
    ValidationResult[int] containing either:
        - On success: int in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    No attributes

    # CONSTRUCTOR:
    Default Constructor

    # CLASS METHODS:
        *   validate(candidate: Any) -> ValidationResult[int]:

    # INSTANCE METHODS:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[int]:
        """
        # ACTION:
        1.  Test if the candidate is:
                *   Not validation.
                *   A positive integer.
        2.  If either text fails send their exception in a ValidationResult.
        3.  When all checks pass cast the candidate to an INT then send inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any) object to certify is an int.

        # Returns:
        ValidationResult[int] containing either:
            - On success: int in the payload.
            - On failure: Exception.

        # Raises:
          *     TypeError
          *     NullNumberException
          *     InvalidNumberException
        """
        method = "IdValidator.validate"
        
        try:
            # Start the error detection process.
            if candidate is None:
                return ValidationResult.failure(
                    NullNumberException(f"{method}: {NullNumberException.DEFAULT_MESSAGE}")
                )
            # make sure its an int
            if not isinstance(candidate, int):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected an integer, got {type(candidate).__name__} instead.")
                )
            # If no errors are detected cast the candidate to an int object then return in
            # a ValidationResult.
            return ValidationResult.success(payload=cast(int, candidate))
        
        # Finally, if there is an unhandled exception Wrap an InvalidNumberException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNumberException(ex=ex, message=f"{method}: {InvalidNumberException.DEFAULT_MESSAGE}")
            )