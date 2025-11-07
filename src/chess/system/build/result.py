# chess/system/build/result.py

"""
Module: chess.system.build.result
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

# src/chess/owner/travel/notification
"""
Module: chess.owner.travel.notification
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

from chess.system import NotImplementedException, Result
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

BuildResult is helpful for debugging and showing Builders have different outcomes than operations which generate team notification.

Attributes:
  _payload (Optional[T]): The payload of the notification, if successful.
  _exception (Optional[Exception]): The error of the notification, if failed.

Methods:
  is_success() -> bool: Returns True if the notification is successful (i.e., has team payload only).
"""


class BuildResult(Result[Generic[T]]):
    _payload: Optional[T]
    _exception: Optional[Exception]
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
        
    @classmethod
    def empty(cls) -> Result:
        method = "BuildResult.empty"
        
        return cls(
            exception=NotImplementedException(
                f"{method}: {NotImplementedException.DEFAULT_MESSAGE}. BuildResult cannot"
                f" be empty. It must have either a payload or an rollback_exception."
            )
        )
        
        #
        #   method = "Result.__init_"
        #
        #   if payload is None and rollback_exception is None:
        #     raise EmptyResultConstructorException(f"{method}: {EmptyResultConstructorException.DEFAULT_MESSAGE}")
        #
        #   if not (payload is None or rollback_exception is None):
        #     raise ErrorContradictsPayloadException(f"{method}: {ErrorContradictsPayloadException.DEFAULT_MESSAGE}")
        #
        #   self._payload = payload
        #   self._exception = rollback_exception
        #
        #
        # @property
        # def payload(self) -> Optional[T]:
        #   return self._payload
        #
        #
        # @property
        # def rollback_exception(self) -> Optional[Exception]:
        #   return self._exception
        #
        #
        # def is_success(self) -> bool:
        #   return self._exception is None and self._payload is not None
        #
        
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
      payload (Optional[T]): The payload of the notification, if successful.
      rollback_exception (Optional[Exception]): The error of the notification, if failed.
    Raises:
      EmptyResultConstructorException: If neither payload nor error is provided.
      ResultPayloadConflictException: If both payload and error are provided.
    """
