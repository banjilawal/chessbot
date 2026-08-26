# src/fabrication/toolkit/toolkit.py

"""
Module: fabrication.toolkit.toolkit
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC
from typing import Generic, Optional, TypeVar

from fabrication import BuildFinalizer
from transit import ValidationDispatcher

T = TypeVar("T")


class BuilderToolkit(ABC, Generic[T]):
    """
    Role
        -   Toolkit

    Responsibilities:
        1.  Provides validators and other resources Builder requires to complete its task.

    Attributes:
        validation_dispatcher: ValidationDispatcher[T]
        finalizer: Optional[BuildFinalizer[T]]

    Provides:

    Super Class:
    """
    _validation_dispatcher: ValidationDispatcher[T]
    _finalizer: Optional[BuildFinalizer[T]]
    
    
    def __init__(
            self,
            validation_dispatcher: ValidationDispatcher[T],
            finalizer: Optional[BuildFinalizer[T]] | None = None,
    ):
        """
        Args:
            validation_dispatcher: ValidationDispatcher[T]
            finalizer: Optional[BuildFinalizer[T]]
        """
        self._validation_dispatcher = validation_dispatcher
        self._finalizer = finalizer
        
        
    @property
    def validation_dispatcher(self) -> ValidationDispatcher[T]:
        return self._validation_dispatcher
    
    
    @property
    def finalizer(self) -> Optional[BuildFinalizer[T]]:
        return self._finalizer
        
     