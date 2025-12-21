# src/chess/system/data/result/insertion.py

"""
Module: chess.system.data.result.insertion
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system.data import EmptyDataResultException
from chess.system import NotImplementedException
from chess.system.data.result.base import DataResult

T = TypeVar("T")

class InsertionResult(DataResult[Generic[T]]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a insertion transaction to the caller.
    2.  Enforcing mutual exclusion. A InsertionResult can either carry payload or exception. Not both.

    # PARENT:
        *   DataResult

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> DataResult:
        method = "InsertionResult.empty"
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )


