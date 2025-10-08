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

# src/chess/system/result.py

"""
Module: `chess.system.result.result`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides:
 Interface for operation results that can have either team data payload or an exception only.

Contains:
 * `Result`
"""


from typing import Optional, TypeVar, Generic

from chess.system import EmptyResultConstructorException, ErrorContradictsPayloadException

T = TypeVar('T')



class Result(Generic[T]):
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
  Abstract super class for data-holding objects which represent outcome of
  operations that produce one of two results only.
    * Success: A payload is returned
    * Failure: An exception is raised

  Attributes:
    `_payload` (`Optional`[`T`]): The payload of the result, if the operation called.
    `_exception` (`Optional`[`Exception`]): The error raised if the operation called failed.
  """

  _payload: Optional[T]
  _exception: Optional[Exception]

  def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
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
    method = "Result.__init_"

    # Raise an error if neither payload nor error is provided
    if payload is None and exception is None:
      raise EmptyResultConstructorException(
        f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}"
      )

    # Raise an error if both payload and error are provided
    if not (payload is None and exception is None):
      raise ErrorContradictsPayloadException(
        f"{method}: {ErrorContradictsPayloadException.DEFAULT_MESSAGE}"
      )

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



