# src/logic/square/database/core/util/util.py

"""
Module: logic.square.database.core.util.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations

from logic.square import SquareStackTokenHandler, SquareStackCrudHandler, SquareStackAnalyzer

class SquareStackUtil:
    """
    # ROLE: Utilities, Update Management Statistics.

    # RESPONSIBILITIES:
    1.  Unifies SquareStackService utilities in one place.
    2.  Separates maintenance and debugging of
            *   Token operations.
            *   Capacity monitoring operations
        from  core data structure operations.
    3.  Manges Updates (state changes) responsibilities for the SquareStackService.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)
        *   token_map Dict[Toke, Square]
        *   stack_service (SquareStackService)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:
        Local:
            *   stats_analyzer (SquareStacKAnalyzer)
            *   occupation_service (SquareStackTokenHandler)
        Inherited:
        None

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _crud: SquareStackCrudHandler
    _stats_analyzer: SquareStackAnalyzer
    _occupation_service: SquareStackTokenHandler
    
    def __init__(
            self,
            crud_handler: SquareStackCrudHandler = SquareStackCrudHandler(),
            stats_analyzer: SquareStackAnalyzer = SquareStackAnalyzer(),
            occupation_service: SquareStackTokenHandler = SquareStackTokenHandler(),
    ):
        self._crud = crud_handler
        self._stats_analyzer = stats_analyzer
        self._occupation_service = occupation_service
        
    @property
    def stats_analyzer(self) -> SquareStackAnalyzer:
        return self._stats_analyzer
    
    @property
    def occupation_service(self) -> SquareStackTokenHandler:
        return self._occupation_service
    
    @property
    def crud(self) -> SquareStackCrudHandler:
        return self._crud