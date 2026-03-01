# src/logic/system/build/result/result.py

"""
Module: logic.system.build.result.result
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional, TypeVar, Generic
from logic.system import Result, MethodImplementationException

T = TypeVar("T")

class BuildResult(Result[T], Generic[T]):
    """"""
    
    def __init__(self, payload: Optional[T] = None, exception: Optional[Exception] = None):
        super().__init__(payload=payload, exception=exception)
    
    @classmethod
    def success(cls, payload: T) -> BuildResult[T]:
        return cls(payload=payload)
    
    @classmethod
    def failure(cls, exception: Exception) -> BuildResult[T]:
        return cls(exception=exception)
        
    @classmethod
    def empty(cls) -> Result:
        method = "BuildResult.empty"
        return cls(exception=MethodImplementationException(
            msg=f"{method}: {MethodImplementationException.MSG}")
        )