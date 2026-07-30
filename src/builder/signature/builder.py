# src/builder/pattern/builder.py

"""
Module: builder.pattern.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from blueprint import SignatureBlueprint
from builder import Builder
from result import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Signature")

class SignatureBuilder(Builder, ABC, Generic[T]):
    
    def __init__(self, builder_toolkit: SignatureBuilderToolkit[T]):
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> SignatureBuilderToolkit[T]:
        return cast(T, super().builder_toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: SignatureBlueprint[T]) -> BuildResult[T]:
        pass