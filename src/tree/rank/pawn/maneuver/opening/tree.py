# src/tree/pawn/maneuver/opening/tree.py

"""
Module: tree.pawn.maneuver.opening.tree
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from tree import ManeuverVectorSpan, VectorTree


class OpeningManeuverVectorSpan(ManeuverVectorSpan):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Positions projected from an OpeningPawn's ManeuverSignature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
        PawnVectorSpan
    """
    
    def __init__(self, tree: VectorTree):
        super().__init__(tree=tree)
   
    
    
