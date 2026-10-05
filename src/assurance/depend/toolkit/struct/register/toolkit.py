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

from assurance import RegisterDependency, StructValidatorToolkit
from domain import Register, RegisterManifest

T = TypeVar("T", bound="Register")


class RegisterValidatorToolkit(StructValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            helper: RegisterHelperTable[T]
            metadata: RegisterManifest[T]

    Provides:

    Super Class:
        StructValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: RegisterDependency[T],
            metadata: RegisterManifest[T],
    ):
        """
            helper: RegisterHelperTable[T]
            metadata: RegisterManifest[T]
        """
        super().__init__(wrapper=wrapper, metadata=metadata)
    
    
    @property
    def wrapper(self) -> RegisterDependency[T]:
        return cast(RegisterDependency, super().wrapper)
    
    @property
    def metadata(self) -> RegisterManifest[T]:
        return cast(RegisterManifest, super().metadata)