# src/assurance/depend/toolkit/model/scalar/toolkit.py

"""
Module: assurance.depend.toolkit.model.scalar.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, ScalarWrapperDependency
from domain import Scalar, ScalarManifest, ScalarNullGroup, ScalarTypeUnion


class ScalarValidatorToolkit(ModelValidatorToolkit[Scalar]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Scalar attribute validators and type metadata.

    Attributes:
        helper: ScalarManifest
        metadata: ScalarWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[ScalarManifest] | None = None,
            wrapper: Optional[ScalarWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[ScalarManifest]
            metadata: Optional[ScalarWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or ScalarWrapperDependency(),
            metadata=metadata or ScalarManifest(),
        )
    
    @property
    def wrapper(self) -> ScalarWrapperDependency:
        return cast(ScalarWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> ScalarManifest:
        return cast(ScalarManifest, super().metadata)
    
    @property
    def nulls(self) -> ScalarNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> ScalarTypeUnion:
        return self.metadata.types