# src/logic/token/database/core/util/util.py

"""
Module: logic.token.database.core.handler.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.token import (
    TokenStackRosterHandler, TokenStackTokenHandler, TokenStackCrudHandler, TokenStackCountsAnalyzer
)

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
    _stats: TokenStackCountsAnalyzer
    _crud: TokenStackCrudHandler
    _token: TokenStackTokenHandler
    _roster: TokenStackRosterHandler
    
    def __init__(
            self,
            crud: TokenStackCrudHandler = TokenStackCrudHandler(),
            token: TokenStackTokenHandler = TokenStackTokenHandler(),
            roster: TokenStackRosterHandler = TokenStackRosterHandler(),
            stats: TokenStackCountsAnalyzer = TokenStackCountsAnalyzer(),
    ):
        self._stats = stats
        self._crud = crud
        self._token = token
        self._roster = roster
        
    @property
    def stats(self) -> TokenStackCountsAnalyzer:
        return self._stats
    
    @property
    def token(self) -> TokenStackTokenHandler:
        return self._token
    
    @property
    def roster(self) -> TokenStackRosterHandler:
        return self._roster
    
    @property
    def crud(self) -> TokenStackCrudHandler:
        return self._crud