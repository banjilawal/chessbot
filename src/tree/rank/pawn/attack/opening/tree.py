# src/tree/pawn/attack/opening/tree.py

"""
Module: tree.pawn.attack.opening.tree
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from tree import AttackVectorSpan, VectorTree


class OpeningAttackVectorSpan(AttackVectorSpan):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from an OpeningPawn's AttackSignature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        PawnVectorSpan
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
   
    
    
