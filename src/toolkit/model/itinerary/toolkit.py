# src/toolkit/model/itinerary/toolkit.py

"""
Module: toolkit.model.itinerary.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import SquareTokenRelationAnalyzer, TokenFreedomAnalyzer
from model import Itinerary
from toolkit import Toolkit
from validation import SquareValidator, TokenValidator


class ItineraryToolkit(Toolkit[Itinerary]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        square_validator: SquareValidator
        token_freedom_analyzer: TokenFreedomAnalyzer
        square_token_relation_analyzer: SquareTokenRelationAnalyzer
        
    Provides:

     Super Class:
         Toolkit
     """
    square_validator: SquareValidator = SquareValidator()
    token_freedom_analyzer: TokenFreedomAnalyzer = TokenFreedomAnalyzer()
    square_token_relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()