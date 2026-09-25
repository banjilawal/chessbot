# src/assurance/toolkit/structure/register.toolkit.py

"""
Module: assurance.toolkit.structure.register.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import RegisterHelperTable, StructureValidatorToolkit
from domain import Register, RegisterManifest

T = TypeVar("T", bound="Register")


class RegisterValidatorToolkit(StructureValidatorToolkit[T], ABC, Generic[T]):
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
        StructureValidatorToolkit
    """
    
    def __init__(
            self,
            helper: RegisterHelperTable[T],
            metadata: RegisterManifest[T],
    ):
        """
            helper: RegisterHelperTable[T]
            metadata: RegisterManifest[T]
        """
        super().__init__(helper=helper, metadata=metadata)
    
    
    @property
    def attribute(self) -> RegisterHelperTable[T]:
        return cast(RegisterHelperTable, super().attribute)
    
    @property
    def metadata(self) -> RegisterManifest[T]:
        return cast(RegisterManifest, super().metadata)