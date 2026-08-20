# src/toolkit/builder/model/toolkit.py

"""
Module: toolkit.builder.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.assembler import ModelAssembler
from assurance.checker import ModelIntegrityChecker
from toolkit.builder.model.toolkit import BuilderToolkit

T = TypeVar("T", bound="Model")

class ModelBuilderToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Bundles ModelBuilder dependencies.

    Attributes:
        assembler: [ModelAssembler[T]],
        root_certifier: [ModelRootCertifier[T]]
        
    Provides:
    
    Super Class:
        BuilderToolkit
    """
    
    def __init__(
            self,
            assembler: [ModelAssembler[T]],
            root_certifier: [ModelIntegrityChecker[T]],
    ):
        """
        Args:
            assembler: [ModelAssembler[T]],
            root_certifier: [ModelRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> [ModelAssembler[T]]:
        return cast([ModelAssembler[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [ModelIntegrityChecker[T]]:
        return cast([ModelIntegrityChecker[T]], super().integrity_checker)