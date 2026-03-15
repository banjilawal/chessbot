# src/logic/token/database/core/util/util.py

"""
Module: logic.token.database.core.handler.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.token import RankQuotaAnalyzer, TokenCollisionDetector, TokenStackCrudHandler


class TokenStackHandler:
    """
    # ROLE: Handler Manager

    # RESPONSIBILITIES:
    1.  Unifies TokenStackService utilities in one place.
    2.  Separates maintenance and debugging of
            *   Token operations.
            *   Capacity monitoring operations
        from  core data structure operations.
    3.  Manges Updates (state changes) responsibilities for the TokenStackService.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)
        *   token_map Dict[Toke, Token]
        *   stack_service (TokenStackService)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   stats_analyzer (TokenStacKAnalyzer)
            *   occupation_service (TokenStackTokenHandler)
        Inherited:
        None

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _crud: TokenStackCrudHandler
    _rank_quota_analyzer: RankQuotaAnalyzer
    _collision_detector: TokenCollisionDetector

    
    def __init__(
            self,
            crud: TokenStackCrudHandler = TokenStackCrudHandler(),
            rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
            collision_detector: TokenCollisionDetector = TokenCollisionDetector(),
    ):
        self._crud = crud
        self._collision_detector = collision_detector
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudHandler:
        return self._crud
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalyzer:
        return self._rank_quota_analyzer
    
    @property
    def collision_detector(self) -> TokenCollisionDetector:
        return self._collision_detector