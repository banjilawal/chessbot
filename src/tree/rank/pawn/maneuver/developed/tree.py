# src/tree/pawn/maneuver/developed/tree.py

"""
Module: tree.pawn.maneuver.developed.tree
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from tree import ManeuverVectorSpan, VectorTree


class DevelopedManeuverVectorSpan(ManeuverVectorSpan):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from a DevelopedPawn's ManeuverSignature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        PawnVectorSpan
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
    
    
