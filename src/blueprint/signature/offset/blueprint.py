# src/builder/pattern/offset/builder.py

"""
Module: builder.pattern.offset.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Type, TypeVar

from blueprint import SignatureBlueprint
from err import OffsetPatternNullException

T = TypeVar("T", bound="OffsetSignature")

class OffsetSignatureBlueprint(SignatureBlueprint, ABC, Generic[T]):
    
    def __init__(
            self,
            model_class: Type[T],
            null_exception: OffsetPatternNullException,
    ):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: OffsetSignatureBlueprint[T]) -> BuildResult[OffsetSignature[T]]:
        pass

    
    
    