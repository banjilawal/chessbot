# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * `OccupationTransaction`
"""

from typing import cast, TypeVar

from chess.system import ValidationResult, Validator, KNIGHT_STEP_SIZE, LoggingLevelRouter
from chess.vector import (
  Vector, NullVectorException, NullXComponentException, NullYComponentException,
  VectorBelowBoundsException, VectorAboveBoundsException,InvalidVectorException
)

T = TypeVar('T')

class VectorValidator(Validator[Vector]):
  """
  ROLE:
  ----
  RESPONSIBILITIES:
  ----------------
  PROVIDES:
  --------
  ATTRIBUTES:
  ----------
  [
    <No attributes. Implementors declare their own.>
  OR
    * `_attribute` (`data_type`): <sentence_if_necessary>
  ]
  """
  """
  Validates existing `Vector` instances that are passed around the system.

  While `VectorBuilder` ensures valid Vectors are created, `VectorValidator`
  checks `Vector` instances that already exist - whether they came from
  deserialization, external sources, or need re-validate after modifications.

  Usage:
    ```python
    # Validate an existing vector
    vector_validation = VectorValidator.validate(candidate)
    if not vector_validation.is_success():
      raise vector_validation.err
    vector = cast(Vector, vector_validation.payload)
    ```
  Use VectorBuilder for construction, VectorValidator for verification.
  """

  @classmethod
  def validate(cls, candidate: Vector) -> ValidationResult[Vector]:

    method = "VectorValidator.validate"

    try:
      if candidate is None:
        err = NullVectorException(f"{method} NullVectorException.DEFAULT_MESSAGE")
        result = ValidationResult(exception=err)
        LoggingLevelRouter.route_error(VectorValidator, err)
        return ValidationResult(exception=err)

      if not isinstance(candidate, Vector):
        raise TypeError(f"{method} Expected an Vector, got {type(candidate).__name__}")

      vector = cast(Vector, candidate)

      if vector.x is None:
        return ValidationResult(
          exception=NullXComponentException(
            f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
        )
        # LoggingLevelRouter.propagate_error(context=VectorValidator, exception_factory=err)
        # raise

      if vector.x < -KNIGHT_STEP_SIZE:
        # print(f"x: {x} knight_step_size:{-KNIGHT_STEP_SIZE}")
        raise VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")

      if vector.x > KNIGHT_STEP_SIZE:
        raise VectorAboveBoundsException( f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}" )

      if vector.y is None:
        raise NullYComponentException(f"{method} {NullYComponentException.DEFAULT_MESSAGE}")

      if vector.y < -KNIGHT_STEP_SIZE:
        raise VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                         )
      if vector.y > KNIGHT_STEP_SIZE:
        raise VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}" )

      return Result(payload=vector)

    except (
        TypeError,
        NullVectorException,
        NullYComponentException,
        NullXComponentException,
        VectorBelowBoundsException,
        VectorAboveBoundsException
    ) as e:
      raise InvalidVectorException(f"{method}: f{InvalidVectorException.DEFAULT_MESSAGE}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidVectorException(f"An unexpected error occurred during validate: {e}") from e

    """
    Action:
    Parameters:
        * `param` (`DataType`):
    Returns:
        `DataType` or `Void`
    Raises:
    MethodNameException wraps
        *
    """
    """
     Validates that an existing `Vector` instance meets all specifications.

     Performs comprehensive validate on team `Vector` instance that already exists,
     checking type safety, null values, and component bounds. Unlike VectorBuilder
     which creates new valid Vectors, this validator verifies existing `Vector`
     instances from external sources, deserialization, or after modifications.

     Args:
       candidate (Generic[T]): The object to validate, expected to be team Vector instance.
              Must not be None and must be within component bounds
              [-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE].

     Returns:
       Result[Vector]: A Result containing either:
         - On success: The validated Vector instance in the payload
         - On failure: Error information and error details

     Raises:
       InvalidVectorException: Wraps any specification violations including:
         - NullVectorException: if input is None
         - TypeError: if input is not team Vector instance
         - NullXComponentException: if Vector.x is None
         - NullYComponentException: if Vector.y is None
         - VectorBelowBoundsException: if x or y < -KNIGHT_STEP_SIZE
         - VectorAboveBoundsException: if x or y > KNIGHT_STEP_SIZE

     Note:
       Use VectorBuilder for creating new Vectors with validate,
       use VectorValidator for verifying existing Vector instances.

     Example:
       ```python
       # Validate an existing vector
       result = VectorValidator.validate(some_vector)
       if result.is_success():
         validated_vector = result.payload
       else:
         # Handle validate failure
         pass
       ```
     """

#
#
# def main():
#   vector = Vector(x=2, y=1)
#   specification_result = VectorValidator.validate(vector)
#   if specification_result.is_success():
#     print("Vector specification satisfied.")
#   else:
#     print("Vector specification not satisfied.")
#
# if __name__ == "__main__":
#   main()
