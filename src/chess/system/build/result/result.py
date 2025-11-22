# src/chess/system/builder/result/result.py

"""
Module: chess.system.builder.result.result
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from typing import Optional, TypeVar, Generic
from chess.system import EmptyBuildResultException, Result, NotImplementedException

T = TypeVar('V')


class BuildResult(Result[Generic[T]]):
    """"""
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
        
    @classmethod
    def empty(cls) -> Result:
        method = "BuildResult.empty"
        
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyBuildResultException(message=f"{method}: {EmptyBuildResultException.DEFAULT_MESSAGE}")
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
        # def payload(self) -> Optional[V]:
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
    Initializes team_name BuildResult object.
    Args:
      payload (Optional[V]): The payload of the notification, if successful.
      rollback_exception (Optional[Exception]): The error of the notification, if failed.
    Raises:
      EmptyResultConstructorException: If neither payload nor error is provided.
      ResultPayloadConflictException: If both payload and error are provided.
    """
