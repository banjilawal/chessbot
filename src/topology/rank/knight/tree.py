# src/topology/rank/knight/tree.py

"""
Module: topology.rank.knight.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import  annotations


from domain.model import Knight
from tree import Topology, VectorTree

class KnightTopology(Topology[Knight]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from a Knight's signature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        Topology
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
