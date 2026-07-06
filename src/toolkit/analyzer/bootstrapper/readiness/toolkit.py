# src/toolkit/analyzer/readiness/toolkit.py

"""
Module: toolkit.analyzer.readiness.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bootstrapper import CombatantReadinessAnalyzer, KingReadinessAnalyzer, ReadinessAnalyzerBootstrapper
from err import TokenValidatorException
from toolkit import AnalyzerBootstrapperToolkit
from validator import TokenValidator


class ReadinessAnalyzerBootstrapperToolkit(
    AnalyzerBootstrapperToolkit[ReadinessAnalyzerBootstrapper]
):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Collection of workers and services that are required for
            ReadinessAnalyzerBootstrapper tasks.
        2.  Simplifies entry points.
        3.  No logic in the Toolkit.

    Attributes:
        board_service: BoardService
        identity_service: IdentityService
            
    Provides:

    Super Class:
        AnalyzerBootstrapperToolkit
    """

    token_validator: TokenValidator = TokenValidatorException()
    king_readiness_analyzer: KingReadinessAnalyzer  = KingReadinessAnalyzer()
    combatant_readiness_analyzer: (
        CombatantReadinessAnalyzer
    ) = CombatantReadinessAnalyzer()

        
    
    