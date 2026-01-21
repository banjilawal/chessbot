# src/chess/system/data/result/base.py

"""
Module: chess.system.data.result.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import abstractmethod
from typing import Generic, Optional, TypeVar

from chess.system import Result, DataResult, DataResultState

T = TypeVar("T")

class DataResult(Result[T], Generic[T]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    Data transactions are solely insertions, deletions, updates, and calculations. Data transactions either
    put something into a collection, remove something from it, or generate a new value from the existing data.
    All these operations either succeed or fail. So they will contain either a payload or an exception (but not both).
    
    1.  Send the outcome of a data transaction to the invoker.
    2.  Enforcing mutual exclusion. A DataResult can either carry payload or exception. Not both.

    # PARENT:
        *   Result

    # PROVIDES:
    DataResult

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See Result class for inherited attributes.
    """
    _state: DataResultState
    
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
            state: Optional[DataResultState] = None,
    ):
        super().__init__(payload=payload, exception=exception)
        self._state = state
        
    @property
    def state(self) -> Optional[DataResultState]:
        return self._state
    
    @classmethod
    @abstractmethod
    def empty(cls) -> DataResult[T]:
        pass
        # method = "DataResult.empty"
        # return cls(
        #     exception=NotImplementedException(
        #         message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
        #         ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
        #     )
        # )
