# src/toolkit/analyzer/itinerary/toolkit.py

"""
Module: toolkit.analyzer.itinerary.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import ItineraryException, ItineraryNullException
from analyzer import Itinerary
from toolkit import AnalyzerBootstrapperToolkit
from analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from validator import SquareValidator, TokenValidator, PrimingValidator


class ItineraryToolkit(AnalyzerBootstrapperToolkit[Itinerary]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for Arena tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        analyzer_type: Itinerary
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
    analyzer_type: Itinerary
    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    priming_validator: PrimingValidator = PrimingValidator()
    null_exception: ItineraryNullException = ItineraryNullException()
    token_freedom_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    square_token_relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()