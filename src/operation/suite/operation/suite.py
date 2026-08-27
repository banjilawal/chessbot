# src/operation/suite/operation/suite.py

"""
Module: operation.suite.operation.suite
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Any, Generic, TypeVar

from assurance import Validator
from fabrication import Builder
from operation.suite import Suite

T = TypeVar("T", bound="Model")


class OperationSuite(Suite, Generic[T]):
    """
    Role:
        - Dependency Container
        -  Dynamic Dependency Provider

    Responsibilities:
        1.  Contains the operations that can be performed on a model.

    Attributes:
            builder: Builder[T]
            validator: Validator[T]
            toolkit: ModelToolkit[T]

    Provides:

    Super Class:

    Notes:
        -  Suite for an empty class which makes managing toolkits easier.
        -  Any toolkits for a suite should be a Suite subclass.
    """
    _builder: Builder[T]
    _validator: Validator[T]
    _toolkit: ModelToolkit[T]
    _entries: dict[str, Any] = {}
    
    def __init__(self, toolkit: ModelToolkit[T], validator: Validator[T], builder: Builder[T]):
        """
        Args:
            builder: Builder[T]
            validator: Validator[T]
            toolkit: ModelToolkit[T]
        """
        self._entries = {
            "builder": builder,
            "validator": validator,
            "toolkit": toolkit,
        }
        self._toolkit = toolkit
        self._builder = builder
        self._validator = validator
    
    @property
    def toolkit(self) -> ModelToolkit[T]:
        return self._toolkit
    
    @property
    def builder(self) -> Builder[T]:
        return self._builder
    
    @property
    def validator(self) -> Validator[T]:
        return self._validator
