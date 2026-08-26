# src/operation/toolkit/builder/model/toolkit.py

"""
Module: operation.toolkit.builder.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from fabrication.builder import ModelBuilder
from assurance.checker import ModelIntegrityChecker
from operation.toolkit.builder.model.toolkit import BuilderToolkit

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
            assembler: [ModelBuilder[T]],
            root_certifier: [ModelIntegrityChecker[T]],
    ):
        """
        Args:
            assembler: [ModelAssembler[T]],
            root_certifier: [ModelRootCertifier[T]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> [ModelBuilder[T]]:
        return cast([ModelBuilder[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [ModelIntegrityChecker[T]]:
        return cast([ModelIntegrityChecker[T]], super().integrity_checker)