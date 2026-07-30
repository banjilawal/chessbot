# src/tree/rank/pawn/tree.py

"""
Module: tree.rank.pawn.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations


from model import Pawn
from tree import RankVectorSpan, VectorTree

class PawnVectorSpan(RankVectorSpan[Pawn]):
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
