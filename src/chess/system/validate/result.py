
from typing import Optional, TypeVar, Generic
from chess.system import Result

T = TypeVar("T")

class ValidationResult(Result[Generic[T]]):
  """
  A Result object encapsulates the outcome of methods and operations that return an object. Different from
  TransactionResult which assures an existing object's state changed correctly without causing inconsistencies.

  USAGE:
    Result is used with
    - Validation of existing objects.
    - Objects returned by accessors and query methods.
    - Operations that return an object, but may fail due to business logic or other reasons.
    - Methods that may fail due to external factors (e.g., network issues, file I

  Attributes:
    _payload (Optional[T]): The payload of the result, if successful.
    _exception (Optional[Exception]): The error of the result, if failed.

  Methods:
    is_success() -> bool: Returns True if the result is successful (i.e., has team payload only).
  """

  _payload: Optional[T]
  _exception: Optional[Exception]

  def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
    super().__init__(payload=payload, exception=exception)
