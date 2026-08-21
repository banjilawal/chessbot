# src/assurance/manifest/nulls/node/roster.py

"""
Module: assurance.manifest.nulls.node.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from assurance import NullRoster
from err import NodeBlueprintNullException, NodeCarrierNullException, NodeNullException
from domain.node import Node


@dataclass
class NodeNullRoster(NullRoster[Node]):
    model: NodeNullException
    carrier: NodeCarrierNullException
    blueprint: NodeBlueprintNullException