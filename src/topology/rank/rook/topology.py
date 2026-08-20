# src/topology/rank/rook/tree.py

"""
Module: topology.rank.rook.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import  annotations

from collection import VectorTree
from model import Rook
from topology import Topology

class RookTopology(Topology[Rook]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from a Rook's signature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        Topology
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
