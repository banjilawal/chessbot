# src/assurance/depend/toolkit/struct/register.toolkit.py

"""
Module: assurance.depend.toolkit.struct.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import RegisterServiceDependency, StructLayerToolkit
from domain import Register, RegisterManifest, RegisterNullWarningSet, RegisterLayer

T = TypeVar("T", bound="Register")


class RegisterLayerToolkit(StructLayerToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: RegisterServiceDependency[T]
            manifest: RegisterManifest[T]

    Provides:

    Super Class:
        StructLayerToolkit
    """
    
    def __init__(
            self,
            dependency: RegisterServiceDependency[T],
            manifest: RegisterManifest[T],
    ):
        """
            wrapper: RegisterServiceDependency[T]
            manifest: RegisterManifest[T]
        """
        super().__init__(dependency=dependency, manifest=manifest)
    
    
    @property
    def dependency(self) -> RegisterServiceDependency[T]:
        return cast(RegisterServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> RegisterManifest[T]:
        return cast(RegisterManifest, super().manifest)
    
    @property
    def nulls(self) -> RegisterNullWarningSet[T]:
        return self.manifest.nulls
    
    @property
    def types(self) -> RegisterLayer[T]:
        return self.manifest.types