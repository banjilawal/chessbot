# src/model/itinerary/model.py

"""
Module: model.itinerary.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model.square import Square
from model.token import Token


@dataclass
class Itinerary:
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the source and destination squares a token wants to travel between.

    Attributes:
        id: int
        token: Token
        source: Square
        destination: Square

    Provides:

    Super Class:
    """
    id: int
    token: Token
    source: Square
    destination: Square

    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self.source:
            return True
        if isinstance(other, Itinerary):
            return (
                    self.id == other.id and
                    self.token == other.token and
                    self.source == other.source and
                    self.destination == other.destination
            )
        return False
        
        
        
    