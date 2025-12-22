# src/chess/system/result/result.py

"""
Module: chess.system.result.result
Author: Banji Lawal
Created: 2025-09-28
version: 1.0.0
"""

from typing import Optional, TypeVar, Generic

from chess.system import Result

T = TypeVar("T")


class Result(Generic[T]):
    """
    # ROLE: Messanger  Data Transport Object, Error Transport Object.
  
    # RESPONSIBILITIES:
    1.  Send the outcome of a request to the client.
    2.  If the request was satisfied send the success-data in the payload.
    3.  If request was not fulfilled return an exception.
    
    # PARENT:
    None
  
    # PROVIDES:
        *   is_success: --> bool
        *   is_failure: --> bool
        *   is_empty: --> bool
        *   success(payload: T): --> Result[T]
        *   failure(exception: Exception): --> Result[Exception]
        *   empty(): --> Result[None]
        
    # LOCAL ATTRIBUTES:
        *   payload (T)
        *   exception (Exception)
        
    INHERITED ATTRIBUTES:
    None
    """
    _payload: Optional[T]
    _exception: Optional[Exception]
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        self._payload = payload
        self._exception = exception
    
    @property
    def payload(self) -> Optional[T]:
        return self._payload
    
    @property
    def exception(self) -> Optional[Exception]:
        return self._exception
    
    @property
    def is_success(self) -> bool:
        return self._exception is None and self._payload is not None
    
    @property
    def is_failure(self) -> bool:
        return self._exception is not None
    
    @property
    def is_empty(self) -> bool:
        return self._payload is None and self._exception is None
    
    @classmethod
    def success(cls, payload: T) -> Result[T]:
        """
        Factory method for creating a successful Result.
        # PARAM:
            *   payload (T): The data to be sent to the client.
        # RETURN:
            *   Result[T]
        # RAISES:
        None
        """
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> Result[T]:
        """
        Factory method for creating a failure.
        # PARAM:
            *   exception (Exception): cause of the failure.
        # RETURN:
            *   Result[Exception]
        # RAISES:
        None
        """
        return cls(exception=exception)
    
    @classmethod
    def empty(cls) -> Result[None]:
        """
        Factory method for returning a null outcome.
        # PARAM:
        None
        # RETURN:
        Result[None]
        # RAISES:
        None
        """
        return cls()
