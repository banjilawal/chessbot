# src/builder/pattern/offset/builder.py

"""
Module: builder.pattern.offset.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, TypeVar

from builder import SignatureBuilder
from util import LoggingLevelRouter

T = TypeVar("T", bound="OffsetSignature")

class OffsetBuilder(SignatureBuilder, Generic[T]):
    
    def __init__(self, builder_toolkit: OffsetBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: OffsetSignatureBlueprint[T]) -> BuildResult[OffsetSignature[T]]:
        pass

    
    
    