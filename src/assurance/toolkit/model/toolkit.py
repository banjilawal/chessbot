# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from assurance import AttributeHelperTable
from domain import Model, ObjectManifest

T = TypeVar("T", bound="Model")


class ModelValidationToolkit(ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
        helper: HelperTable[T]
        metadata: ObjectManifest[T]

    Provides:

    Super Class:
    """
    _metadata: ObjectManifest[T]
    _helper: AttributeHelperTable[T]
    
    
    def __init__(
            self,
            helper: AttributeHelperTable[T],
            metadata: ObjectManifest[T],
    ):
        """
        Args:
            helper: HelperTable[T]
            metadata: ObjectManifest[T]
        """
        self._helper = helper
        self._metadata = metadata
    
    
    @property
    def helper(self) -> AttributeHelperTable[T]:
        return self._helper
    
    @property
    def metadata(self) -> ObjectManifest[T]:
        return self._metadata