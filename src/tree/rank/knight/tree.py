# src/tree/rank/knight/tree.py

"""
Module: tree.rank.knight.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations


from model import Knight
from tree import RankVectorSpan, VectorTree

class KnightVectorSpan(RankVectorSpan[Knight]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from a Knight's signature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        RankVectorSpan
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
