# src/toolkit/model/path/token/toolkit.py

"""
Module: toolkit.model.path.token.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from analyzer import SquareTokenRelationAnalyzer, TokenReadinessAnalyzer
from model import Square, Token
from result import BuildResult
from search import TokenOriginSearcher
from toolkit import Toolkit
from util import LoggingLevelRouter
from validation import SquareValidator, TokenValidator
from validation.destination import TokenDestinationRelationValidator

@dataclass
class TokenPathToolkit(Toolkit):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Collection of workers and services that are required for TokenPath tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        token_validator: TokenValidator
        square_validator: SquareValidator
        origin_searcher: TokenOriginSearcher
        readiness_analyzer: TokenReadinessAnalyzer
        relation_analyzer: SquareTokenRelationAnalyzer
        destination_validator: TokenDestinationRelationValidator

    Provides:

    Super Class:
    """
    token_validator: TokenValidator = TokenValidator()
    square_validator: SquareValidator = SquareValidator()
    origin_searcher: TokenOriginSearcher = TokenOriginSearcher()
    readiness_analyzer: TokenReadinessAnalyzer = TokenReadinessAnalyzer()
    relation_analyzer: SquareTokenRelationAnalyzer = SquareTokenRelationAnalyzer()
    destination_validator: TokenDestinationRelationValidator =  TokenDestinationRelationValidator()

    