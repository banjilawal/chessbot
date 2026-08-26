# src/domain/metadata/unions/model/snapshot/manifest.py

"""
Module: domain.metadata.unions.model.snapshot.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Snapshot, SnapshotBlueprint, SnapshotCarrier, SnapshotSearchContext


@dataclass
class SnapshotTypeUnions(ModelTypeUnions[Snapshot]):
    """
    Role:
        -  Metadata

    Responsibilities:
        1. Catalog of data unions a Snapshot uses in the domain.

    Attributes:
        model: Type[Snapshot] = Snapshot
        carrier: Type[SnapshotCarrier] = SnapshotCarrier
        blueprint: Type[SnapshotBlueprint] = SnapshotBlueprint
        search_context: Type[SnapshotSearchContext] = SnapshotSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Snapshot] = Snapshot
    carrier: Type[SnapshotCarrier] = SnapshotCarrier
    blueprint: Type[SnapshotBlueprint] = SnapshotBlueprint
    search_context: Type[SnapshotSearchContext] = SnapshotSearchContext