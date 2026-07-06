# src/toolkit/model/itinerary/toolkit.py

"""
Module: toolkit.model.itinerary.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import ItineraryException, ItineraryNullException
from model import Itinerary
from toolkit import ModelToolkit
from analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from validator import SquareValidator, TokenValidator, PrimingValidator


class ItineraryToolkit(ModelToolkit[Itinerary]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        model_type: Itinerary
        token_validator: TokenValidator
        square_validator: SquareValidator
        priming_validator: PrimingValidator
        null_exception: ItineraryNullException
        token_freedom_analyzer: TokenFreedomAnalyzer
        square_token_relation_analyzer: SquareTokenRelationAnalyzer
        
    Provides:

     Super Class:
         Toolkit
     """
    model_type: Itinerary
    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    priming_validator: PrimingValidator = PrimingValidator()
    null_exception: ItineraryNullException = ItineraryNullException()
    token_freedom_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    square_token_relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()