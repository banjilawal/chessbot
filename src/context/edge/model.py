# src/model/state/context/edge/model/state.py

"""
Module: model.state.context.edge.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from future import annotations
from typing import Optional



from model import Board, Context, Coord, Edge, Node, Token


class EdgeContext(Context[Edge]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        currentposition:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        openingsquarename: Optional[str]

    Provides:
        -   todict() -> Dict[str, Any]

    Super Class:
        Context
    """
    label: Optional[int] = None
    head: Optional[Node] = None
    tail: Optional[Node] = None
    weight: Optional[int] = None
    distance: Optional[int] = None
    heuristic: Optional[int] =  None
  
  
    def todict(self) -> dict:

        return {
            "label": self.label,
            "head": self.head,
            "tail": self.tail,
            "weight": self.weight,
            "distance": self.distance,
            "heuristic": self.heuristic,
        }