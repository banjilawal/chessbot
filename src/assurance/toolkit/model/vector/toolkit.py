# src/assurance/toolkit/model/vector/toolkit.py

"""
Module: assurance.toolkit.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, VectorValidationWrapperDict
from domain import Vector, VectorManifest, VectorNullGroup, VectorTypeUnion


class VectorValidatorToolkit(ModelValidatorToolkit[Vector]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Vector attribute validators and type metadata.

    Attributes:
        helper: VectorManifest
        metadata: VectorHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[VectorManifest] | None = None,
            wrapper: Optional[VectorValidationWrapperDict] | None = None,
    ):
        """
        Args:
            wrapper: Optional[VectorManifest]
            metadata: Optional[VectorHelperTable]
        """
        super().__init__(
            wrapper=wrapper or VectorValidationWrapperDict(),
            metadata=metadata or VectorManifest(),
        )
    
    @property
    def wrapper(self) -> VectorValidationWrapperDict:
        return cast(VectorValidationWrapperDict, super().wrapper)
    
    @property
    def metadata(self) -> VectorManifest:
        return cast(VectorManifest, super().metadata)
    
    @property
    def nulls(self) -> VectorNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> VectorTypeUnion:
        return self.metadata.types