# src/blueprint/model/itinerary/blueprint.py

"""
Module: blueprint.model.itinerary.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from blueprint import Blueprint
from err import ItineraryNullException
from model import Itinerary, Square, Token


@dataclass
class ItineraryBlueprint(Blueprint[Itinerary]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Itinerary object.

    Attributes:
        source: Square
        destination: Square
        traveler: Token
        null_exception: ItineraryNullException
        model_type: Itinerary
        
    Provides:

     Super Class:
        Blueprint
     """
    source: Square
    destination: Square
    traveler: Token

    null_exception: ItineraryNullException = ItineraryNullException()
    model_type: Itinerary = Itinerary
