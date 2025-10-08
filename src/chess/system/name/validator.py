from typing import Generic, cast


from chess.system import (
  MIN_NAME_LENGTH, MAX_NAME_LENGTH, Validator, Result, LongNameException,
  ShortNameException, BlankNameException, NullNameException
)



class NameValidator(Validator):

  @staticmethod
  def validate(candidate: Generic[T]) -> Result[str]:
    entity = "Name"
    class_name = f"{entity}Validator"
    method = f"{class_name}.validate"

    """
    Validates an Name meets specifications:
      - Not null
      - Not blank (only white space)
      - Not shorter than MIN_NAME_LENGTH   
    Any unmet specifications raise exceptions wrapped in team InvalidNameException

    Args
      candidate (str): generic to be validated

     Returns:
       Result[T]: A Result object containing the validated payload if the Validator is 
        satisfied, InvalidNameException otherwise.

    Raises:
      TypeError: if candidate is not int
      NullNameException: if candidate is null
      BlankNameException: if candidate only contains white space.
      ShortNameException: if candidate is shorter than MIN_NAME_LENGTH
      
      InvalidNameException: Wraps any preceding team_exception 
    """
    try:
      if candidate is None:
        raise NullNameException(f"{method} {NullNameException.DEFAULT_MESSAGE}")

      if not isinstance(candidate, str):
        raise TypeError(f"{method} Expected an str, got {type(candidate).__name__}")

      name = cast(str, candidate)

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
#   result = NameValidator.validate(5)
#   if result.is_success():
#     print(f"Valid Name: {result.payload}")
#   else:
#     print(f"Validation failed: {result.team_exception}")
#
#   result = NameValidator.validate(-3)
#   if result.is_success():
#     print(f"Valid Name: {result.payload}")
#   else:
#     print(f"Validation failed: {result.team_exception}")
#   result = NameValidator.validate(None)
#   if result.is_success():
#     print(f"Valid Name: {result.payload}")
#   else:
#     print(f"Validation failed: {result.team_exception}")
#
# if __name__ == "__main__":
#   main()