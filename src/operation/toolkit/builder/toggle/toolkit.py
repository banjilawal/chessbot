# src/operation/toolkit/builder/toggle/toolkit.py

"""
Module: operation.toolkit.builder.toggle.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.builder import ToggleBuilder
from assurance.validator import ToggleCertifier
from operation.toolkit.builder.toggle.toolkit import BuilderToolkit

T = TypeVar("T", bound="Toggle")

class ToggleBuilderToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -  Dependency Management
        
    Responsibilities:
        1.  Bundles ToggleBuilder dependencies.

    Attributes:
        assembler: [ToggleAssembler[T]],
        root_certifier: [ToggleRootCertifier[T]]
        
    Provides:
    
    Super Class:
        BuilderToolkit
    """
    
    def __init__(
            self,
            assembler: [ToggleBuilder[T]],
            root_certifier: [ToggleCertifier[T]],
    ):
        """
        Args:
            assembler: [ToggleAssembler[T]],
            root_certifier: [ToggleRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> [ToggleBuilder[T]]:
        return cast([ToggleBuilder[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [ToggleCertifier[T]]:
        return cast([ToggleCertifier[T]], super().integrity_checker)