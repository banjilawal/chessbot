# src/assurance/depend/toolkit/struct/binder.toolkit.py

"""
Module: assurance.depend.toolkit.struct.binder.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import BinderDependency, StructValidatorToolkit
from domain import Binder, BinderManifest, BinderNullGroup, BinderLayer

T = TypeVar("T", bound="Binder")


class BinderValidatorToolkit(StructValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: BinderWrapperDependency[T]
            metadata: BinderManifest[T]

    Provides:

    Super Class:
        StructValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: BinderDependency[T],
            metadata: BinderManifest[T],
    ):
        """
            wrapper: BinderWrapperDependency[T]
            metadata: BinderManifest[T]
        """
        super().__init__(wrapper=wrapper, metadata=metadata)
    
    
    @property
    def wrapper(self) -> BinderDependency[T]:
        return cast(BinderDependency, super().wrapper)
    
    @property
    def metadata(self) -> BinderManifest[T]:
        return cast(BinderManifest, super().metadata)
    
    @property
    def nulls(self) -> BinderNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> BinderLayer[T]:
        return self.metadata.types