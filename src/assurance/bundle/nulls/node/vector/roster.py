# src/assurance/manifest/nulls/node/roster.py

"""
Module: assurance.manifest.nulls.node.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from assurance import NodeNullRoster
from err import VectorNodeBlueprintNullException, VectorNodeCarrierNullException, VectorNodeNullException


@dataclass
class VectorNodeNullRoster(NodeNullRoster):
    model: VectorNodeNullException = VectorNodeNullException()
    carrier: VectorNodeCarrierNullException = VectorNodeCarrierNullException()
    blueprint: VectorNodeBlueprintNullException = VectorNodeBlueprintNullException()