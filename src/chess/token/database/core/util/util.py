# src/chess/token/database/core/util/util.py

"""
Module: chess.token.database.core.util.util
Author: Banji Lawal
Created: 2025-02-21
version: 1.0.0
"""

from __future__ import annotations

from chess.rank import RankService
from chess.formation import FormationService
from chess.token import RankQuotaAnalyzer


class TokenStackUtil:
    _rank_service: RankService
    _formation_service: FormationService
    _rank_quota_analyzer: RankQuotaAnalyzer

    def __init__(
            self,
            rank_service: RankService = RankService(),
            formation_service: FormationService = FormationService(),
            rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
    ):
        self._rank_service = rank_service
        self._formation_service = formation_service
        self._rank_quota_analyzer = rank_quota_analyzer
        
    @@property
    def (self) -> RankService:
        return self._rank_service
        
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalyzer:
        return self._rank_quota_analyzer