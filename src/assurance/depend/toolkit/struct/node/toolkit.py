# src/assurance/depend/toolkit/struct/node.toolkit.py

"""
Module: assurance.depend.toolkit.struct.node.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import NodeDependency, StructValidatorToolkit
from domain import Node, NodeManifest, NodeNullGroup, NodeTypeUnion

T = TypeVar("T", bound="Node")


class NodeValidatorToolkit(StructValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: NodeWrapperDependency[T]
            metadata: NodeManifest[T]

    Provides:

    Super Class:
        StructValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: NodeDependency[T],
            metadata: NodeManifest[T],
    ):
        """
            wrapper: NodeWrapperDependency[T]
            metadata: NodeManifest[T]
        """
        super().__init__(wrapper=wrapper, metadata=metadata)
    
    
    @property
    def wrapper(self) -> NodeDependency[T]:
        return cast(NodeDependency, super().wrapper)
    
    @property
    def metadata(self) -> NodeManifest[T]:
        return cast(NodeManifest, super().metadata)
    
    @property
    def nulls(self) -> NodeNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> NodeTypeUnion[T]:
        return self.metadata.types