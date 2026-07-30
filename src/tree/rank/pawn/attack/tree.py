# src/tree/pawn/tree.py

"""
Module: tree.pawn.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from tree import PawnVectorSpan, VectorTree


class AttackVectorSpan(PawnVectorSpan):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions a projected from a Pawn's AttackSignature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        PawnVectorSpan
    """
        
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)

    
