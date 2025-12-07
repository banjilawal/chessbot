# src/chess/piece/searcher/finder.py

"""
Module: chess.piece.searcher.searcher
Author: Banji Lawal
Created: 2025-10-18
version: 1.0.0
"""

from typing import List

from chess.team import Team
from chess.rank import Rank
from chess.coord import Coord

from chess.system import LoggingLevelRouter, Finder, SearchResult
from chess.piece import Piece, PieceContext, PieceContextValidator, PieceFinderException

class PieceFinder(Finder[Piece]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def find(
            cls,
            data_set: List[Piece],
            context: PieceContext,
            context_validator: PieceContextValidator = PieceContextValidator()
    ) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder.find"
        try:
            result = context_validator.validate(candidate=context)
            if result.is_failure():
                return SearchResult.failure(result.exception)
            
            if context.id is not None:
                return cls._find_by_id(data_set=data_set, id=context.id)
            
            if context.name is not None:
                return cls._find_by_name(data_set=data_set, name=context.name)
            
            if context.team is not None:
                return cls._find_by_tean(data_set=data_set, team=context.team)
            
            if context.rank is not None:
                return cls._find_by_rank(data_set=data_set, team=context.rank)
            
            if context.ransom is not None:
                return cls._find_by_ransom(data_set=data_set, ransom=context.ransom)
            
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )

    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_id(cls, data_set: List[Piece], id: int) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder._find_by_id"
        try:
            matches = [
                piece for piece in data_set if piece.id == id
            ]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_name(cls, data_set: List[Piece], name: str) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder._find_by_name"
        try:
            matches = [
                piece for piece in data_set if piece.name.upper() == name.upper()
            ]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_team(
            cls,
            data_set: List[Piece],
            team: Team
    ) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder._find_by_team"
        try:
            matches = [
                piece for piece in data_set if piece.team == team
            ]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_rank(cls, data_set: List[Piece], rank: Rank) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder._find_by_name"
        try:
            matches = [
                piece for piece in data_set if piece.rank == rank
            ]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_ransom(
            cls,
            data_set: List[Piece],
            ransom: int
    ) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder._find_by_team"
        try:
            matches = [
                piece for piece in data_set if piece.rank.ransom == ransom
            ]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _find_by_coord(
            cls,
            data_set: List[Piece],
            coord: Coord,
    ) -> SearchResult[List[Piece]]:
        """"""
        method = "PieceFinder._find_by_name"
        try:
            matches = [
                piece for piece in data_set if piece.current_position == coord
            ]
            if len(matches) == 0:
                return SearchResult.empty()
            
            if len(matches) >= 1:
                return SearchResult.success(payload=matches)
        except Exception as ex:
            return SearchResult.failure(
                PieceFinderException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceFinderException.DEFAULT_MESSAGE}"
                    )
                )
            )