# src/domain/metadata/nulls/structure/roster.py

"""
Module: domain.metadata.nulls.structure.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from domain import NullExceptionRoster, Structure

T = TypeVar("T", bound="Structure")

@dataclass
class NodeNullRoster(NullExceptionRoster[T], ABC, Generic[T]):
    """
    Role:
        -  Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a StructuralWrapper.

    Attributes:
        model: NodeNullException
        carrier: EntityCarrierNullException
        blueprint: BlueprintNullException
        search_context: ContextNullException

    Provides:

    Super Class:
        NullExceptionRoster
    """
    model: NodeNullException
    carrier: EntityCarrierNullException
    blueprint: BlueprintNullException
    search_context: ContextNullException