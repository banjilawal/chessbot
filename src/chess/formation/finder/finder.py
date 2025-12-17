# src/chess/battleOrder/battleOrder_schema/finder/finder.py

"""
Module: chess.battleOrder.battleOrder_schema.finder.finder
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from typing import List


from chess.system import Finder, GameColor, LoggingLevelRouter, SearchResult
from chess.battleOrder import (
    NullBattleOrderException, BattleOrderColorBoundsException, BattleOrderNameBoundsException, BattleOrder, BattleOrderContext,
    BattleOrderContextValidator, BattleOrderFinderException
)


class BattleOrderFinder(Finder[BattleOrder]):
    """
    # ROLE: Finder

    # RESPONSIBILITIES:
    1.  Search BattleOrder collections for items which match the attribute target specified in the BattleOrderContext parameter.
    2.  Safely forward any errors encountered during a search to the caller.

    # PARENT:
        *   Finder

    # PROVIDES:
        *   BattleOrderFinder:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
        

            
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_color(cls, color: GameColor) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get the BattleOrder which matches the target color.
        2.  If no match is found return an exception.

        # Parameters:
            *   color (BattleOrderColor)

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On success: List[BattleOrder] in the payload.
            - On failure: Exception.

        # Raises:
            *   BattleOrderColorBoundsException
            *   BattleOrderFinderException
        """
        method = "BattleOrderFinder._find_by_color"
        try:
            if color in BattleOrder.color:
                return SearchResult.success(List[BattleOrder.color])
            # If a match is not found return an exception. Its important to know if no battleOrder_schema has that color.
            return SearchResult.failure(
                BattleOrderColorBoundsException(f"{method}: {BattleOrderColorBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside an BattleOrderFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderFinderException(ex=ex, message=f"{method}: {BattleOrderFinderException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, name: str) -> SearchResult[List[BattleOrder]]:
        """
        # Action:
        1.  Get the BattleOrder which matches the target name.
        2.  If no match is found return an exception.

        # Parameters:
            *   name (str)

        # Returns:
        SearchResult[List[BattleOrder]] containing either:
            - On success: List[BattleOrder] in the payload.
            - On failure: Exception.

        # Raises:
            *   BattleOrderNameBoundsException
            *   BattleOrderFinderException
        """
        method = "BattleOrderFinder._find_by_name"
        try:
            if name.upper() in BattleOrder.name.upper():
                return SearchResult.success(List[BattleOrder.name])
            # If a match is not found return an exception. Its important to know if no battleOrder_schema has that name.
            return SearchResult.failure(
                BattleOrderColorBoundsException(f"{method}: {BattleOrderNameBoundsException.DEFAULT_MESSAGE}")
            )
        # Finally, if some exception is not handled by the checks wrap it inside an BattleOrderFinderException
        # then, return the exception chain inside a SearchResult.
        except Exception as ex:
            return SearchResult.failure(
                BattleOrderFinderException(ex=ex, message=f"{method}: {BattleOrderFinderException.DEFAULT_MESSAGE}")
            )