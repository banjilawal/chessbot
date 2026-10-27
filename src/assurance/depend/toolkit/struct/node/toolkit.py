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

from assurance import NodeServiceDependency, StructLayerToolkit
from domain import Node, NodeManifest, NodeNullWarningSet, NodeLayer

T = TypeVar("T", bound="Node")


class NodeLayerToolkit(StructLayerToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: NodeServiceDependency[T]
            manifest: NodeManifest[T]

    Provides:

    Super Class:
        StructLayerToolkit
    """
    
    def __init__(
            self,
            dependency: NodeServiceDependency[T],
            manifest: NodeManifest[T],
    ):
        """
            wrapper: NodeServiceDependency[T]
            manifest: NodeManifest[T]
        """
        super().__init__(dependency=dependency, manifest=manifest)
    
    
    @property
    def dependency(self) -> NodeServiceDependency[T]:
        return cast(NodeServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> NodeManifest[T]:
        return cast(NodeManifest, super().manifest)
    
    @property
    def nulls(self) -> NodeNullWarningSet[T]:
        return self.manifest.nulls
    
    @property
    def types(self) -> NodeLayer[T]:
        return self.manifest.types