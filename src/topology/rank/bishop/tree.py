# src/topology/rank/bishop/tree.py

"""
Module: topology.rank.bishop.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import  annotations


from domain.model import Bishop
from tree import Topology, VectorTree

class BishopTopology(Topology[Bishop]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from a Bishop's signature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        Topology
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
