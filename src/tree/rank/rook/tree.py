# src/tree/rank/rook/tree.py

"""
Module: tree.rank.rook.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations


from model import Rook
from tree import RankVectorSpan, VectorTree

class RookVectorSpan(RankVectorSpan[Rook]):
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
