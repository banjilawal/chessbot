# src/domain/metadata/nulls/vector/manifest.py

"""
Module: domain.metadata.nulls.vector.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from assurance import NullRoster
from err import VectorBlueprintNullException, VectorCarrierNullException, VectorNullException
from domain.model import Vector


@dataclass
class VectorNullRoster(NullRoster[Vector]):
    model: VectorNullException = VectorNullException()
    carrier: VectorCarrierNullException = VectorCarrierNullException()
    blueprint: VectorBlueprintNullException = VectorBlueprintNullException()