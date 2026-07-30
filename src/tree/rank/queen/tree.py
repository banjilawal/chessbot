# src/tree/rank/queen/tree.py

"""
Module: tree.rank.queen.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations


from model import Queen
from tree import RankVectorSpan, VectorTree

class QueenVectorSpan(RankVectorSpan[Queen]):
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
