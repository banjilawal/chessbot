# src/logic/token/database/core/util/util.py

"""
Module: logic.token.database.core.handler.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.formation import FormationService
from logic.rank import RankService
from logic.token import (
    TokenStackRosterHandler, TokenStackTokenHandler, TokenStackCrudHandler, TokenStackCountsAnalyzer
)
from logic.token.database.core.handler.quota import RankQuotaAnalyzer


class TokenStackHandler:
    """
    # ROLE: Utilities, Update Management Statistics.

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
    _rank_service: RankService
    _formation_service: FormationService
    _rank_quota_analyzer: RankQuotaAnalyzer
    
    def __init__(
            self,
            rank_service: RankService = RankService(),
            crud: TokenStackCrudHandler = TokenStackCrudHandler(),
            formation_service: FormationService = FormationService(),
            rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
    ):
        self._crud = crud
        self._rank_service = rank_service
        self._formation_service = formation_service
        self._rank_quota_analyzer = rank_quota_analyzer

    @property
    def crud(self) -> TokenStackCrudHandler:
        return self._crud
    
    @property
    def rank_service(self) -> RankService:
        return self._rank_service
    
    @property
    def formation_service(self) -> FormationService:
        return self._formation_service
    
    @property
    def rank_quota_analyzer(self) -> RankQuotaAnalyzer:
        return self._rank_quota_analyzer