# src/chess/system/data/result/deletion.py

"""
Module: chess.system.data.result.deletion
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system.data import DataResult
from chess.system import EmptyDataResultException, NotImplementedException

T = TypeVar("T")

class DeletionResult(DataResult[Generic[T]]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a deletion transaction to the caller.
    2.  Enforcing mutual exclusion. A DeletionResult can either carry payload or exception. Not both.

    # PARENT
        *   DataResult

    # PROVIDES:
    DeletionResult

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> DataResult:
        method = "DeletionResult.empty"
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )


