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
    source: Square
    destination: Square
    traveler: Token
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self.source:
            return True
        if isinstance(other, Itinerary):
            return (
                    self.traveler == other.traveler and
                    self.source == other.source and
                    self.destination == other.destination
            )
        return False
        
        
        
    