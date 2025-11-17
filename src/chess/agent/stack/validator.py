# src/chess/agent/stack/validator.py

"""
Module: chess.agent.stack.validator
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
  'CoordStackValidator'
]

class CoordStackValidator(Validator):

  @staticmethod
  def validate(candidate: CoordValidator) -> Result[CoordStack]:

    method = "CoordinateStackValidator.validate"

    try:
      if candidate is None:
        raise NullCoordStackException(
          f"{method} {NullCoordStackException.DEFAULT_MESSAGE}"
        )

      if not isinstance(candidate, CoordStack):
        raise TypeError(f"{method} Expected team_name CoordStack, got {type(candidate).__name__} instead.")

      coords = cast(CoordStack, candidate)

      if coords.size() > 0 and coords.is_empty():
        raise StackSizeConflictException(f"{method}: {StackSizeConflictException.DEFAULT_MESSAGE}")

      if coords.is_empty() and coords.current_coord is not None:
        raise InconsistentCurrentCoordException(
          f"{method}: {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
        )

      if coords.current_coord is None and not coords.is_empty():
        raise InconsistentCurrentCoordException(
          f"{method} {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
        )

      if coords.items is None:
        raise CorruptedStackException(f"{method} {CorruptedStackException.DEFAULT_MESSAGE}")

      current_coord = coords.current_coord

      if (current_coord is not None and
          not CoordValidator.validate(current_coord).is_success()):
        raise InconsistentCurrentCoordException(
          f"{method} {InconsistentCurrentCoordException.DEFAULT_MESSAGE}"
        )

      return Result(payload=coords)

    except (
        TypeError,
        NullCoordStackException,
        StackSizeConflictException,
        InconsistentCurrentCoordException
    ) as e:
      raise CoordStackValidationException(
        f"{method}: {CoordStackValidationException.DEFAULT_MESSAGE}"
      ) from e
#
#
# def main():
#   coordinate_stack = CoordStack()
#   validator_result = CoordinateStackValidatorvalidate(coordinate_stack)
#   if validator_result.is_success():
#     print("CoordStack validator satisfied.")
#   else:
#     print("CoordStack validator not satisfied.")
#
#
# if __name__ == "__main__":
#   main()