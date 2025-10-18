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
 * `TravelEventFactory`
"""

from chess.system import EmptyResultConstructorException, ErrorContradictsPayloadException
from typing import Optional, TypeVar, Generic


T = TypeVar('T')

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
BuildResult is team generic class that encapsulates the outcome of Builder operation. BuildResult has the
same structure as Result but is used specifically in the roster of building entities. It can hold either.
team payload of type T or an Exception, but not both. If the build operation is successful, the payload will
contain the built object. If the build operation fails, the error will contain the error that
occurred during the build process.

BuildResult is helpful for debugging and showing Builders have different outcomes than operations which generate team transaction.

Attributes:
  _payload (Optional[T]): The payload of the transaction, if successful.
  _exception (Optional[Exception]): The error of the transaction, if failed.

Methods:
  is_success() -> bool: Returns True if the transaction is successful (i.e., has team payload only).
"""

class BuildResult(Generic[T]):


  _payload: Optional[T]
  _exception: Optional[Exception]

  def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):

    method = "Result.__init_"

    if payload is None and exception is None:
      raise EmptyResultConstructorException(f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}")

    if not (payload is None or exception is None):
      raise ErrorContradictsPayloadException(f"{method}: {ErrorContradictsPayloadException.DEFAULT_MESSAGE}")

    self._payload = payload
    self._exception = exception


  @property
  def payload(self) -> Optional[T]:
    return self._payload


  @property
  def exception(self) -> Optional[Exception]:
    return self._exception


  def is_success(self) -> bool:
    return self._exception is None and self._payload is not None


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
    Initializes team BuildResult object.
    Args:
      payload (Optional[T]): The payload of the transaction, if successful.
      exception (Optional[Exception]): The error of the transaction, if failed.
    Raises:
      EmptyResultConstructorException: If neither payload nor error is provided.
      ResultPayloadConflictException: If both payload and error are provided.
    """


