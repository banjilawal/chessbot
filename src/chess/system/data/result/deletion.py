# src/chess/system/data/result/deletion/result.py

"""
Module: chess.system.data.result.deletion.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system.data import DataResult
from chess.system import  NotImplementedException

T = TypeVar("T")

class DeletionResult(DataResult[Generic[T]]):
    
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None
    ):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> DataResult:
        method = "BuildResult.empty"
        
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )


