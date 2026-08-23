# src/domain/metadata/nulls/model/snapshot/roster.py

"""
Module: domain.metadata.nulls.model.snapshot.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Snapshot
from err import (
    SnapshotBlueprintNullException, SnapshotCarrierNullException, SnapshotContextNullException, SnapshotNullException
)


@dataclass
class SnapshotNullExceptionRoster(ModelNullExceptionRoster[Snapshot]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Snapshot.

    Attributes:
        model: SnapshotNullException
        carrier: SnapshotCarrierNullException
        blueprint: SnapshotBlueprintNullException
        search_context: SnapshotContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: SnapshotNullException = SnapshotNullException()
    carrier: SnapshotCarrierNullException = SnapshotCarrierNullException()
    blueprint: SnapshotBlueprintNullException = SnapshotBlueprintNullException()
    search_context: SnapshotContextNullException = SnapshotContextNullException()