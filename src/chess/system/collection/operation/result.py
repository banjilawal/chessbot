# src/chess/system/collection/result/result.py

"""
Module: chess.system.collection.result.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, Optional, TypeVar

from chess.system import Result, ResultState

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
    _state: ResultState
    
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None,
            state: Optional[ResultState] = None,
    ):
        super().__init__(payload=payload, exception=exception)
        self._state = state
        
    @property
    def state(self) -> Optional[ResultState]:
        return self._state
