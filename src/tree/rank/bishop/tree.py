# src/tree/rank/bishop/tree.py

"""
Module: tree.rank.bishop.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import  annotations


from model import Bishop
from tree import RankVectorSpan, VectorTree

class BishopVectorSpan(RankVectorSpan[Bishop]):
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
