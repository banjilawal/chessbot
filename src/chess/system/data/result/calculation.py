# src/chess/system/data/result/calculation/result.py

"""
Module: chess.system.data.result.calculation.result
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system.data import DataResult
from chess.system import  NotImplementedException, Result

T = TypeVar("T")

class CalculationResult(DataResult[Generic[T]]):
    
    def __init__(
            self,
            payload: Optional[T] = None,
            exception: Optional[Exception] = None
    ):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "BuildResult.empty"
        
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )


