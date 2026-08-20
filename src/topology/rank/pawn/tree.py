# src/topology/pawn/tree.py

"""
Module: topology.pawn.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from model import Pawn
from tree import Topology, VectorTree


class PawnTopology(Topology[Pawn], ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions a projected from a Pawn's signature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        Topology
    """
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
