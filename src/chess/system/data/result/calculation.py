# src/chess/system/data/result/calculation.py

"""
Module: chess.system.data.result.calculation
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Generic, Optional, TypeVar

from chess.system.data import DataResult
from chess.system import EmptyDataResultException, NotImplementedException, Result

T = TypeVar("T")

class CalculationResult(DataResult[Generic[T]]):
    """
    # ROLE: Messanger, Data Transport Object, Error Transport Object.

    # RESPONSIBILITIES:
    1.  Send the outcome of a calculation transaction to the caller.
    2.  Enforcing mutual exclusion. A CalculationResult can either carry payload or exception. Not both.

    # PARENT
        *   DataResult

    # PROVIDES:
    CalculationResult

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DataResult class for inherited attributes.
    """
    
    def __init__( self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def empty(cls) -> Result:
        method = "CalculationResult.empty"
        return cls(
            exception=NotImplementedException(
                message=f"{method}: {NotImplementedException.DEFAULT_MESSAGE}",
                ex=EmptyDataResultException(f"{method}: {EmptyDataResultException.DEFAULT_MESSAGE}")
            )
        )


