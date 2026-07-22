# src/toolkit/builder/model/toolkit.py

"""
Module: toolkit.builder.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from assembler import ModelAssembler
from root import ModelRootCertifier
from toolkit import BuilderToolkit


T = TypeVar("T", bound="Model")

class ModelBuildToolkit(BuilderToolkit, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Role:
        -   Dependency Management

    Attributes:
        assembler: ModelAssembler[T],
        root_certifier: ModelRootCertifier[T]
        
    Provides:
    
    Super Class:
        BuildToolkit
    """
    
    def __init__(
            self,
            assembler: [ModelAssembler[T]],
            root_certifier: [ModelRootCertifier[T]],
    ):
        """
        Args:
            assembler: [ModelAssembler[T]]
            root_certifier: [ModelRootCertifier[T]]
        """
        super().__init__(assembler=assembler, root_certifier=root_certifier)

        
    @property
    def assembler(self) -> [ModelAssembler[T]]:
        return cast([ModelAssembler[T]], super()._assembler)
        
    @property
    def root_certifier(self) -> [ModelRootCertifier[T]]:
        return cast([ModelRootCertifier[T]], self._root_certifier)