# src/operation/toolkit/analyzer/readiness/toolkit.py

"""
Module: operation.toolkit.analyzer.readiness.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from bootstrapper import CombatantReadinessAnalyzer, KingReadinessAnalyzer, ReadinessAnalyzerBootstrapper
from err import TokenValidatorException
from operation.toolkit.analyzer.bootstrapper.readiness.toolkit import AnalyzerBootstrapperToolkit
from assurance.validator import TokenValidator


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

        
    
    