# src/domain/metadata/nulls/structure/node/roster.py

"""
Module: domain.metadata.nulls.structure.node.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from domain import Node, NullExceptionRoster
from err import (
    BlueprintNullException, StackContextNullException, EntityCarrierNullException, NodeBlueprintNullException,
    NodeCarrierNullException, NodeNullException
)


T = TypeVar("T", bound="Node")

@dataclass
class NodeNullRoster(NullExceptionRoster[T], ABC, Generic[T]):
    """
    Role:
        -  Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Node

    Attributes:
        model: NodeNullException
        carrier: EntityCarrierNullException
        blueprint: BlueprintNullException
        search_context: Optional[ContextNullException] = None

    Provides:

    Super Class:
        NullExceptionRoster
    """
    model: NodeNullException
    carrier: EntityCarrierNullException
    blueprint: BlueprintNullException
    search_context: Optional[StackContextNullException] = None